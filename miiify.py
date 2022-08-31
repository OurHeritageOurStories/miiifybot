import requests


class Miiify:
    def __init__(self, ctx):
        self.miiify_local_url = ctx.miiify_local_url
        self.miiify_remote_url = ctx.miiify_remote_url
        self.container = ctx.container
        self.logger = ctx.logger

    def host(self, url):
        lis = url.split('/')
        assert len(lis) == 5
        return(lis[2])

    def __annotation_payload(self, author, body, target):
        dict = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
            "motivation": "commenting",
            "body": {"type": "TextualBody", "value": body, "format": "text/plain"},
            "target": target,
            "creator": {"name": author}
        }
        return dict

    def __container_payload(self, label):
        dict = {
            "@context": [
                "http://www.w3.org/ns/anno.jsonld",
                "http://www.w3.org/ns/ldp.jsonld"
            ],
            "type": ["BasicContainer", "AnnotationCollection"],
            "label": label
        }
        return dict

    def __basic_headers(self):
        dict = {'User-Agent': 'miiifybot 0.1', 'Host': self.host(self.miiify_remote_url)}
        return dict

    def __slug_headers(self, slug):
        dict = self.__basic_headers()
        dict['Slug'] = slug
        return dict


    def is_alive(self):
        lis = self.miiify_local_url.split('/')
        assert len(lis) == 5
        url = '/'.join(lis[0:3]) # remove /annotations/
        headers = self.__basic_headers()
        try:
            response = requests.get(url, verify=False, headers=headers)
        except:
            return False
        else:
            return response.status_code == 200


    def create_annotation(self, author, body, target):

        url = f"{self.miiify_local_url}{self.container}/"
        headers = self.__basic_headers()
        payload = self.__annotation_payload(author, body, target)
        response = requests.post(
            url, json=payload, verify=False, headers=headers)
        return response.status_code

    def create_container(self, name):
        url = self.miiify_local_url
        headers = self.__slug_headers(self.container)
        payload = self.__container_payload(name)
        response = requests.post(
            url, json=payload, verify=False, headers=headers)
        return response.status_code


    def delete_annotation(self, id):
        url = id
        headers = self.__basic_headers()
        response = requests.delete(
            url, verify=False, headers=headers)
        return response.status_code


    def __parse(self, data, target):
        lis = data['items']
        target_lis = list(filter(lambda x: x['target'] == target, lis))
        if target_lis == []:
            return "no contributions on this item"
        else:
            res_lis = list(
                map(lambda x: f"*{x['body']['value']}* by **{x['creator']['name']}**", target_lis))
            res_str = '\n'.join(res_lis)
            return res_str

    def read_annotation(self, target):
        url = f"{self.miiify_remote_url}{self.container}"
        headers = self.__basic_headers()
        try:
            response = requests.get(url, verify=True, headers=headers)
        except Exception as e:
            self.logger.error(e)
            return f"I am having problems accessing {url}"
        else:
            try:
                data = response.json()
            except Exception as e:
                self.logger.error(e)   
                return f"I am having problems reading the JSON back from {url}" 
            else:
                return self.__parse(data, target)

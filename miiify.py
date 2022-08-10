import requests


class Miiify:
    def __init__(self, ctx):
        self.miiify_url = ctx.miiify_url
        self.container = ctx.container

    def __annotation_payload(self, author, body, target):
        dict = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
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

    def __annotation_headers(self):
        dict = {'User-Agent': 'miiifybot 0.1'}
        return dict

    def __container_headers(self, slug):
        dict = {'User-Agent': 'miiifybot 0.1', 'Slug': slug}
        return dict

    def create_annotation(self, author, body, target):
        url = f"{self.miiify_url}{self.container}/"
        headers = self.__annotation_headers()
        payload = self.__annotation_payload(author, body, target)
        response = requests.post(
            url, json=payload, verify=False, headers=headers)
        return response.status_code

    def create_container(self, name):
        url = self.miiify_url
        headers = self.__container_headers(self.container)
        payload = self.__container_payload(name)
        response = requests.post(
            url, json=payload, verify=False, headers=headers)
        return response.status_code


    def delete_annotation(self, id):
        url = id
        headers = self.__annotation_headers()
        response = requests.delete(
            url, verify=False, headers=headers)
        return response.status_code


    def __parse(self, data, item):
        lis = data['first']['items']
        target_lis = list(filter(lambda x: x['target'] == item, lis))
        res_lis = list(
            map(lambda x: {x['creator']['name'], x['body']['value']}, target_lis))
        return str(res_lis)

    def read_annotation(self, item):
        url = f"{self.miiify_url}{self.container}/"
        headers = self.__annotation_headers()
        response = requests.get(url, verify=False, headers=headers)
        data = response.json()
        return self.__parse(data, item)

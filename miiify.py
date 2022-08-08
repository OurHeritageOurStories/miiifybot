import requests


class Miiify:
    def __init__(self, ctx):
        self.miiify_url = ctx.miiify_url

    def __create_payload(self, author, body, target):
        dict = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
            "body": {"type": "TextualBody", "value": body, "format": "text/plain"},
            "target": target,
            "creator": {"name": author}
        }
        return dict

    def __create_headers(self):
        dict = {'User-Agent': 'miiifybot 0.1'}
        return dict

    def create_annotation(self, author, body, target):
        url = self.miiify_url
        headers = self.__create_headers()
        payload = self.__create_payload(author, body, target)
        response = requests.post(
            url, json=payload, verify=False, headers=headers)
        return response.status_code

    def __parse(self, data, item):
        lis = data['first']['items']
        target_lis = list(filter(lambda x: x['target'] == item, lis))
        res_lis = list(map(lambda x: { x['body']['creator']['name'], x['body']['value'] }, target_lis))
        return str(res_lis)

    def read_annotation(self, item):
        url = self.miiify_url
        headers = self.__create_headers()
        response = requests.get(url, verify=False, headers=headers)
        data = response.json()
        return self.__parse(data, item)

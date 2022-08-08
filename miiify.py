import requests

class Miiify:
    def __init__(self, ctx):
        self.miiify_url = ctx.miiify_url

    def __create_payload(self, body, target):
        dict = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
            "body": {"type": "TextualBody", "value": body, "format": "text/plain"},
            "target": target
        }
        return dict

    def __create_headers(self):
        dict = {'User-Agent': 'miiifybot 0.1'}
        return dict


    def create_annotation(self, body, target):
        url = self.miiify_url
        headers = self.__create_headers()
        payload = self.__create_payload(body, target)
        response = requests.post(
            url, json=payload, verify=False, headers=headers)
        return response.status_code


    def __parse(self, data, item):
        lis = data['first']['items']
        fl = list(filter(lambda x: x['target'] == item, lis))
        return "completed read"

    def read_annotation(self, item):
        url = self.miiify_url
        headers = self.__create_headers()
        response = requests.get(url, verify=False, headers=headers)
        data = response.json()
        return self.__parse(data, item)

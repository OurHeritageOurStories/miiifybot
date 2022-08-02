import requests

headers = {'User-Agent': 'miiifybot 0.1'}


class Miiify:
    def __init__(self, ctx):
        self.miiify_url = ctx.miiify_url

    def __create_dict(self, body, target):
        dict = {
            "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
            "body": {"type": "TextualBody", "value": body, "format": "text/plain"},
            "target": target
        }
        return dict

    def create_annotation(self, body, target):
        url = self.miiify_url
        payload = self.__create_dict(body, target)
        response = requests.post(
            url, json=payload, verify=False, headers=headers)
        return response.status_code

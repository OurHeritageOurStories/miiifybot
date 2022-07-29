import requests

headers = {'User-Agent': 'miiifybot 0.1'}


def createDict(body, target):
    dict = {
        "@context": "http://www.w3.org/ns/anno.jsonld",
        "type": "Annotation",
        "body": {"type": "TextualBody", "value": body, "format": "text/plain"},
        "target": target
    }
    return dict


def createAnnotation(ctx, body, target):
    url = ctx.url
    payload = createDict(body, target)
    response = requests.post(url, json=payload, verify=False, headers=headers)
    return response.status_code

import requests
from jsonpath_ng import jsonpath, parse

class Manifest:
    def __init__(self, ctx):
        self.manifest_url = ctx.manifest_url
        self.logger = ctx.logger
        self.target_prefix = ctx.target_prefix

    def target_exists(self, target):
        try:
            response = requests.get(self.manifest_url)
        except Exception as e:
            self.logger.error(e)
            return False
        else:
            if response.status_code == 200:
                json = response.json()
                jsonpath_expression = parse('items[*].items[*].items[*].target')
                lis = [match.value for match in jsonpath_expression.find(json)]
                if (self.target_prefix+target) in lis:
                    return True
                else:
                    return False
            else:
                self.logger.error(f"Got status code {response.status_code}")
                return False


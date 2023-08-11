
import requests

from collections import OrderedDict


def define_env(env):
    "Hook function"
    
    @env.macro
    def list_blogs(user: str):
        resp = requests.get(f'https://dev.to/api/articles?username={user}')
        output = {}
        for blog in resp.json():
            output[blog['title']] = {'url': blog['url'], 'description': blog['description']}
        return OrderedDict(sorted(output.items()))
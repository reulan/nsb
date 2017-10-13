"""
mpmsimo
10/12/2017 - damn after 8mo's

TwitchAPI
"""

import requests
import json

class TwitchAPI():
    """
    Twitch API placeholder
    """
# API Key
    def __init__(self):
        self.apikey = None

# URL settings
    #api_url = ?

    def _url(self, endpoint):
        """Returns a URL endpoint"""
        #url = ('https://{url}/wow/{ep}').format(url=api_url[region], ep=endpoint)
        url = ('https://us.api.battle.net/wow/{ep}').format(ep=endpoint)
        return url

    def _parameters(self, parameters):
        """Returns a dictionary of parameters including the API key."""
        if 'api_key' not in parameters.keys():
            parameters['apikey'] = self.apikey
        return parameters

# Request handling
    def get_resource(self, resource, params):
        response = requests.get(self._url(resource), self._parameters(params))
        print(response.url)
        return response.json()

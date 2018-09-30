"""
mpmsimo
12/25/17

Battlerite API
"""

import requests
import json

class BattleriteAPI():
    """Battlerite API
        Attributes:
            locale
            base_url
            parameters
            apikey
    """
# API Key
    def __init__(self):
        self.apikey = None

# URL settings
    #api_url = { "en_US": "us.api.battle.net" }

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

# Locale and Language settings
    region_list = ['en_US']
    region = region_list[0]

    def set_region(r):
        """Set the region locale."""
        if r in region_list:
            reg = r
        else:
            logger.info("Set region to en_US by default.")
            reg = 'en_US'
        return reg

# Request handling
    def get_resource(self, resource, params):
        response = requests.get(self._url(resource), self._parameters(params))
        logger.info(response.url)
        return response.json()

# Item API
 # Item
    def get_item(self, itemId):
        endpoint = ('item/{iId}'.format(iId=itemId))
        params = {'itemId': itemId,  'locale': self.region}
        return self.get_resource(endpoint, params)

# Character Profile API
# Guild Profile API
 # Item Set
# Data Resources
# PvP API
    def pvp_leaderboards(self, bracket):
        # 2v2, 3v3, 5v5, rbg
        endpoint = ('leaderboards/{brackets}'.format(brackets=bracket))
        self.get_resource(endpoint)

if __name__ == '__main__':
    wa = BattleriteAPI()
    #wa.pvp_leaderboards('2v2')

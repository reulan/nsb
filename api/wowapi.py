"""
mpmsimo
2/12/2017

WoW API - Item Level integration
"""

import requests
import json
import secret_info as si

global api_key
api_key = si.wow_api_key

class WowAPI():
    """World of Warcraft API class
        Attributes:
            locale
            base_url
    """
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
            parameters['apikey'] = api_key
            #params['api_key'] = api_key
        return parameters

# Locale and Language settings
    region_list = ['en_US']
    region = region_list[0]

    def set_region(r):
        """Set the region locale."""
        if r in region_list:
            reg = r
        else:
            print("Set region to en_US by default.")
            reg = 'en_US'
        return reg

# Request handling
    def get_resource(self, resource, params):
        response = requests.get(self._url(resource), self._parameters(params))
        print(response.url)
        print(response)
        print(response.json())
        return response

# Item API
 # Item
    def get_item(self, itemId):
        endpoint = ('item/{iId}'.format(iId=itemId))
        params = {'itemId': itemId,  'locale': self.region}
        self.get_resource(endpoint, params)

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
    wa = WowAPI()
    wa.get_item(18803)
    #wa.pvp_leaderboards('2v2')

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
    def get_resource(self, resource, _parameters):
        parameters = _parameters
        if 'api_key' not in parameters.keys():
            parameters['apikey'] = api_key
            #params['api_key'] = api_key

        response = requests.get(self._url(resource), params=parameters)
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
        print('Ran get_item')

if __name__ == '__main__':
    wa = WowAPI()
    wa.get_item(18803)

# Character Profile API
# Guild Profile API
 # Item Set
# Data Resources

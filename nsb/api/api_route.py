"""
api_route.py
Generates an API route which can be modified per API.
"""
import logging

import requests
from requests.auth import HTTPDigestAuth, HTTPBasicAuth

import apikey

logger = logging.getLogger('nsb')

class APIRoute(object):
    """Generate a URL which can be used to access an API."""

    def __init__(self, auth_type, username=None, apikey=None, endpoint=None, base_url=None, **kwargs):
        self.auth_type = auth_type
        self.username = username
        self.apikey = apikey
        self.endpoint = endpoint
        self.base_url = base_url

    def _url(self, path):
        """Returns a URL endpoint"""
        url = ('https://{bu}/{ep}/{p}').format(bu=self.base_url, ep=self.endpoint, p=path)
        return url

    def _headers(self, headers={}):
        """Returns a dictionary of API headers to be passed to the route."""
        # Always return json headers, cannot be overwritten atm
        headers = {'Content-Type': 'application/json'}
        return headers

    def _parameters(self, parameters={}):
        """Returns a dictionary of parameters including the API key."""
        return parameters

    def _data(self, data={}):
        """Returns a dictionary of API data to be passed to the route."""
        return data

    def _json(self, json={}):
        """The json json to be sent alongside the request."""
        return json

    def _auth(self):
        """
        Identifies the type of authentication needed:
          - HTTPDigestAuth
          - API Key passed in a parameter.
        """
        #HTTP Digest Authetication
        if self.auth_type is "http_digest":
            auth = HTTPDigestAuth(self.username, self.apikey)
        #HTTP Basic Auth
        elif self.auth_type is "basic_auth":
            auth = HTTPBasicAuth(self.username, self.apikey)
        elif self.auth_type is None:
            logger.info("You need to specfiy and auth type to connect to the API.")
        else:
            auth = HTTPDigestAuth(self.username, self.apikey)
        return auth

    def _request(self, method, path, headers={}, params={}, data={}, json={}):
        """Calls a specific type of request and passes in any additional fields if needed."""
        # http://docs.python-requests.org/en/master/api/
        if method is "GET":
            response = requests.get(self._url(path), headers=self._headers(headers), params=self._parameters(params), auth=self._auth())
        elif method is "POST":
            response = requests.post(self._url(path), headers=self._headers(headers), params=self._parameters(params), data=self._data(data), json=self._json(json), auth=self._auth())
        elif method is "DELETE":
            response = requests.delete(self._url(path), headers=self._headers(headers), auth=self._auth())
        else:
            response = requests.get(self._url(path), self._parameters(params), auth=self._auth())
        r = response

        #logger.info("api_route._request: [{m}] {ru} ({sc})".format(m=response.request, ru=response.url, sc=response.status_code))

        response.close()
        return r

def debug_request(request):
    """Prints out the request that would be sent to the API server."""
    # Make sure to change the request to requests.Request and pass in the method as the first argument
    # You could pass it into a list and take the first value of the list to make a copy of the var
    request = request.prepare()
    logger.info('{s}\n{mu}\n{h}\n\n{b}'.format(s='-----------START-----------',
                                            mu=request.method + ' ' + request.url,
                                            h='\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
                                            b=request.body,))

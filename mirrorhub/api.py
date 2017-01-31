"""Submodule of mirrorhub.

which provides an api client
"""
import requests as req


class APIClient():
    """Client class for API interaction."""

    URL = 'https://mirrorhub.io'

    def __init__(self, token):
        """Initialize a new APIClient."""
        self.token = token
        self.header = {'Grpc-Metadata-ClientToken': token}

    def _get(self, url):
        """Wrapper method for HTTP GET requests."""
        return req.get(self.URL + url, headers=self.header)

    def get_mirror_info(self):
        """Get the mirror details from the API.

        Returns:
            dict: data as JSON
        """
        return self._get('/v1/mirrors/self').text

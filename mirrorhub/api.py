"""Submodule of mirrorhub.

which provides an api client
"""


class APIClient():
    """Client class for API interaction."""

    def __init__(self, token):
        """Initialize a new APIClient."""
        self.token = token
        self.session = None

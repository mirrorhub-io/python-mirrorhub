'''submodule of mirrorhub, which provides an api client'''
import requests as req

class APIClient():
    def __init__(self, token):
        self.token = token
        self.session = None

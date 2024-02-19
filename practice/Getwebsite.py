# Classes are blueprint or prototypes
import requests


class Getwebsite:
    def __init__(self, name):
        self.name = name

    def getUrl(self):
        return requests.get(self.name)

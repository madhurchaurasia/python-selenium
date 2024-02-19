# Classes are blueprint or prototypes
from selenium import webdriver
import requests
import random
class Getwebsite:
    def __init__(self,name):
        self.name = name

    def getUrl(self):
        return requests.get(self.name)


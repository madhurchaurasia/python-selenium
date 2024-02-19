from practice import Getwebsite
from practice.Getwebsite import Getwebsite
from practice import myModule as mm
from selenium import webdriver
drive = webdriver.Chrome()
myurl = "https://www.google.com/"
s = Getwebsite(myurl)
print(s.getUrl())
print(mm.convertName(myurl))
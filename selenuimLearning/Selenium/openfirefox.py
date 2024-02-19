from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.python.org")
    print(driver.title)
    # search_bar = driver.find_element_by_name("q")
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.clear()
    search_bar.send_keys("getting started with python")
    search_bar.send_keys(Keys.RETURN)
    print(driver.current_url)
    driver.close()
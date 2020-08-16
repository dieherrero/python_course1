import time
import sys

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

from urllib.parse import urlparse


class Fetcher:
    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        print(self.url)

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.implicitly_wait.until(ec.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
                ))
        except:
            print("Fail")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        self.answer = soup.find_all(class_="_sPg")



        #s  ome searches doesnt have class_ _spg, so we have to add more classes with if statement:
        #  if not answer: self.answer = soup.find_all(class_="")[0]
        return self.answer[0].get_text()
#        self.driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest, time, re

class Sel(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://steamcommunity.com/app/522020/reviews/?browsefilter=toprated&snr=1_5_reviews_"
		self.verificationErrors = []
		self.accept_next_alert = True
	def test_sel(self):
		driver = self.driver
		delay = 3
		driver.get(self.base_url)
		for i in range(1,100):
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(4)
		html_source = driver.page_source
		data = html_source.encode('utf-8')
		file = open("reviews.html", 'w')
		file.write(data)
		file.close()
		


if __name__ == "__main__":
    unittest.main()
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


INTERESTING_URL = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

chrome_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_path)
browser = Chrome(service=browser_service)

browser.get(INTERESTING_URL)

import time
time.sleep(240)

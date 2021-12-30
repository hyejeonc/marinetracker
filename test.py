# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/
# https://wikidocs.net/6660
# https://www.fun-coding.org/crawl_basic2.html



import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://debristracker.org/data'

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

print(driver.current_url)

driver.implicitly_wait(time_to_wait=2)


# filter for all organization 
<div id="gatsby-announcer" style="position:absolute;top:0;width: 0px;height:1px;padding:0;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border:0;" aria-live="assertive" aria-atomic="true"></div>


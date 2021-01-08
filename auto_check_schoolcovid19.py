from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Chrome('D:\stdudent_covidcheck_auto-\chromedriver.exe')
url = 'https://hcs.eduro.go.kr/#/loginHome'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
#
# (
#     action.send_keys('용현중학교').key_down(Keys.TAB).pause(1)
#     .send_keys('김민성').key_down(Keys.TAB).pause(1)
#     .send_keys('050201').pause(1)
#     .perform()
# )
driver.find_element_by_css_selector('#btnConfirm2').click()
time.sleep(0.5)
driver.find_element_by_css_selector('#schul_name_input').click()
time.sleep(0.5)
driver.find_element_by_css_selector('#sidolabel').click()
time.sleep(0.5)
# driver.find_element_by_css_selector('#rspns02').click()
# time.sleep(1)
# driver.find_element_by_css_selector('#rspns070').click()
# time.sleep(1)
# driver.find_element_by_css_selector('#rspns080').click()
# time.sleep(1)
# driver.find_element_by_css_selector('#rspns090').click()
# time.sleep(1)
# driver.find_element_by_css_selector('#rspns090').click()
# driver.find_element_by_css_selector('#btnConfirm').click()
# time.sleep(1)

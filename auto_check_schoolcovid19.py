from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome('P:\\stdudent_covidcheck_auto\chromedriver.exe')
url = 'https://eduro.ice.go.kr/stv_cvd_co00_002.do'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

(
    action.send_keys('용현중학교').key_down(Keys.TAB).pause(1)
    .send_keys('김민성').key_down(Keys.TAB).pause(1)
    .send_keys('050201').pause(1)
    .perform()
)
driver.find_element_by_css_selector('#btnConfirm').click()
time.sleep(1)
driver.find_element_by_css_selector(f'#rspns011').click()
time.sleep(1)
driver.find_element_by_css_selector('#rspns02').click()
time.sleep(1)
driver.find_element_by_css_selector('#rspns070').click()
time.sleep(1)
driver.find_element_by_css_selector('#rspns080').click()
time.sleep(1)
driver.find_element_by_css_selector('#rspns090').click()
time.sleep(1)
driver.find_element_by_css_selector('#rspns090').click()
driver.find_element_by_css_selector('#btnConfirm').click()
time.sleep(1)

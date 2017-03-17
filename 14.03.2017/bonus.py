
from selenium import webdriver

import time
import os


geckodriver = os.path.join(os.path.dirname(os.path.abspath(__file__)),"geckodriver")
os.environ["webdriver.mozilla.driver"] = geckodriver

driver = webdriver.Firefox(geckodriver)
driver.get("https://habrahabr.ru")

register = driver.find_element_by_xpath("//a[@class='btn btn_x-large btn_navbar_registration']").click()
time.sleep(1)
form = driver.find_element_by_xpath("//form[@id='register_form']")
driver.find_element_by_name('email').send_keys("example@ukr.net")
driver.find_element_by_xpath("//input[@name='login']").send_keys("alex")
driver.find_element_by_xpath("//input[@name='password']").send_keys("alex1234")
driver.find_element_by_xpath("//input[@name='password2']").send_keys("alex1234")

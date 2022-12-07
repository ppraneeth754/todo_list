import selenium
import pickle
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

username='admin@2'
password='Admin123'

def scrolling(driver):
    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    return driver
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://127.0.0.1:5000/register")
driver.maximize_window()

sleep(2)
# driver.find_element_by_xpath("//a[text()='Register']").click()
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
sleep(2)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
sleep(2)
driver.find_element_by_xpath("//input[@name='password_re']").send_keys(password)
sleep(4)
driver.find_element_by_xpath("//input[@name='submit']").click() 
sleep(5)


username='admin'
password='123'
driver.find_element_by_xpath("//input[@name='username']").clear()
sleep(2)
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
sleep(4)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
sleep(3)
driver.find_element_by_xpath("//input[@name='password_re']").send_keys(password)
sleep(5)
driver.find_element_by_xpath("//input[@name='submit']").click() 
sleep(5)

# driver.get("http://127.0.0.1:5000/login")
# driver.maximize_window()
# driver.find_element_by_xpath("//a[text()='Register']").click()

username='admin12'
password='123'
driver.find_element_by_xpath("//input[@name='username']").clear()
sleep(3)
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
# sleep(3)
# driver.find_element_by_xpath("//input[@name='password']").clear()
# sleep(1)
# driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
# sleep(3)
# driver.find_element_by_xpath("//input[@name='password_re']").clear()
# sleep(1)
# driver.find_element_by_xpath("//input[@name='password_re']").send_keys(password)
sleep(4)
driver.find_element_by_xpath("//input[@name='submit']").click() 
sleep(5)

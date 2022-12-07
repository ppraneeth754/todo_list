import selenium
import pickle
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


username='smqa'
password='Admin1'
task_title = 'Title of the Task'
task_info = 'Description of the task'


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


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://127.0.0.1:5000/login")
driver.maximize_window()
sleep(2)
driver.find_element_by_xpath("//a[text()='Register']").click()
sleep(2)
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
sleep(3)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
sleep(3)
driver.find_element_by_xpath("//input[@name='password_re']").send_keys(password)
sleep(5)
driver.find_element_by_xpath("//input[@name='submit']").click() 
sleep(4)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
sleep(2)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
sleep(5)
driver.find_element_by_xpath("//input[@name='submit']").click()
driver.find_element_by_xpath("//div[@class='button-add-task position-fixed end-0 bottom-0 m-4']").click()
sleep(2)
driver.find_element_by_xpath("//input[@name='Task_Name']").send_keys(task_title)
sleep(5)
driver.find_element_by_xpath("//textarea[@name='Task_Info']").send_keys(task_info)
sleep(5)
element=driver.find_element_by_xpath("//textarea[@name='Task_Info']")
sleep(2)
driver.execute_script("arguments[0].setAttribute('style','height: 200px;')", element)
sleep(4)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='ADD']"))).click()
sleep(5)
driver.find_element_by_xpath("//a[text()='Logout']").click()
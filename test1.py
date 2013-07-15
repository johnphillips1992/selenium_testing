import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome driver
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.set_window_size(1300, 900)

driver.get("http://myaccount-dev.arch.tamu.edu")
try:
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))
    time.sleep(0.5)

    driver.set_window_size(800, 900)
    time.sleep(0.5)

    driver.set_window_size(300, 900)

    driver.get("https://myaccount-dev.arch.tamu.edu/accounts/login/")
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))

    inputElement = driver.find_element_by_name("username")
    inputElement.send_keys("johnphillips")

    inputElement = driver.find_element_by_name("password")
    inputElement.send_keys("Blobdoll###1")

    inputElement.submit()
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))

    driver.get("https://myaccount-dev.arch.tamu.edu/accounts/logout/")
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))
except:
    print "myaccount-dev.arch failed"

def test_site(site):
    driver.set_window_size(1300, 900)

    driver.get(site)
    try:
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "container")))
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 0);")
        driver.set_window_size(800, 900)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 0);")
        driver.set_window_size(300, 900)
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    except:
        print site + " failed"


test_site("http://chc-dev.arch.tamu.edu")

test_site("http://chsd-dev.arch.tamu.edu")

test_site("http://chud-dev.arch.tamu.edu")

test_site("http://colonias-dev.arch.tamu.edu")

test_site("http://cosc-dev.arch.tamu.edu")

test_site("http://creativity-dev.arch.tamu.edu")

test_site("http://crs-dev.arch.tamu.edu")

test_site("http://dept-dev.arch.tamu.edu")

test_site("http://hrrc-dev.arch.tamu.edu")

test_site("http://laup-dev.arch.tamu.edu")

test_site("http://one-dev.arch.tamu.edu")

test_site("http://payments-dev.arch.tamu.edu")

driver.get("http://pypi-dev.arch.tamu.edu")
try:
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
except:
    print "payments-dev.arch failed"

test_site("http://symposium-dev.arch.tamu.edu")

test_site("http://targetcities-dev.arch.tamu.edu")

test_site("http://viz-dev.arch.tamu.edu")

test_site("http://dev.arch.tamu.edu")

driver.quit()


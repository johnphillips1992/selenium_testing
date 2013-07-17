import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys

startMillis = int(round(time.time() * 1000))

errors = 0

# Create a new instance of the Chrome driver
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def test_site(site):
    global errors
    driver.get(site)
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "navbar")))
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "header")))
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "site-top-menu")))
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "footer")))
        return True
    except:
        print "Error: " + site + " failed"
        errors = errors + 1
        return False

test_site("http://myaccount-dev.arch.tamu.edu")
test_site("http://chc-dev.arch.tamu.edu")
test_site("http://chsd-dev.arch.tamu.edu")
test_site("http://chud-dev.arch.tamu.edu")
test_site("http://olonias-dev.arch.tamu.edu")
test_site("http://cosc-dev.arch.tamu.edu")
test_site("http://creativity-dev.arch.tamu.edu")
test_site("http://crs-dev.arch.tamu.edu")
test_site("http://dept-dev.arch.tamu.edu")
test_site("http://hrrc-dev.arch.tamu.edu")
test_site("http://laup-dev.arch.tamu.edu")
test_site("http://one-dev.arch.tamu.edu")
test_site("http://payments-dev.arch.tamu.edu")

# pypi.arch does not have a footer class
# so we test for the container and table tag.
driver.get("http://pypi-dev.arch.tamu.edu")
try:
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "container")))
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "table")))
except:
    print "pypi-dev.arch failed"

test_site("http://symposium-dev.arch.tamu.edu")
test_site("http://targetcities-dev.arch.tamu.edu")
test_site("http://viz-dev.arch.tamu.edu")
test_site("http://dev.arch.tamu.edu")

driver.quit()

endMillis = int(round(time.time() * 1000))
totalMillis = endMillis - startMillis
print "Test time: " + str(float(totalMillis)/1000) + " seconds"

print "Total errors: " + str(errors) + " errors"

if errors > 0:
    sys.exit(2)


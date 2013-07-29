import os
from selenium import webdriver
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

test_site("http://myaccount.arch.tamu.edu")
test_site("http://chc.arch.tamu.edu")
test_site("http://chsd.arch.tamu.edu")
test_site("http://chud.arch.tamu.edu")
test_site("http://colonias.arch.tamu.edu")
test_site("http://cosc.arch.tamu.edu")
test_site("http://creativity.arch.tamu.edu")
test_site("http://crs.arch.tamu.edu")
test_site("http://dept.arch.tamu.edu")
test_site("http://hrrc.arch.tamu.edu")
test_site("http://laup.arch.tamu.edu")
test_site("http://one.arch.tamu.edu")
test_site("http://payments.arch.tamu.edu")

# pypi.arch does not have a footer class
# so we test for the container and table tag.
driver.get("http://pypi.arch.tamu.edu")
try:
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "container")))
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "table")))
except:
    print "pypi.arch failed"

test_site("http://symposium.arch.tamu.edu")
test_site("http://targetcities.arch.tamu.edu")
test_site("http://viz.arch.tamu.edu")
driver.get("http://www.arch.tamu.edu")
try:
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "navbar")))
except:
    print "Error: http://www.arch.tamu.edu navbar failed"
    errors = errors + 1
try:
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header")))
except:
    print "Error: http://www.arch.tamu.edu header failed"
    errors = errors + 1

try:
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "site-top-menu")))
except:
    print "Error: http://www.arch.tamu.edu site-top-menu failed"
    errors = errors + 1

try:
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "footer")))
except:
    print "Error: http://www.arch.tamu.edu footer failed"
    errors = errors +1

try:
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "newsitems")))
except:
    print "Error: http://www.arch.tamu.edu newsitems failed"
    errors = errors +1

try:
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "upcoming-events")))
except:
    print "Error: http://www.arch.tamu.edu upcoming events failed"
    errors = errors +1

driver.quit()

endMillis = int(round(time.time() * 1000))
totalMillis = endMillis - startMillis
print "Test time: " + str(float(totalMillis)/1000) + " seconds"

print "Total errors: " + str(errors) + " errors"

if errors > 0:
    sys.exit(2)


import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time

start_millis = int(round(time.time() * 1000))

errors = 0

# Create a new instance of the Chrome driver
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.set_window_size(1300, 900)

def test_site(site):
    driver.get(site)
    try:
        element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "footer")))
        return True
    except:
        print site + " failed"
        errors = errors + 1
        return False

test_site("http://myaccount-dev.arch.tamu.edu")
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

# pypi.arch does not have a footer tag
# so we test for the table tag.
driver.get("http://pypi-dev.arch.tamu.edu")
try:
    element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "table")))
except:
    print "payments-dev.arch failed"

test_site("http://symposium-dev.arch.tamu.edu")
test_site("http://targetcities-dev.arch.tamu.edu")
test_site("http://viz-dev.arch.tamu.edu")
test_site("http://dev.arch.tamu.edu")

driver.quit()

end_millis = int(round(time.time() * 1000))
total_millis = end_millis - start_millis
print "Test time: " + str(float(total_millis)/1000) + " seconds"

print str(errors) + " errors"


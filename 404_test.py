import os
import time
import sys

from argparse import ArgumentParser

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

parser = ArgumentParser(description='Specify staging environment.')
parser.add_argument('-s', '--staging', action='store_true')

startMillis = int(round(time.time() * 1000))

errors = 0

# Create a new instance of the Chrome driver
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("http://www.arch.tamu.edu/this/is/a/test/")

try:
    search_box = driver.find_element_by_xpath("//form[@id='google_404']/p/input[@name='q']")

    text = search_box.get_attribute('value')

    if text != " this is a test ":
        errors = errors + 1
        print "Error: Search box does not contain the correct text."

except Exception as e:
    print "Error: Could not complet the test."
    print e

driver.quit()

endMillis = int(round(time.time() * 1000))
totalMillis = endMillis - startMillis
print "Test time: " + str(float(totalMillis)/1000) + " seconds"

print "Total errors: " + str(errors) + " errors"


if errors > 0:
    sys.exit(2)


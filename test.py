import os
import time
import sys

from argparse import ArgumentParser

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

parser = ArgumentParser(description='Set the environment to test')
parser.add_argument('-s', '--staging', action='store_true')

startMillis = int(round(time.time() * 1000))

errors = 0

# Create a new instance of the Chrome driver
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def check_tag(tag_name, site):
    global errors
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, tag_name)))
    except:
        print "Error: %s failed to display %s tag properly." % (site, tag_name)
        errors = errors + 1

def check_class(class_name, site):
    global errors
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    except:
        print "Error: %s failed to display %s class properly." % (site, 
                                                                  class_name)
        errors = errors + 1

def test_site(site):
    global errors
    driver.get(site)
    check_class("navbar", site)
    check_class("header", site)
    check_class("site-top-menu", site)
    check_class("footer", site)

if __name__ == '__main__':
    args = parser.parse_args()

    dev_str = ""

    if args.staging:
        dev_str = "-dev"

    test_site("http://myaccount%s.arch.tamu.edu" % dev_str)
    test_site("http://chc%s.arch.tamu.edu" % dev_str)
    test_site("http://chsd%s.arch.tamu.edu" % dev_str)
    test_site("http://chud%s.arch.tamu.edu" % dev_str)
    test_site("http://colonias%s.arch.tamu.edu" % dev_str)
    test_site("http://cosc%s.arch.tamu.edu" % dev_str)
    test_site("http://creativity%s.arch.tamu.edu" % dev_str)
    test_site("http://crs%s.arch.tamu.edu" % dev_str)
    test_site("http://dept%s.arch.tamu.edu" % dev_str)
    test_site("http://hrrc%s.arch.tamu.edu" % dev_str)
    test_site("http://laup%s.arch.tamu.edu" % dev_str)
    test_site("http://one%s.arch.tamu.edu" % dev_str)
    test_site("http://payments%s.arch.tamu.edu" % dev_str)
    test_site("http://symposium%s.arch.tamu.edu" % dev_str)
    test_site("http://targetcities%s.arch.tamu.edu" % dev_str)
    test_site("http://viz%s.arch.tamu.edu" % dev_str)

    # pypi.arch does not have a footer class
    # so we test for the container and table tag.
    site = "http://pypi%s.arch.tamu.edu" % dev_str
    driver.get(site)
    check_class("container", site)
    check_tag("table", site)

    if args.staging:
        site = "http://dev.arch.tamu.edu"
    else:
        site = "http://www.arch.tamu.edu"

    driver.get(site)
    check_class("navbar", site)
    check_class("header", site)
    check_class("site-top-menu", site)
    check_class("footer", site)
    check_class("newsitems", site)
    check_class("upcoming-events", site)

    driver.quit()

    endMillis = int(round(time.time() * 1000))
    totalMillis = endMillis - startMillis
    print "Test time: " + str(float(totalMillis)/1000) + " seconds"

    print "Total errors: " + str(errors) + " errors"

    if errors > 0:
        sys.exit(2)


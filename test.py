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

def check_tag(tag_name, site):
    global errors
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, tag_name)))
    except Exception as e:
        print "Error: %s failed to display %s tag properly." % (site, tag_name)
        print e
        errors = errors + 1

def check_class(class_name, site):
    global errors
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    except Exception as e:
        print "Error: %s failed to display %s class properly." % (site, 
                class_name)
        print e
        errors = errors + 1

def check_element(site, width, element, dimension, large, small):
    try:
        element_dimension = driver.find_element_by_xpath(element).size.get(dimension)

        if width == 1300 and element_dimension != large:
            print "Error: %s failed. %s has incorrect %s" % (site, 
                element, dimension)
            errors = errors + 1

        if width == 800 and element_dimension != small:
            print "Error: %s failed. %s has incorrect %s" % (site, 
                element, dimension)
            errors = errors + 1
    except Exception as e:
        print "Error %s failed to check %s" % (site, element)
        print e

def test_site(site):
    global errors
    driver.get(site)
    try:
        for width in [1300, 800, 300]:
            driver.set_window_size(width, 800)
            check_class("navbar", site)

            check_element(site, width, "//div[@class='navbar navbar-fixed-top']",
                    'height', 42, 52)

            if 'one' in site:
                check_element(site, width, "/html/body/div[@class='container']",
                        'width', 990, 724)
            else:
                check_element(site, width, "/html/body/div[@class='container']",
                        'width', 1000, 724)

            check_class("header", site)
            check_class("site-top-menu", site)
            check_class("footer", site)
    except Exception as e:
        print "Error: %s faild." % site
        print e
        errors = errors + 1

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

    site = "http://symposium%s.arch.tamu.edu" % dev_str
    driver.get(site)
    for width in [1300, 800, 300]:
        driver.set_window_size(width, 800)
        check_class("navbar", site)
        check_class("header", site)
        check_class("site-top-menu", site)
        check_class("footer", site)

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
    try:
        driver.get(site)
        for width in [1300, 800, 300]:
            driver.set_window_size(width, 800)
            check_class("navbar", site)

            check_element(site, width, "//div[@class='navbar navbar-fixed-top']",
                    'height', 42, 52)

            check_element(site, width, "/html/body/div[@class='container']",
                    'width', 1000, 724)

            check_element(site, width, "//div[@class='newsitems']",
                    'width', 660, 476)

            check_element(site, width, "//div[@class='upcoming-events']",
                    'width', 300, 208)

            check_element(site, width, "//div[@class='banner span12']",
                    'height', 309, 228)

            check_class("header", site)
            check_class("site-top-menu", site)
            check_class("footer", site)
            check_class("newsitems", site)
            check_class("upcoming-events", site)

    except Exception as e:
        print "Error: %s failed." % (site)
        print e
        errors = errors + 1

    driver.quit()

    endMillis = int(round(time.time() * 1000))
    totalMillis = endMillis - startMillis
    print "Test time: " + str(float(totalMillis)/1000) + " seconds"

    print "Total errors: " + str(errors) + " errors"

    if errors > 0:
        sys.exit(2)


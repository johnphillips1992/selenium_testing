import os
import time
import sys

from argparse import ArgumentParser

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

errors = 0

PRODUCTION_SITES = [
    "http://myaccount.arch.tamu.edu",
    "http://chc.arch.tamu.edu",
    "http://chsd.arch.tamu.edu",
    "http://chud.arch.tamu.edu",
    "http://colonias.arch.tamu.edu",
    "http://cosc.arch.tamu.edu",
    "http://creativity.arch.tamu.edu",
    "http://crs.arch.tamu.edu",
    "http://dept.arch.tamu.edu",
    "http://hrrc.arch.tamu.edu",
    "http://laup.arch.tamu.edu",
    "http://one.arch.tamu.edu",
    "http://targetcities.arch.tamu.edu",
    "http://viz.arch.tamu.edu",
    "http://www.arch.tamu.edu",
    "http://pypi.arch.tamu.edu",
    "http://symposium.arch.tamu.edu",
    "http://fablab.arch.tamu.edu",
    "http://vizeval.arch.tamu.edu",
    "http://coastalatlas.arch.tamu.edu",
    "http://grandchallenge.tamu.edu"
]

STAGING_SITES = [
    "https://myaccount-dev.arch.tamu.edu",
    "https://chc-dev.arch.tamu.edu",
    "https://chsd-dev.arch.tamu.edu",
    "https://chud-dev.arch.tamu.edu",
    "https://colonias-dev.arch.tamu.edu",
    "https://cosc-dev.arch.tamu.edu",
    "https://creativity-dev.arch.tamu.edu",
    "https://crs-dev.arch.tamu.edu",
    "https://dept-dev.arch.tamu.edu",
    "https://hrrc-dev.arch.tamu.edu",
    "https://laup-dev.arch.tamu.edu",
    "https://one-dev.arch.tamu.edu",
    "https://targetcities-dev.arch.tamu.edu",
    "https://viz-dev.arch.tamu.edu",
    "https://dev.arch.tamu.edu",
    "https://pypi-dev.arch.tamu.edu",
    "https://symposium-dev.arch.tamu.edu",
    "https://fablab-dev.arch.tamu.edu",
    "https://vizeval-dev.arch.tamu.edu",
    "https://coastalatlas-dev.arch.tamu.edu",
    "https://grandchallenge-dev.tamu.edu"
]


def check_tag(instance, driver, tag_name, site):
    global errors
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, tag_name)))
    except Exception as e:
        print "Error: %s failed to display %s tag properly." % (site, tag_name)
        print e
        instance.end()
        sys.exit(2)

def check_class(instance, driver, class_name, site):
    global errors
    try:
        WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    except Exception as e:
        print "Error: %s failed to display %s class properly." % (site,
                class_name)
        print e
        instance.end()
        sys.exit(2)

def check_element(instance, driver, site, width, element, dimension, large,
        small):
    try:
        element_dimension = driver.find_element_by_xpath(element).\
                size.get(dimension)

        if width == 1300 and element_dimension != large:
            print "Error: %s failed. %s has incorrect %s" % (site,
                element, dimension)
            raise

        if width == 800 and element_dimension != small:
            print "Error: %s failed. %s has incorrect %s" % (site,
                element, dimension)
            raise
    except Exception as e:
        print "Error %s failed to check %s" % (site, element)
        print e
        instance.end()
        sys.exit(2)

class Test():
    driver = None

    def __init__(self, driver="chrome"):
        try:
            self.open_browser(driver)
        except:
            pass

    def open_browser(self, driver):
        if self.driver != None:
            self.driver.quit()
        if driver == "chrome":
            chromedriver = "./chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)
        if driver == "ie":
            self.driver = webdriver.Ie()
        if driver == "firefox":
            self.driver = webdriver.Firefox()
        if driver == "safari":
            self.driver = webdriver.SafariDriver()
        if driver == "opera":
            os.environ["SELENIUM_SERVER_JAR"] = "./selenium-server-standalone-2.33.0.jar"
            self.driver = webdriver.Opera()
        print "Driver set to %s" % self.driver

    def test_site(self, site=None):
        global errors
        if site is None:
            site = self.driver.current_url
        print "Testing: %s" % site
        self.driver.get(site)
        try:
            for width in [1300, 800, 300]:
                self.driver.set_window_size(width, 800)
                if "symposium" in site:
                    check_class(self, self.driver, "navbar", site)
                    check_class(self, self.driver, "header", site)
                    check_class(self, self.driver, "site-top-menu", site)
                    check_class(self, self.driver, "footer", site)
                    continue
                if "pypi" in site:
                    self.driver.get(site)
                    check_class(self, self.driver, "container", site)
                    check_tag(self, self.driver, "table", site)
                    continue

                check_element(self, self.driver, site, width, 
                        "//div[@class='navbar navbar-fixed-top']", 'height',
                        42, 52)

                if 'one' in site:
                    check_element(self, self.driver, site, width, 
                            "/html/body/div[@class='container']", 'width',
                            990, 724)
                else:
                    check_element(self, self.driver, site, width, 
                            "/html/body/div[@class='container']", 'width',
                            1000, 724)

                if site == "http://dev.arch.tamu.edu" or \
                    site == "http://www.arch.tamu.edu":
                    check_element(self, self.driver, site, width,
                            "//div[@class='newsitems']", 'width',
                            660, 476)
                    check_element(self, self.driver, site, width,
                            "//div[@class='upcoming-events']", 'width',
                            300, 208)
                    check_element(self, self.driver, site, width, 
                            "//div[@class='banner span12']", 'height',
                            309, 228)
                    check_class(self, self.driver, "newsitems", site)
                    check_class(self, self.driver, "upcoming-events", site)

        except Exception as e:
            print "Error: %s faild." % site
            print e
            pass

    def test_all_sites(self, environment="staging"):
        if(environment == "staging"):
            for site in STAGING_SITES:
                self.test_site(site)
        if(environment == "production"):
            for site in PRODUCTION_SITES:
                self.test_site(site)
    def end(self):
        self.driver.quit()
        self.driver = None

    def quit(self):
        if self.driver:
            self.driver.quit()
        sys.exit()


from getpass import getpass

from test_object import Test



class AccountsTest(Test):
    username = None
    password = None

    def __init__(self):
        self.username = raw_input("Username: ")
        self.password = getpass()

    def test_myaccount(self):
        try:
            self.driver.get("http://myaccount.arch.tamu.edu/accounts/login")
        except Exception as e:
            print "Error: Could not load myaccount login page!"
            print e

        try:
            username_element = self.driver.find_element_by_id("id_username")
            password_element = self.driver.find_element_by_id("id_password")
        except Exception as e:
            print "Error: Could not locate the username and password fields."
            print e
        else:
            username_element.send_keys(self.username)
            password_element.send_keys(self.password)

            password_element.submit()

            if "Login" in self.driver.title:
                print "Warning: Incorrect username or password."
            elif "My Profile" in self.driver.title:
                self.test_site()
            else:
                print "Error: Could not load My Profile page."
                print "Page: %s" % self.driver.title
        return

    def test_admin(self):
        try:
            self.driver.get("http://www.arch.tamu.edu/admin")
        except Exception as e:
            print "Error: Could not load http://www.arch.tamu.edu/admin!"
            print e

        try:
            username_element = self.driver.find_element_by_id("id_username")
            password_element = self.driver.find_element_by_id("id_password")
        except Exception as e:
            print "Error: Could not locate the username and password fields."
        else:
            username_element.send_keys(self.username)
            password_element.send_keys(self.password)

            password_element.submit()

            if "Log in" in self.driver.title:
                print "Warning: Incorrect username or password."
            elif "Site administration" in self.driver.title:
                return
            else:
                print "Error: Could not load the Site Administration page."
        return

    def change_user(self):
        self.username = raw_input("Username: ")
        self.password = getpass()


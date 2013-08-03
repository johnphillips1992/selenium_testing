from getpass import getpass

from test_object import Test



class AccountsTest(Test):
    def test_myaccount(self):
        username = raw_input("Username: ")
        password = getpass()
        test.driver.get("http://myaccount.arch.tamu.edu")
        print username
        print password
        return

    def test_admin(self):
        return

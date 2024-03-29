from selenium import webdriver
import unittest
import time


class EduPortalLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.f = open("username.txt", "r")

    def test_login(self):
        driver = self.driver
        f = self.f

        credential = f.readline()
        user, passw = credential.split(" ")

        driver.get("https://demoen.eduportal.pl/Zaloguj")
        username = driver.find_element_by_id("UserName")
        username.clear()

        username.send_keys(user)

        password = driver.find_element_by_id("Password")
        password.clear()

        password.send_keys(passw)

        driver.find_element_by_id("BtnLogowanie").click()

        # Logout
        time.sleep(10)
        self.assertEqual(driver.title, "tablicaSzkoleniowa",
                            "Failed authentication with username: "+user)
        driver.find_element_by_link_text("Wyloguj").click()

    def tearDown(self):
        self.driver.close()
        self.f.close()


if __name__ == "__main__":
    unittest.main()

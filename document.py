from selenium import webdriver
import unittest
import time
import os
import sys


class EduPortalUpload(unittest.TestCase):
    FILE_NAME_UPLOAD = "file.txt"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.f = open("username.txt", "r")

    def test_upload(self):
        driver = self.driver
        f = self.f

        # Check upload file exist
        if not os.path.exists(os.path.join(os.getcwd(), self.FILE_NAME_UPLOAD)):
            self.fail(self.FILE_NAME_UPLOAD+" file not found")

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
        driver.get("https://demoen.eduportal.pl/Dokument/MojePliki/")
        time.sleep(5)
        driver.find_element_by_id("filePlik").send_keys(
            os.path.join(os.getcwd(), self.FILE_NAME_UPLOAD))
        time.sleep(15)
        driver.find_element_by_link_text(self.FILE_NAME_UPLOAD)

    def tearDown(self):
        self.driver.close()
        self.f.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        EduPortalUpload.FILE_NAME_UPLOAD = sys.argv.pop()

    unittest.main()

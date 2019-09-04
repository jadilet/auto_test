from selenium import webdriver
import time


def Login(email, passw):
    driver = webdriver.Chrome()
    driver.get("https://demoen.eduportal.pl/Zaloguj")

    username = driver.find_element_by_id("UserName")
    username.clear()

    username.send_keys(email)

    password = driver.find_element_by_id("Password")
    password.clear()

    password.send_keys(passw)

    driver.find_element_by_id("BtnLogowanie").click()

    # Logout
    time.sleep(10)
    driver.find_element_by_link_text("Wyloguj").click()

    driver.quit()
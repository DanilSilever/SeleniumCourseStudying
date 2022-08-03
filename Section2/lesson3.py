from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def ex1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/alert_accept.html")

        browser.find_element(By.CSS_SELECTOR, ".btn").click()

        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(1)

        x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        y = calc(x)

        text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
        text_area.send_keys(y)
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    finally:
        time.sleep(7)
        browser.quit()


def ex2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/redirect_accept.html")

        browser.find_element(By.CSS_SELECTOR, ".btn").click()

        browser.switch_to.window(browser.window_handles[1])

        x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        y = calc(x)

        text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
        text_area.send_keys(y)
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    finally:
        time.sleep(7)
        browser.quit()


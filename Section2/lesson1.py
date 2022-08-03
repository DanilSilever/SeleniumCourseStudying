from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def ex1():
    try:
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/math.html")
        time.sleep(1)

        x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        y = calc(x)

        text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
        text_area.send_keys(y)

        browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
        browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    finally:
        time.sleep(5)
        browser.quit()


def ex2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/get_attribute.html")
        time.sleep(1)

        x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
        x = x_element.get_attribute("valuex")
        y = calc(x)

        text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
        text_area.send_keys(y)

        browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
        browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    finally:
        time.sleep(7)
        browser.quit()

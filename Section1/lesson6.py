from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def send_form(browser, button):
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    if not button:
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


def ex1():
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        send_form(browser)

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла


def ex2():
    site_link = "http://suninjuly.github.io/find_link_text"
    try:
        browser = webdriver.Chrome()
        browser.get(site_link)
        link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
        link.click()
        time.sleep(2)
        send_form(browser)

    finally:
        time.sleep(15)
        browser.quit()


def ex3():

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.CSS_SELECTOR, "input")
        for element in elements:
            element.send_keys("kekw")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def ex4():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/find_xpath_form")
        button = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        send_form(browser, button)

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

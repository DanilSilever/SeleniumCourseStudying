from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def ex1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/selects2.html")
        x_sum = sum(
            [int(browser.find_element(By.CSS_SELECTOR, "#num1").text),
             int(browser.find_element(By.CSS_SELECTOR, "#num2").text)]
        )
        select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
        select.select_by_visible_text(str(x_sum))

        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    finally:
        time.sleep(7)
        browser.quit()


def ex2():
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
        browser.get("http://suninjuly.github.io/execute_script.html")
        time.sleep(1)

        x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        y = calc(x)

        text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
        text_area.send_keys(y)

        browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
        button2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
        button3 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
        time.sleep(1)
        button2.click()
        button3.click()

    finally:
        time.sleep(7)
        browser.quit()


def ex3():
    try:
        link = "http://suninjuly.github.io/file_input.html"
        browser = webdriver.Chrome()
        browser.get(link)
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'kekw.txt')

        # Ваш код, который заполняет обязательные поля
        input_first_name = browser.find_element(By.NAME, "firstname")
        input_first_name.send_keys("kekw")

        input_last_name = browser.find_element(By.NAME, "lastname")
        input_last_name.send_keys("kekw")

        email = browser.find_element(By.NAME, "email")
        email.send_keys("kekw")

        input_file = browser.find_element(By.CSS_SELECTOR, "#file")
        input_file.send_keys(file_path)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(7)
        # закрываем браузер после всех манипуляций
        browser.quit()


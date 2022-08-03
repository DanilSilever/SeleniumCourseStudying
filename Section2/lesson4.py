from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def ex1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/explicit_wait2.html")

        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
        btn = browser.find_element(By.ID, "book")
        btn.click()

        x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        y = calc(x)

        text_area = browser.find_element(By.CSS_SELECTOR, "#answer")
        browser.execute_script("return arguments[0].scrollIntoView(true);", text_area)
        text_area.send_keys(y)
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    finally:
        time.sleep(7)
        browser.quit()


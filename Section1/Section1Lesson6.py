from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test(url):
    try:
        link = url
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first")
        input_first_name.send_keys("kekw")

        input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second")
        input_last_name.send_keys("kekw")

        email = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third")
        email.send_keys("kekw")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        print(f"Тест успешно пройдет с url = {link}")

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
test(link1)
test(link2)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    # Переменные
    LOGIN = 'gzpbank@ecredit.one'
    PASSWORD = 'gvymW7'

    # Локаторы
    LOGIN_FORM = (By.CSS_SELECTOR, "input[type='text']")
    PASSWORD_FORM = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")


    def input_login(self, time_sleep = 0):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(LoginPage.LOGIN_FORM))
        element.send_keys(LoginPage.LOGIN)

    def input_password(self, time_sleep = 0):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(LoginPage.PASSWORD_FORM))
        element.send_keys(LoginPage.PASSWORD)

    def press_button_login(self, time_sleep=0):
        element = WebDriverWait(self, time_sleep).until(EC.element_to_be_clickable(LoginPage.LOGIN_BUTTON))
        element.click()
        element.click()





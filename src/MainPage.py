import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    # Локаторы
    CREATE_APPLICATION = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[4]/div[1]/div[2]")
    CREATE_APPLICATION_NAV = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[2]")
    CREATE_APPLICATION_CREDIT = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[1]/a[1]")

    def press_create_new_application(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.CREATE_APPLICATION))
        element.click()

    def move_to_create_new_application(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.element_to_be_clickable(MainPage.CREATE_APPLICATION_NAV))
        element.click()


    def press_create_new_application_button(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.element_to_be_clickable(MainPage.CREATE_APPLICATION_CREDIT))
        element.click()

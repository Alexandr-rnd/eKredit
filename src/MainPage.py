import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    # Локаторы
    CREATE_APPLICATION = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[4]/div[1]/div[1]")
    CREATE_APPLICATION_NAV = (By.XPATH, "//span[text()='Создать']/parent::div")
    CREATE_APPLICATION_CREDIT = (By.XPATH, "//a[text()='Кредит']")
    GET_APPLICATION_LIST = (By.XPATH, "//span[text()='Заявки']/parent::div")
    GET_APPLICATION_LIST_IN_WORK = (By.XPATH, "//a[text()='В работе']")
    INPUT_PLACE = (By.CSS_SELECTOR, "input[placeholder]")
    BUTTON_GO_TO_SEARCH_APPLICATION = (By.CSS_SELECTOR, "button.sc-kYnagK")
    BUTTON_GO_TO_OPEN_APPLICATION = (By.XPATH, "//button[text()='Открыть']")
    VIEW_APPLICATION = (By.XPATH, "//button[text()='Рассмотрение заявки']")
    BUTTON_COUNT_CREDIT = (By.XPATH, "//button[text()='Рассчитать кредит']")
    CLOSE_BUNNER = (By.CSS_SELECTOR, "div.popup__close-button")
    PREPARE_APPLICATION = (By.XPATH, "//a[text()='Подготовить заявку']")

    def press_create_new_application(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.CREATE_APPLICATION))
        element.click()

    def move_to_create_new_application(self, time_sleep=2):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.CREATE_APPLICATION_NAV))
        element.click()

    def press_create_new_application_button(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.CREATE_APPLICATION_CREDIT))
        element.click()

    def press_open_tab_application_list(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.GET_APPLICATION_LIST))
        element.click()

    def press_open_tab_application_list_in_work(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.GET_APPLICATION_LIST_IN_WORK))
        element.click()

    def input_number_of_application(self, time_sleep=1, application_num=None):
        time.sleep(1)
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.INPUT_PLACE))
        element.send_keys(application_num)

    def go_to_search_application(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep)\
            .until(EC.element_to_be_clickable(MainPage.BUTTON_GO_TO_SEARCH_APPLICATION))
        element.click()

    def go_to_open_application(self, time_sleep=1):
        time.sleep(1)
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.BUTTON_GO_TO_OPEN_APPLICATION))
        element.click()

    def button_view_application(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.VIEW_APPLICATION))
        element.click()

    def button_close_bunner(self, time_sleep=1):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        frame1 = WebDriverWait(self, time_sleep, ignored_exceptions=ignored_exceptions).until\
            (EC.element_to_be_clickable((By.CSS_SELECTOR, "iframe#carrot-popup-frame")))
        self.switch_to.frame(frame1)
        element = WebDriverWait(self, time_sleep, ignored_exceptions=ignored_exceptions)\
            .until(EC.element_to_be_clickable(MainPage.CLOSE_BUNNER))
        element.click()
        self.switch_to.default_content()
        time.sleep(1)


    def button_count_credit(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.BUTTON_COUNT_CREDIT))
        element.click()

    def button_prepear_credit(self, time_sleep=1):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self, time_sleep,
                ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located(MainPage.PREPARE_APPLICATION))
        time.sleep(2)
        element = WebDriverWait(self, time_sleep,
                                ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located(MainPage.PREPARE_APPLICATION))

        element.click()
        self.refresh()

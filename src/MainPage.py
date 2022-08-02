import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():

    USER_GPB = (By.XPATH, "//button[text()='Тестирование ГазпромБанк']")

    # Локаторы
    CREATE_APPLICATION = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[4]/div[1]/div[1]")
    CREATE_APPLICATION_NAV = (By.XPATH, "//span[text()='Создать']/parent::div")
    CREATE_APPLICATION_CREDIT = (By.XPATH, "//a[text()='Кредит']")
    GET_APPLICATION_LIST = (By.XPATH, "//span[text()='Заявки']/parent::div")
    GET_APPLICATION_LIST_IN_WORK = (By.XPATH, "//a[text()='В работе']")
    INPUT_PLACE = (By.CSS_SELECTOR, "input[placeholder]")
    BUTTON_GO_TO_SEARCH_APPLICATION = (By.CSS_SELECTOR, "button.sc-dBoRSD")
    BUTTON_GO_TO_OPEN_APPLICATION = (By.XPATH, "//button[text()='Открыть']")
    VIEW_APPLICATION = (By.XPATH, "//button[text()='Рассмотрение заявки']")
    BUTTON_COUNT_CREDIT = (By.XPATH, "//button[text()='Рассчитать кредит']")
    PREPARE_APPLICATION = (By.XPATH, "//a[text()='Подготовить заявку']")
    USER_CONFIG_BUTTON = (By.CSS_SELECTOR, ".nav-button.nav-button--increased-height")
    USER_CONFIG_LABLE = (By.CSS_SELECTOR, ".nav-item--increased-height")
    CLOSE_BUNNER = (By.CSS_SELECTOR, "div.popup__close-button")



    def press_create_new_application(self, time_sleep=1):
        time.sleep(1)
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.CREATE_APPLICATION))
        element.click()


    def move_to_create_new_application(self, time_sleep=2):
        time.sleep(1)
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.CREATE_APPLICATION_NAV))
        element.click()

    def press_create_new_application_button(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.CREATE_APPLICATION_CREDIT))
        time.sleep(1)
        element.click()

    def press_open_tab_application_list(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.GET_APPLICATION_LIST))
        time.sleep(1)
        element.click()

    def press_open_tab_application_list_in_work(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.GET_APPLICATION_LIST_IN_WORK))
        time.sleep(1)
        element.click()

    def input_number_of_application(self, time_sleep=1, application_num=None):
        time.sleep(1)
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.INPUT_PLACE))
        if application_num == "LAST":
            with open("fio.txt", "r")as fio:
                element.send_keys(fio.readline())
        else:
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
        WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.VIEW_APPLICATION))
        time.sleep(2)
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(MainPage.VIEW_APPLICATION))
        element.click()

    def button_close_bunner(self, time_sleep=1):
        try:
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
            WebDriverWait(self, time_sleep, ignored_exceptions=ignored_exceptions).until \
                (EC.element_to_be_clickable((By.CSS_SELECTOR, "iframe#carrot-popup-frame")))
            time.sleep(1)
            frame1 = WebDriverWait(self, time_sleep, ignored_exceptions=ignored_exceptions).until\
                (EC.element_to_be_clickable((By.CSS_SELECTOR, "iframe#carrot-popup-frame")))
            self.switch_to.frame(frame1)
            element = WebDriverWait(self, time_sleep, ignored_exceptions=ignored_exceptions)\
                .until(EC.element_to_be_clickable(MainPage.CLOSE_BUNNER))
            element.click()
            self.switch_to.default_content()
            time.sleep(1)
        except:
            pass

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



    def move_to_config_label(self, time_sleep=2):
        time.sleep(1)
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(MainPage.USER_CONFIG_BUTTON))
        element.click()

    def move_to_config_user(self, time_sleep=2):
        time.sleep(1)
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(MainPage.USER_CONFIG_LABLE))
        element.click()

    def move_to_user_gpb(self, time_sleep=2):
        time.sleep(1)
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(MainPage.USER_GPB))
        element.click()


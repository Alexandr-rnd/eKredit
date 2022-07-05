import time

from faker import Faker
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class CreditScorePage():
    # Переменные
    CAR_MARK = "Hyundai"
    CAR_MODEL = "Creta"
    CAR_COMPLECTATION = "2.0 (149HP) 4WD BI2 (G043/G039) (2021) 21MY 6AT (1 674 000 ₽)"
    CAR_PRISE = "1500000"
    KASKO_PRODUCT = "105"
    SAFE_LIFE = "2849"
    KASKO_PRICE_SUM = "30000"
    ADDITIONAL_EQUPMENT = "10000"


    # Локаторы
    CAR_MARK_SELECT = (By.CSS_SELECTOR, "select#car_brand_id")
    CAR_MODEL_SELECT = (By.CSS_SELECTOR, "select#car_model_id")
    CAR_COMPLECTION_SELECT = (By.CSS_SELECTOR, "#car_id")
    KASKO_SELECT = (By.CSS_SELECTOR, "#kasko_name_val")
    SAFE_LIFE_SELECT = (By.CSS_SELECTOR, "#life_price_val")
    KASKO_PRICE = (By.CSS_SELECTOR, "#kasko_price_val")
    BUTTON_GET_COUNT = (By.CSS_SELECTOR, "#btn_calculation_get")
    SELECT_SMOEONE_OFFER = (By.XPATH, "/html/body/div[3]/div[2]/div[8]/div/div[2]/div[2]/div/div[1]/div[5]/div[9]/div[2]/table/tbody[2]/tr[1]/td[5]")
    SELECT_SAFE_EQUALS = (By.CSS_SELECTOR, "#btn_calculation_save")
    SELECT_NAME_PLACE = (By.CSS_SELECTOR, "#saveCalculationForm input[name = 'client_name']")
    SELECT_SURENAME_PLACE = (By.CSS_SELECTOR,"input[name='client_surname']")
    SELECT_TEL_NUM_PLACE = (By.CSS_SELECTOR,"#client_phone")
    CLICK_SAFE_EQUALS = (By.CSS_SELECTOR, "#saveCalculationForm button")
    CLOSE_NEW_APPLICATION_BUTTON = (By.CSS_SELECTOR, "#alert-btn-ok")
    VECHICAL_PRISE = (By.CSS_SELECTOR, "#price_before")
    BUTTON_NOTIF_CLOSE = (By.CSS_SELECTOR,"button#notification-close")
    PRICE_ADDITIONAL_EQUPMENT = ((By.CSS_SELECTOR, "input#price_after"))



    def make_random(self):
        f = Faker('ru_RU')
        if self =="name":
            return f.first_name()
        elif self == "surename":
            return f.last_name()
        elif self == "number":
            return f.phone_number()
        else:
            return "make_random такого не знает"


    def select_mark_car(self, time_sleep=1):
        WebDriverWait(self, time_sleep).until(EC.element_to_be_clickable(CreditScorePage.CAR_MARK_SELECT))
        time.sleep(3)
        select_limit = Select(self.find_element(*CreditScorePage.CAR_MARK_SELECT))
        select_limit.select_by_visible_text(CreditScorePage.CAR_MARK)

    def select_model_car(self):
        select_limit = Select(self.find_element(*CreditScorePage.CAR_MODEL_SELECT))
        select_limit.select_by_visible_text(CreditScorePage.CAR_MODEL)

    def select_complection_car(self):
        select_limit = Select(self.find_element(*CreditScorePage.CAR_COMPLECTION_SELECT))
        select_limit.select_by_visible_text(CreditScorePage.CAR_COMPLECTATION)

    def select_kasko_car(self):
        target = self.find_element(*CreditScorePage.KASKO_SELECT)
        target.location_once_scrolled_into_view
        select_limit = Select(self.find_element(*CreditScorePage.KASKO_SELECT))
        select_limit.select_by_value(CreditScorePage.KASKO_PRODUCT)

    def input_kasko_prise(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.KASKO_PRICE))
        element.click()
        element.send_keys(Keys.BACK_SPACE, "20000")

    def select_safe_life_programm_car(self):
        target = self.find_element(*CreditScorePage.SAFE_LIFE_SELECT)
        target.location_once_scrolled_into_view
        select_limit = Select(self.find_element(*CreditScorePage.SAFE_LIFE_SELECT))
        select_limit.select_by_value(CreditScorePage.SAFE_LIFE)


    def press_get_count_button(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.BUTTON_GET_COUNT))
        element.click()

    def press_choose_someone_offer(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.SELECT_SMOEONE_OFFER))
        element.click()

    def press_save_equals(self, time_sleep=1):
        target = self.find_element(*CreditScorePage.SELECT_SAFE_EQUALS)
        target.location_once_scrolled_into_view
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.SELECT_SAFE_EQUALS))
        element.click()


    def input_name_client(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.SELECT_NAME_PLACE))
        element.click()
        element.send_keys(Keys.BACK_SPACE, CreditScorePage.make_random("name"))

    def input_surename_client(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.SELECT_SURENAME_PLACE))
        element.click()
        element.send_keys(Keys.BACK_SPACE, CreditScorePage.make_random("surename"))

    def input_telephone_number_client(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.SELECT_TEL_NUM_PLACE))
        element.click()
        element.send_keys(Keys.BACK_SPACE, "89281665121")

    def press_save_equals_client_information(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.CLICK_SAFE_EQUALS))
        element.click()

    def click_new_application_confirm(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(CreditScorePage.CLOSE_NEW_APPLICATION_BUTTON))
        element.click()

    def input_vehical_prise(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(CreditScorePage.VECHICAL_PRISE))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE, CreditScorePage.CAR_PRISE)


    def button_close_notif(self, time_sleep=1):
        try:
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
            WebDriverWait(self, time_sleep, ignored_exceptions=ignored_exceptions).until \
                (EC.element_to_be_clickable((By.CSS_SELECTOR, "iframe#carrot-messenger-frame")))
            time.sleep(1)
            frame1 = WebDriverWait(self, time_sleep, ignored_exceptions=ignored_exceptions).until \
                (EC.element_to_be_clickable((By.CSS_SELECTOR, "iframe#carrot-messenger-frame")))
            self.switch_to.frame(frame1)
            element = WebDriverWait(self, time_sleep, ignored_exceptions=ignored_exceptions) \
                .until(EC.element_to_be_clickable(CreditScorePage.BUTTON_NOTIF_CLOSE))
            element.click()
            self.switch_to.default_content()
            time.sleep(1)
        except:
            pass

    def input_additional_equpment_price(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(CreditScorePage.PRICE_ADDITIONAL_EQUPMENT))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE, CreditScorePage.ADDITIONAL_EQUPMENT)
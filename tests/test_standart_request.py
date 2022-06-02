import time

from src.CreditScorePage import CreditScorePage
from src.LoginPage import LoginPage
from src.MainPage import MainPage


def test_first(driver, base_url):
    driver.get(base_url)
    LoginPage.input_login(driver, 2)
    LoginPage.input_password(driver)
    LoginPage.press_button_login(driver)
    MainPage.press_create_new_application(driver, 5)
    MainPage.move_to_create_new_application(driver, 1)
    time.sleep(2)
    MainPage.press_create_new_application_button(driver)
    CreditScorePage.select_mark_car(driver, 10)
    CreditScorePage.select_model_car(driver)
    CreditScorePage.select_complection_car(driver)
    CreditScorePage.select_kasko_car(driver)
    CreditScorePage.select_safe_life_programm_car(driver)
    CreditScorePage.input_kasko_prise(driver)
    CreditScorePage.press_get_count_button(driver)
    CreditScorePage.press_choose_someone_offer(driver)
    CreditScorePage.press_save_equals(driver)
    CreditScorePage.input_name_client(driver)
    CreditScorePage.input_surename_client(driver)
    CreditScorePage.input_telephone_number_client(driver)
    CreditScorePage.press_save_equals_client_information(driver)
    CreditScorePage.click_new_application_confirm(driver)
    time.sleep(9000)


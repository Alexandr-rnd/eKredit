import time

from src.CreditScorePage import CreditScorePage
from src.LoginPage import LoginPage
from src.MainPage import MainPage
from src.PrepearPage import PrepearPage


def test_create_simple_application(driver, base_url): # заполнение первой страницы
    driver.get(base_url)
    LoginPage.input_login(driver, 2)
    LoginPage.input_password(driver)
    LoginPage.press_button_login(driver)
    MainPage.button_close_bunner(driver, 30)
    MainPage.press_create_new_application(driver, 5)
    MainPage.move_to_create_new_application(driver)
    MainPage.press_create_new_application_button(driver)
    CreditScorePage.select_mark_car(driver, 7)
    CreditScorePage.select_model_car(driver)
    CreditScorePage.select_complection_car(driver)
    CreditScorePage.select_kasko_car(driver)
  #  CreditScorePage.select_safe_life_programm_car(driver)
    CreditScorePage.input_kasko_prise(driver)
    CreditScorePage.press_get_count_button(driver)
    CreditScorePage.press_choose_someone_offer(driver)
    CreditScorePage.press_save_equals(driver)
    CreditScorePage.input_name_client(driver)
    CreditScorePage.input_surename_client(driver)
    CreditScorePage.input_telephone_number_client(driver)
    CreditScorePage.press_save_equals_client_information(driver)
    CreditScorePage.click_new_application_confirm(driver, 5)
    time.sleep(9000)

NUMBER_OF_APPLICATION = 2987
def test_open_application(driver, base_url): # поиск заявки  по "NUMBER_OF_APPLICATION" и 2 страница
    driver.get(base_url)
    LoginPage.input_login(driver, 2)
    LoginPage.input_password(driver)
    LoginPage.press_button_login(driver)
    MainPage.move_to_config_label(driver, 10)
    MainPage.move_to_config_user(driver, 10)
    MainPage.move_to_user_gpb(driver, 10)
    MainPage.button_close_bunner(driver, 30)
    MainPage.press_create_new_application(driver, 5)
    MainPage.move_to_create_new_application(driver)
    MainPage.press_create_new_application_button(driver)
    PrepearPage.input_passport(driver, 60)
    PrepearPage.input_driver_licence(driver, 10)
    PrepearPage.close_found_personal_data(driver, 120)
    PrepearPage.input_clients_fio(driver, 10)
    PrepearPage.click_show_all_atributes_passport(driver, 10)
    PrepearPage.issure_date(driver, 5)
    PrepearPage.issure_code(driver, 10)
    PrepearPage.choose_family_status(driver, 5)
    PrepearPage.select_count_children(driver, 5)
    PrepearPage.series_number(driver, 5)
    PrepearPage.birth_place(driver, 5)
    PrepearPage.birth_date(driver, 5)
    PrepearPage.select_drive_licence(driver, 5)
    PrepearPage.select_data_drive_licence(driver, 5)
    PrepearPage.select_registration_adress(driver, 5)
            # метод для индекса PrepearPage.select_registration_index(driver, 5)
    PrepearPage.select_registration_date(driver, 5)
    PrepearPage.select_experience_work(driver, 5)
    PrepearPage.select_organization_name(driver, 5)
    PrepearPage.choose_work_type(driver, 5)
    PrepearPage.choose_work_experience_age(driver, 5)
    PrepearPage.averge_income(driver, 5)
    PrepearPage.averge_extra_income(driver, 5)
    PrepearPage.select_organization_phone(driver, 5)
    PrepearPage.select_post_name(driver, 5)
    PrepearPage.input_trust_person_fio(driver, 5)
    PrepearPage.select_trust_person_phone_number(driver, 5)
    PrepearPage.input_consedence(driver, 5)
    PrepearPage.press_save_button(driver, 5)
    time.sleep(6000)

NUMBER_OF_APPLICATION = "LAST"
def test_open_vehicle_page(driver, base_url):
    driver.get(base_url)
    LoginPage.input_login(driver, 2)
    LoginPage.input_password(driver, 2)
    LoginPage.press_button_login(driver, 10)
    MainPage.press_create_new_application(driver, 10)
    MainPage.press_open_tab_application_list(driver, 20)
    MainPage.press_open_tab_application_list_in_work(driver)
    MainPage.input_number_of_application(driver, application_num=NUMBER_OF_APPLICATION)
    MainPage.go_to_search_application(driver, 50)
    MainPage.go_to_open_application(driver, 20)
    MainPage.button_view_application(driver, 20)
    time.sleep(600)


def test_create_simple_application1(driver, base_url): # Заведение и отправка заявки
    driver.get(base_url)
    LoginPage.input_login(driver, 2)
    LoginPage.input_password(driver)
    LoginPage.press_button_login(driver)
    #MainPage.move_to_config_label(driver, 10)       #MainPage.move_to_config_user(driver, 10)       #MainPage.move_to_user_gpb(driver, 10)          #MainPage.button_close_bunner(driver, 10)
    MainPage.press_create_new_application(driver, 5)
    MainPage.move_to_create_new_application(driver)
    MainPage.press_create_new_application_button(driver)
    CreditScorePage.select_mark_car(driver, 7)
    CreditScorePage.select_model_car(driver)
    CreditScorePage.select_complection_car(driver)
    CreditScorePage.input_additional_equpment_price(driver)
    CreditScorePage.input_vehical_prise(driver)
    CreditScorePage.select_kasko_car(driver)#  CreditScorePage.select_safe_life_programm_car(driver)
    CreditScorePage.input_kasko_prise(driver)
    CreditScorePage.press_get_count_button(driver)
    CreditScorePage.press_choose_someone_offer(driver, 10)
    CreditScorePage.press_save_equals(driver)
    CreditScorePage.input_name_client(driver)
    CreditScorePage.input_surename_client(driver)
    CreditScorePage.input_telephone_number_client(driver)
    CreditScorePage.press_save_equals_client_information(driver)
    #CreditScorePage.button_close_notif(driver, 10)
    CreditScorePage.click_new_application_confirm(driver, 5)
    PrepearPage.input_passport(driver, 60)
    PrepearPage.input_driver_licence(driver, 10)
    PrepearPage.close_found_personal_data(driver, 120)
    PrepearPage.input_clients_fio(driver, 10)
    #PrepearPage.click_show_all_atributes_passport(driver, 10)
    PrepearPage.issure_date(driver, 5)
    PrepearPage.issure_code(driver, 10)
    PrepearPage.choose_family_status(driver, 5)
    PrepearPage.select_count_children(driver, 5)
    PrepearPage.series_number(driver, 5)
    PrepearPage.birth_place(driver, 5)
    PrepearPage.birth_date(driver, 5)
    PrepearPage.select_drive_licence(driver, 5)
    PrepearPage.select_data_drive_licence(driver, 5)
    PrepearPage.select_registration_adress(driver, 5) # метод для индекса PrepearPage.select_registration_index(driver, 5)
    PrepearPage.select_registration_date(driver, 5)
    PrepearPage.select_experience_work(driver, 5)
    PrepearPage.select_organization_name(driver, 5)
    PrepearPage.choose_work_type(driver, 5)
    PrepearPage.choose_work_experience_age(driver, 5)
    PrepearPage.averge_income(driver, 5)
    PrepearPage.averge_extra_income(driver, 5)
    PrepearPage.select_organization_phone(driver, 5)
    PrepearPage.select_post_name(driver, 5)
    PrepearPage.input_trust_person_fio(driver, 5)
    PrepearPage.select_trust_person_phone_number(driver, 5)
    PrepearPage.input_consedence(driver, 5)
    #PrepearPage.press_save_button(driver, 5)
    PrepearPage.press_send_to_process_button(driver, 60)
    PrepearPage.press_select_gazprom(driver, 30)
    PrepearPage.press_select_offer_gazprom(driver)
    PrepearPage.press_send_offer_to_gazprom(driver)
    time.sleep(6000)
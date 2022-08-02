import random
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.CreditScorePage import CreditScorePage
from selenium.webdriver.common.action_chains import ActionChains


class PrepearPage():
    PASSPORT =  "C:\Dev\eKredit\docks\passport.pdf"
    DRIVER_LICENCE = "C:\Dev\eKredit\docks\drivers.pdf"
    CONCEDENCE =  "C:\Dev\eKredit\docks\Consedence.pdf"
    NUMBER_SERIES = "6014"
    FAMILY_STATUS_NO_MARRIED = (By.XPATH, "//p[text()='Холост / Не замужем']")
    CHILDREN = "0"
    ISSUER_DATE_VALUE = "01022015"
    ISSUER_NUMBER_VALUE = "770-001"
    ISSUER_PASSPORT_VALUE = "ГУ МВД РОССИИ ПО Г. МОСКВЕ"
    BIRTH_DATE_VALUE = "01121980"
    BIRTH_PLASE_VALUE = "ОДОБРЕНИЕ"
    DRIVER_LICENCE_NUM = "1565 213516"
    DRIVER_LICENCE_DATE = "11.01.2017"
    WORKER = (By.XPATH, "//li/p[text()='Наемный работник']")
    ADRESS_REGISTRATION = "г Москва, ул Малая Полянка, д 4/6, кв 2"
    INDEX_REGISTRATION = "119180"
    REGISTRATION_DATE = "03102014"
    TRUST_PERSONE_PHONE_NUMBER = "9501234567"
    ORGANISATION_NAME = "1К.БУХГАЛТЕРИЯ"
    PHONE_ORGANIZATION = "9505165156"
    POST_NAME = "Ведущий Специалист"
    EXPERIENCE_WORK_DATE = "01012015"
    EXPERIENCE_AGE = (By.XPATH, "//p[text()='более 10 лет']")
    INCOME_SUMM = ("300000")
    FIRS_POST = (By.CSS_SELECTOR, "div.sc-gHfsNP> :first-child")

    INPUT_PASSPORT = (By.CSS_SELECTOR, "#personalInfo input.sc-hxqEdz")
    COMPLETE_INPUT_BANNER = (By.XPATH, "//button[text()='Ок']")
    INPUT_FIO = (By.CSS_SELECTOR, "div#personalInfo_fullName input")
    FAMILY_STATUS = (By.CSS_SELECTOR, "div#personalInfo_familyState_sysName")
    CHILDREN_COUNT = (By.CSS_SELECTOR, "#personalInfo_childrenCount input")
    LINK_SHOW = (By.XPATH, "//span[text()='Показать']")
    ISSUER_DATE = (By.CSS_SELECTOR, "#passport_issueDate input")
    ISSUER_CODE = (By.CSS_SELECTOR, "#passport_issuerCode input")
    ISSUER_PASSPORT = (By.CSS_SELECTOR, "#passport_issuer input")
    BIRTH_PLACE = (By.CSS_SELECTOR, "#passport_birthPlace input")
    BIRTH_DATE = (By.CSS_SELECTOR, "#personalInfo_birthDate input")
    SERIAS_NUMBER = (By.CSS_SELECTOR, "#passport_serianumber input")
    SELECT_ISSURE_PLASE = (By.XPATH, "//span[text()='ГУ МВД РОССИИ ПО Г. МОСКВЕ']")
    SELECT_DRIVE_LICENSE = (By.CSS_SELECTOR, "#SecDocInput input")
    SELECT_DATA_DRIVE_LICENSE = (By.CSS_SELECTOR, "#secondDocument_driverLicense_issueDate input")
    SELECT_REGESTRATION_ADRESS = (By.CSS_SELECTOR, "#addressReg_fiasValue input")
    SELECT_REGESTRATION_DATE = (By.CSS_SELECTOR, "#addressReg_regDate input")
    SELECT_REGESTRATION_INDEX = (By.CSS_SELECTOR, "#addressReg_index input")
    SELECT_TRUSTED_PERSON = (By.CSS_SELECTOR, "input[label='Фамилия, имя, отчество']")
    SELECT_PHONE_NUMBER_TRUSTED_PERSON = (By.CSS_SELECTOR, ".jhgOMY input[label = 'Мобильный телефон']")
    SELECT_TYPE_OF_WORK = (By.CSS_SELECTOR, "#work_employmentType_sysName")
    SELECT_DRIVE_INDEX = (By.CSS_SELECTOR, "#addressReg_index input")
    SELECT_ORGANIZATION_NAME = (By.CSS_SELECTOR, "#work_organization_name input")
    SELECT_ORGANIZATION_PHONE = (By.CSS_SELECTOR, "#work_organizationPhone input")
    SELECT_POST_NAME = (By.CSS_SELECTOR, "div.sc-jvfqPk")
    EXPERIENCE_WORK = (By.CSS_SELECTOR, "#work_careerStartTime input")
    AGE_EXPERIENCE_WORK = (By.CSS_SELECTOR, "#work_experienceTime>div.sc-hHfuMS")
    SELECT_AVERGE_INCOME = (By.CSS_SELECTOR, "#profit_mainprofit input")
    SELECT_EXTRA_AVERGE_INCOME = (By.CSS_SELECTOR, "#profit_addedprofit input")
    INPUT_CONSEDENCE = (By.CSS_SELECTOR, "#sign input.jsiCud")
    OK_FIND_PERSONAL_DATA = (By.XPATH, "//button[text()='Ок']")
    BUTTON_SAVE = (By.XPATH, "//button[text()='Сохранить']")
    BUTTON_SEND_TO_PROCESS = (By.XPATH, "//button[text()='Отправить заявку в банки']")
    BUTTON_SELECT_GAZPROM = (By.XPATH, "//span[text()='Газпромбанк']")
    BUTTON_SELECT_OFFER_GAZPROM = (By.XPATH, "/html/body/div[3]/div[2]/div[8]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table[2]/tbody/tr[8]/td[6]/label/span")
    BUTTON_SEND_OFFER_TO_RKK = (By.XPATH, "//td/div/div/a[text()='Отправить заявку']")

    def input_passport(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep) \
            .until(EC.presence_of_element_located(PrepearPage.INPUT_PASSPORT))
        element.send_keys(PrepearPage.PASSPORT)

    def input_driver_licence(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(PrepearPage.INPUT_PASSPORT))
        element.send_keys(PrepearPage.DRIVER_LICENCE)

    def close_found_personal_data(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.OK_FIND_PERSONAL_DATA))
        time.sleep(2)
        element.click()

    def input_clients_fio(self, time_sleep=1):
        with open ("fio.txt", "w") as fio:
            element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(PrepearPage.INPUT_FIO))
            element.click()
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.BACK_SPACE)
            surename = CreditScorePage.make_random("surename")
            name = CreditScorePage.make_random("name")
            lastname =  CreditScorePage.make_random("surename")
            fio.write(surename)
            element.send_keys(surename + " " + name + " " + lastname, Keys.ENTER)
            time.sleep(1)
            element.send_keys(Keys.ENTER)

    def click_show_all_atributes_passport(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(PrepearPage.LINK_SHOW))
        element.click()

    def choose_family_status(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.visibility_of_element_located(PrepearPage.FAMILY_STATUS))
        element.click()
        time.sleep(1)
        element2 = WebDriverWait(self, time_sleep).until(
            EC.element_to_be_clickable(PrepearPage.FAMILY_STATUS_NO_MARRIED))
        element2.click()

    def select_count_children(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.
                                                        visibility_of_element_located(PrepearPage.CHILDREN_COUNT))
        element.click()
        element.send_keys("0")

    def issure_code(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.
                                                        visibility_of_element_located(PrepearPage.ISSUER_CODE))
        element.send_keys(PrepearPage.ISSUER_NUMBER_VALUE)

    # def issure_passport(self, time_sleep=1):
    #     element = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(PrepearPage.ISSUER_PASSPORT))
    #     element.send_keys(PrepearPage.ISSUER_PASSPORT_VALUE)
    #     element2 = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(PrepearPage.SELECT_ISSURE_PLASE))
    #     element2.click()

    def birth_place(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(PrepearPage.BIRTH_PLACE))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(PrepearPage.BIRTH_PLASE_VALUE)

    def birth_date(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(PrepearPage.BIRTH_DATE))
        element.click()
        element.send_keys(PrepearPage.BIRTH_DATE_VALUE)

    def issure_date(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(PrepearPage.ISSUER_DATE))
        element.click()
        element.send_keys(PrepearPage.ISSUER_DATE_VALUE)

    def series_number(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(PrepearPage.SERIAS_NUMBER))
        element.click()
        element.clear()
        element.send_keys(Keys.BACK_SPACE, PrepearPage.NUMBER_SERIES +str(random.randint(100000, 999999)), Keys.ENTER)

    def select_drive_licence(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.SELECT_DRIVE_LICENSE))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.DRIVER_LICENCE_NUM)

    def select_data_drive_licence(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.SELECT_DATA_DRIVE_LICENSE))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(PrepearPage.DRIVER_LICENCE_DATE)

    #def select_data_drive_licence(self, time_sleep=1):
     #   element = WebDriverWait(self, time_sleep).until(
      #      EC.visibility_of_element_located(PrepearPage.SELECT_DATA_DRIVE_LICENSE))
       # actionchains = ActionChains(self)
        #actionchains.move_to_element(element).click(element).send_keys(PrepearPage.SELECT_DATA_DRIVE_LICENSE).perform()


    def select_registration_adress(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.SELECT_REGESTRATION_ADRESS))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.ADRESS_REGISTRATION)
        time.sleep(1)
        element.click()
        element.send_keys(Keys.ENTER)

    def select_registration_date(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.presence_of_element_located(PrepearPage.SELECT_REGESTRATION_DATE))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.REGISTRATION_DATE)

    def select_registration_index(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.SELECT_REGESTRATION_INDEX))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.INDEX_REGISTRATION)

    def input_trust_person_fio(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.
                                                        presence_of_element_located(PrepearPage.SELECT_TRUSTED_PERSON))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys("Тест Тест Тест", Keys.ENTER)
        time.sleep(1)
        element.click()
        time.sleep(1)
        element.send_keys(Keys.BACK_SPACE)

    def select_trust_person_phone_number(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.presence_of_element_located(PrepearPage.SELECT_PHONE_NUMBER_TRUSTED_PERSON))
        element.click()
        actions = ActionChains(self)
        actions.send_keys(PrepearPage.TRUST_PERSONE_PHONE_NUMBER)
        actions.perform()
        time.sleep(1)
        element.click()
        # element.send_keys(Keys.BACK_SPACE, PrepearPage.TRUST_PERSONE_PHONE_NUMBER)

    def choose_work_type(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.SELECT_TYPE_OF_WORK))
        element.click()
        time.sleep(1)
        element2 = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.WORKER))
        element2.click()
        time.sleep(1)

    def select_organization_name(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.presence_of_element_located(PrepearPage.SELECT_ORGANIZATION_NAME))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.ORGANISATION_NAME)
        time.sleep(2)
        element.click()
        element.send_keys(Keys.ENTER)

    def select_organization_phone(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.presence_of_element_located(PrepearPage.SELECT_ORGANIZATION_PHONE))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.PHONE_ORGANIZATION)

    def select_post_name(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.SELECT_POST_NAME))
        element.click()
        actions = ActionChains(self)
        actions.send_keys(PrepearPage.POST_NAME)
        actions.perform()
        element2 = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.FIRS_POST))
        element2.click()

    def select_experience_work(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.presence_of_element_located(PrepearPage.EXPERIENCE_WORK))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.EXPERIENCE_WORK_DATE)

    def choose_work_experience_age(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.presence_of_element_located(PrepearPage.AGE_EXPERIENCE_WORK))
        element.click()
        time.sleep(1)
        element.click()
        element2 = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.EXPERIENCE_AGE))
        element2.click()

    def averge_income(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.presence_of_element_located(PrepearPage.SELECT_AVERGE_INCOME))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.INCOME_SUMM)

    def averge_extra_income(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.presence_of_element_located(PrepearPage.SELECT_EXTRA_AVERGE_INCOME))
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(Keys.BACK_SPACE, PrepearPage.INCOME_SUMM)

    def input_consedence(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(EC.presence_of_element_located(PrepearPage.INPUT_CONSEDENCE))
        element.send_keys(PrepearPage.CONCEDENCE)

    def press_save_button(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.element_to_be_clickable(PrepearPage.FAMILY_STATUS_NO_MARRIED))
        element.click()

    def press_send_to_process_button(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.element_to_be_clickable(PrepearPage.BUTTON_SEND_TO_PROCESS))
        element.click()

    def press_select_gazprom(self, time_sleep=1):
        WebDriverWait(self, time_sleep).until(
            EC.element_to_be_clickable(PrepearPage.BUTTON_SELECT_GAZPROM))
        time.sleep(10)
        element = WebDriverWait(self, time_sleep).until(
            EC.visibility_of_element_located(PrepearPage.BUTTON_SELECT_GAZPROM))
        element.click()

    def press_select_offer_gazprom(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.element_to_be_clickable(PrepearPage.BUTTON_SELECT_OFFER_GAZPROM))
        element.click()

    def press_send_offer_to_gazprom(self, time_sleep=1):
        element = WebDriverWait(self, time_sleep).until(
            EC.element_to_be_clickable(PrepearPage.BUTTON_SEND_OFFER_TO_RKK))
        element.click()
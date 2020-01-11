test_wizzair_simple_log.py



#ctrl z kursorem - inpesct klase czy cos tam
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#biblioteka Keys to sa po prostu klawisze np. Enter (return), itp
import sys
import logging

# Dane testowe - ("lamerski" hardcode)
valid_name = "Dick"
valid_surname = "Laurent"
gender = 'female'
country_code = '+48'
valid_telephone = '123432456'
invalid_email = "xcvsdfvhsdfjh.wp.pl"
valid_password = "Qwer46@213"
valid_country = "Afganistan"

class WizzairRegistration(unittest.TestCase):
    """
    Scenariusz testowy: Rejestracja nowego użytkownika na stronie wizzair.com
    """
    def setUp(self):
        """
        Warunki wstępne:
        Przeglądarka otwarta na https://wizzair.com/pl-pl/main-page#/
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")
        self.driver.implicitly_wait(10)
        self.log = logging.getLogger("Registration Test")
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)

    def tearDown(self):
        """ Sprzątanie po teście """
        # Jeśli błąd, to zrób zrzut ekranu
        if sys.exc_info()[0]:
            self.driver.save_screenshot("error.png")
        self.driver.quit()


    def test_invalid_email(self):
        """
        Rejestracja nowego użytkownika
        używając adresu email - dane niepoprawne
        (niekompletny email brak '@')
        """
        self.log.info("Rozpoczynam test")
        driver = self.driver
        # KROKI:
        # ======================
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        # Czekam maks. 5 sekund, aż będzie można kliknąć przycisk ZALOGUJ
        self.log.info("Klikam ZALOGUJ")
        zaloguj_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[data-test=navigation-menu-signin]")))
        zaloguj_btn.click()
        # ======================
        # 2. Kliknij REJESTRACJA
        self.log.info("Klikam REJESTRACJA")
        rejestracja_btn = driver.find_element_by_xpath('//button[text()=" Rejestracja "]')
        rejestracja_btn.click()
        # ======================
        # 3. Wprowadź imię
        self.log.info(f"Wprowadzam imie: {valid_name}")
        imie_field = driver.find_element_by_name("firstName")
        imie_field.send_keys(valid_name)
        # ======================
        # 4. Wprowadź nazwisko
        self.log.info(f"Wprowadzam nazwiwsko: {valid_surname}")
        nazwisko_field = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        nazwisko_field.send_keys(valid_surname)
        # 5.Wybierz płeć
        # ======================
        self.log.info(f"Wybieram płeć: {gender}")
        if gender == 'male':
            # Wybierz MĘŻCZYZNA
            m = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            imie_field.click()
            #driver.execute_script("arguments[0].click();",m)
            m.click()
        else:
            # WYBIERZ KOBIETA
            f = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            f.click()
        # ======================
	    # 6.a Wpipsz kod kraju
        self.log.info(f"Wpisuję kod kraju: {country_code}")
        cc = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        #driver.execute_script("arguments[0].click();", cc)
        ActionChains(driver).move_to_element(cc).click().perform()
        cc2 = driver.find_element_by_xpath('//input[@name="phone-number-country-code"]')
        cc2.send_keys(country_code)
        # 6.b. Wpisz nr telefonu
        self.log.info(f"Wpisuję nr telefonu: {valid_telephone}")
        telephone_field = driver.find_element_by_name('phoneNumberValidDigits')
        telephone_field.send_keys(valid_telephone)
        # ======================
        # 7. Wpisz niepoprawny e-mail (brak '@')
        self.log.info(f"Wpisuję e-mail bez znaku '@': {invalid_email}")
        email_field = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_field.send_keys(invalid_email)
        # ======================
        # 8. Wpisz hasło
        self.log.info(f"Wpisuję haslo")
        password_field = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        password_field.send_keys(valid_password)
        # ======================
        # 9. Wybierz narodowość
        country_field = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        # Wyszukaj kraje
        self.log.info(f"Wybieram z listy kraj: {valid_country}")
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        countries = country_to_choose.find_elements_by_xpath("label")
        # find elementS by xpath - szuka calej listy i zapmietuje a nie pojedynczego elementu
        for label in countries:
            option=label.find_element_by_tag_name('strong')
            # print(d.text)
            if option.get_attribute("innerText") == valid_country:
                option.location_once_scrolled_into_view
                option.click()
                break
        # ======================
        # 10. Zaznacz "Akceptuję Informację o polityce prywatności"
        self.log.info(f"Akceptuję politykę prywatności")
        privacy_policy_checkbox = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
        (By.XPATH, '//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')))
        privacy_policy_checkbox.click()
        # ======================
        # 11. Kliknij ZAREJESTRUJ
        register_btn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        register_btn.click()

        """TEST: SPRAWDZAMY OCZEKIWANY REZULTAT"""

        # Wyszukuję wszystkie błędy
        self.log.info("Sprawdzam poprawność informacji dla uzytkownika")
        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        visible_error_notices = []
        # Zapisuję widoczne błędy do listy visible_error_notices
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy widoczny jest tylko jeden błąd
        assert len(visible_error_notices) == 1
        # Sprawdzam treść widocznego błędu
        error_text = visible_error_notices[0].get_attribute("innerText")
        self.log.info(f"Akceptuję politykę prywatności")
        self.log.info(f"Błąd glosi: {error_text}")
        self.assertEqual(error_text,"Nieprawidłowy adres e-mail")

if __name__ == '__main__':
    unittest.main(verbosity=2)
    #verbosity = 2 wypisuje nam wiecej informacj o testach, verbosity = 0 wypisze mnie; tyle siem dowiedzialam...

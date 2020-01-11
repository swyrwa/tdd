from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


# Scenariusz rejestracja

imie = "Jozef"
zleImie = "Józef"
nazwisko = "Deser"
kodKraju = "Albania"
mobilePhoneNumber = "500000000"
email = "jozef.deser@gmail.com"
haslo = "ILoveDeser123!"
hasloZaKrotkie = "Des1!"
hasloBezCyfr = "Deserr!"
narodowosc = "Albania"

class Rejestracja(unittest.TestCase):

    # Setup
    def setUp(self):
        # 1.Go to https: // wizzair.com / pl - pl  # /
        self.driver = webdriver.Chrome()
        self.driver.get('https://wizzair.com/pl-pl/#/')
        self.driver.maximize_window()

        # 2. Click on ZALOGUJ SIĘ tab
        zalogujSieButton = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='navigation-menu-signin']")))
        print("znalazelm")
        zalogujSieButton.click()

        # 3. Click on the REJESTRACJA link
        #self.driver.switch_to.alert()
        RejestrujSięButton = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), " Rejestracja")]')))
        RejestrujSięButton.click()
        

    def testImieZDiakrytycznym(self):
        # jesli cialo testu nie zaczyna sie od slowa 'test' to sie nic nie odpali bo nie traktuje tej metody jako test
        imie =


#
# R
# #2 Zostawienie pustego pola numeru telefonu
# 1. In the Imię text field type Jozef
# 2. In the Nazwisko text field type Deser
# 3. Choose Mężczyzna
# 4. In the Kod kraju dropdown field choose Albania
# 5. Leave the Mobile Phone number text field empty
# 6. In the E-mail text field type jozefdeser@gmail.com
# 7. In the Hasło text field type ILoveDeser123!
# 8. In the Narodowość (Obywatelstwo) text field type Albania
# 9. Check the Akceptuję checkbox
# 10. Click ZAREJESTRUJ SIĘ button
#
#
# #3 Niepoprawne hasło - za krótkie
# 1. In the Imię text field type Jozef
# 2. In the Nazwisko text field type Deser
# 3. Choose Mężczyzna
# 4. In the Kod kraju dropdown field choose Albania
# 5. In the Mobile Phone number type 500000000
# 6. In the E-mail text field type jozefdeser@gmail.com
# 7. In the Hasło text field type Dese3!
# 8. In the Narodowość (Obywatelstwo) text field type Albania
# 9. Check the Akceptuję checkbox
# 10. Click ZAREJESTRUJ SIĘ button
#
#
# #4 Niepoprawne hasło - bez cyfr
# 1. In the Imię text field type Jozef
# 2. In the Nazwisko text field type Deser
# 3. Choose Mężczyzna
# 4. In the Kod kraju dropdown field choose Albania
# 5. In the Mobile Phone number type 500000000
# 6. In the E-mail text field type jozefdeser@gmail.com
# 7. In the Hasło text field type DeserPyszny!
# 8. In the Narodowość (Obywatelstwo) text field type Albania
# 9. Check the Akceptuję checkbox
# 10. Click ZAREJESTRUJ SIĘ button
#
#
# #5 rejestracja bez wyboru kobieta - mężczyzna
# 1. In the Imię text field type Jozef
# 2. In the Nazwisko text field type Deser
# 3. In the Kod kraju dropdown field choose Albania
# 4. In the Mobile Phone number type 500000000
# 5. In the E-mail text field type jozefdeser@gmail.com
# 6. In the Hasło text field type DeserPyszny123!
# 7. In the Narodowość (Obywatelstwo) text field type Albania
# 8. Check the Akceptuję checkbox
# 9. Click ZAREJESTRUJ SIĘ button

if __name__ == '__main__':
    unittest.main()

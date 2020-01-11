import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

#Scenariusz rejestracja

@Setup

def setUp(self):
    #Go to https: // wizzair.com / pl - pl  # /
    self.driver = webdriver.Chrome()
    self.driver.get('https://wizzair.com/pl-pl/#/')
    self.driver.maximize_window()
    self.driver.implicitly_wait(1)

    #2. Click on ZALOGUJ SIĘ tab
    zalogujSieButton = self.driver.find_element_by_link_text("Zaloguj się")
    zalogujSieButton.click();

    3. Click on the REJESTRACJA link


#1 Rejestracja ze znakami diakretycznymi w polu imię
1. In the Imię text field type Józef
2. In the Nazwisko text field type Deser
3. Choose Mężczyzna
4. In the Kod kraju dropdown field choose Albania
5. In the Mobile Phone number type 500000000
6. In the E-mail text field type jozefdeser@gmail.com
7. In the Hasło text field type ILoveDeser123!
8. In the Narodowość (Obywatelstwo) text field type Albania
9. Check the Akceptuję checkbox
10. Click ZAREJESTRUJ SIĘ button

#2 Zostawienie pustego pola numeru telefonu
1. In the Imię text field type Jozef
2. In the Nazwisko text field type Deser
3. Choose Mężczyzna
4. In the Kod kraju dropdown field choose Albania
5. Leave the Mobile Phone number text field empty
6. In the E-mail text field type jozefdeser@gmail.com
7. In the Hasło text field type ILoveDeser123!
8. In the Narodowość (Obywatelstwo) text field type Albania
9. Check the Akceptuję checkbox
10. Click ZAREJESTRUJ SIĘ button


#3 Niepoprawne hasło - za krótkie
1. In the Imię text field type Jozef
2. In the Nazwisko text field type Deser
3. Choose Mężczyzna
4. In the Kod kraju dropdown field choose Albania
5. In the Mobile Phone number type 500000000
6. In the E-mail text field type jozefdeser@gmail.com
7. In the Hasło text field type Dese3!
8. In the Narodowość (Obywatelstwo) text field type Albania
9. Check the Akceptuję checkbox
10. Click ZAREJESTRUJ SIĘ button


#4 Niepoprawne hasło - bez cyfr
1. In the Imię text field type Jozef
2. In the Nazwisko text field type Deser
3. Choose Mężczyzna
4. In the Kod kraju dropdown field choose Albania
5. In the Mobile Phone number type 500000000
6. In the E-mail text field type jozefdeser@gmail.com
7. In the Hasło text field type DeserPyszny!
8. In the Narodowość (Obywatelstwo) text field type Albania
9. Check the Akceptuję checkbox
10. Click ZAREJESTRUJ SIĘ button


#5 rejestracja bez wyboru kobieta - mężczyzna
1. In the Imię text field type Jozef
2. In the Nazwisko text field type Deser
3. In the Kod kraju dropdown field choose Albania
4. In the Mobile Phone number type 500000000
5. In the E-mail text field type jozefdeser@gmail.com
6. In the Hasło text field type DeserPyszny123!
7. In the Narodowość (Obywatelstwo) text field type Albania
8. Check the Akceptuję checkbox
9. Click ZAREJESTRUJ SIĘ button

import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

addressFieldmail = "ala6789@gmail.com"
firstName1 = "Kunegunda"
lastName1 = "Boligłowa"
password1 = "Eloelo520"
addressAddress1 = "Skrzacikowa 10"
cityAddress1 = "Koziegłowy"
postCodeAddress1 = "12345"
alias1 = "eloeloelo"

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

        print("Startujemy.")

    def test(self):


        signInButton = self.driver.find_element_by_class_name('login')
        signInButton.click()

        addressField = self.driver.find_element_by_id('email_create')
        addressField.send_keys(addressFieldmail)

        createAnAccountButton = self.driver.find_element_by_id('SubmitCreate')
        createAnAccountButton.click()
        time.sleep(1)

        gender1 = self.driver.find_element_by_id('id_gender2')
        gender1.click()

        firstName = self.driver.find_element_by_id('customer_firstname')
        firstName.send_keys(firstName1)

        lastName = self.driver.find_element_by_id('customer_lastname')
        lastName.send_keys(lastName1)

        emailInputOnForm = self.driver.find_element_by_id('email')
        emailValue = emailInputOnForm.get_attribute('value')
        assert addressFieldmail == emailValue

        password = self.driver.find_element_by_id('passwd')
        password.send_keys(password1)

        day = Select(self.driver.find_element_by_name('days'))
        day.select_by_value('1')

        month = Select(self.driver.find_element_by_name('months'))
        month.select_by_value('1')

        year = Select(self.driver.find_element_by_name('years'))
        year.select_by_value('1989')

        newsletter = self.driver.find_element_by_id('newsletter')
        newsletter.click()

        firstNameAddress = self.driver.find_element_by_id('firstname')
        firstNameAddress.clear()
        firstNameAddress.send_keys('Kunegunda')

        lastNameAddress = self.driver.find_element_by_id('lastname')
        lastNameAddress.clear()
        lastNameAddress.send_keys('Boligłowa')

        addressAddress = self.driver.find_element_by_id('address1')
        addressAddress.send_keys(addressAddress1)

        cityAddress = self.driver.find_element_by_id('city')
        cityAddress.send_keys(cityAddress1)

        state = Select(self.driver.find_element_by_name('id_state'))
        state.select_by_value('1')

        postCodeAddress = self.driver.find_element_by_id('postcode')
        postCodeAddress.send_keys(postCodeAddress1)

        country = Select(self.driver.find_element_by_name('id_country'))
        country.select_by_value('21')

        mobilePhone = self.driver.find_element_by_id('phone_mobile')
        mobilePhone.send_keys('123456789')

        alias = self.driver.find_element_by_name('alias')
        alias.clear()
        alias.send_keys(alias1)

        register = self.driver.find_element_by_id("submitAccount")
        register.click()

        home = self.driver.find_element_by_class_name('navigation_page')
        assert home.text == 'My account'

        time.sleep(5)

        print("Tu testujemy.")
        pass

    def tearDown(self):
        self.driver.close()
        print("Kończymy.")
        pass

if __name__ == '__main__':
    unittest.main()


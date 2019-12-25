from threading import Thread

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

#This example requires Selenium WebDriver 3.13 or newer
class seven:

    def doSomething(email_address,phone_number):
            driver = webdriver.Chrome(executable_path=r"C:\Users\pemawangyal\Downloads\chromedriver_win32\chromedriver.exe")
            driver.get('https://www.7-eleven.com/register')

            first_name = driver.find_element_by_id('RegisterPage_firstName')
            first_name.send_keys('Jay')

            email = driver.find_element_by_id('RegisterPage_email')
            #make sure user input here is not only numbers.. and must contain @
            if('@' in email_address):
                email.send_keys(email_address)
            else:
                print("invalid email address ")
                os.kill()

            password = driver.find_element_by_id('RegisterPage_password')
            password.send_keys('Taktuk1241$')

            birth_month = Select(driver.find_element_by_id('RegisterPage_birthMonth'))
            birth_month.select_by_value('05')
            birth_date = Select(driver.find_element_by_id('RegisterPage_birthDay'))
            birth_date.select_by_value('5')
            birth_year = Select(driver.find_element_by_id('RegisterPage_birthYear'))
            birth_year.select_by_value('1991')

            phoneNumber = driver.find_element_by_id('RegisterPage_phone')
            # make sure user input is number
            try:
                val = int(phone_number)
                phoneNumber.send_keys(phone_number)
            except ValueError:
                print("That's not an int!")
                os.kill()


            zipCode = driver.find_element_by_id('RegisterPage_zip')
            zipCode.send_keys('14214')

            terms_and_conditions = driver.find_element_by_id('cb-legal')
            terms_and_conditions.send_keys(Keys.SPACE)

            register_button = driver.find_element_by_css_selector("input[value='Register']")
            register_button.click()





    if __name__ == "__main__" :
        email_address1 = input("Enter your email address")
        print("your email : " + email_address1)
        phone_number1 = input("Enter your phone number")
        print("your phone number : " + phone_number1)

        doSomething(email_address1,phone_number1)



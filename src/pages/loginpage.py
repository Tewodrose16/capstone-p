from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver): # this method is called when object of the class is created
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # implicity define time sleep

    def login_textbox(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='userid']")))

            assert submit_button.is_displayed(), "user id textbox is not displayed on the page."
            submit_button.send_keys(2985)


        except Exception as e:
            print(f"Assertion failed: {e}")

    def click_login(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "// input[contains( @ value, 'Login')]"))
            )
            assert submit_button.is_displayed(), "log in button is not displayed on the page."
            submit_button.click()


        except Exception as e:
            print(f"Assertion failed: {e}")

    def click_logout(self):
        try:
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/logout']"))
            )
            assert logout_button.is_displayed(), "logout button is not displayed on the page."
            logout_button.click()


        except Exception as e:
            print(f"Assertion failed: {e}")

    def click_home(self):
        try:
            home_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Home']"))

            )
            assert home_button.is_displayed(), "Home button is not displayed on the page."
            home_button.click()


        except Exception as e:
            print(f"Assertion failed: {e}")

    def login_textbox2(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='userid']"))
            )
            assert submit_button.is_displayed(), "user id textbox is not displayed on the page."
            submit_button.send_keys(2984)



        except Exception as e:
            print(f"Assertion failed: {e}")

    def login_again(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "// input[contains( @ value, 'Login')]"))
            )
            assert submit_button.is_displayed(), "log in button is not displayed on the page."
            submit_button.click()


        except Exception as e:
            print(f"Assertion failed: {e}")

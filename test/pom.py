import os
import time

from selenium import webdriver

from src.pages.Landingpage import LandingPage
from src.pages.regesterationpage import RegPage
from src.pages.loginpage import LoginPage
from src.pages.product import ProductPage
from src.pages.cartpage import CartPage
from src.pages.orderpage import OrderPage
driver = webdriver.Chrome()
driver.get("http://shop.icraftsoft.net:8095/")
driver.maximize_window()
# Landingpage

lp = LandingPage(driver)

lp.click_login()

time.sleep(5)

# Registration
Reg = RegPage(driver)
Reg.getUsername()
Reg.getEmail()
Reg.getButton()
time.sleep(5)

#Login page
driver.get("http://shop.icraftsoft.net:8095/")
LP = LoginPage(driver)
LP.login_textbox()
time.sleep(2)
LP.click_login()
time.sleep(2)
LP.click_logout()
time.sleep(2)
LP.click_home()
time.sleep(2)
LP.login_textbox2()
time.sleep(2)
LP.login_again()
time.sleep(2)
# prodctpage
Prop = ProductPage(driver)
Prop.search_box()
time.sleep(2)
Prop.Quick_view_product()
time.sleep(2)
Prop.select_Product1()
time.sleep(2)
Prop.Add_to_Cart()
time.sleep(2)
Prop.second_cart()
time.sleep(5)
# Cartpage
Cart = CartPage(driver)
Cart.click_on_cart()
time.sleep(5)
# Orderpage
Orp = OrderPage(driver)
time.sleep(5)
Orp.remove_items()
time.sleep(5)
Orp.continue_shop()
time.sleep(5)
Orp.click_on_cart()
time.sleep(5)
Orp.click_on_Buy_now()
time.sleep(5)
Orp.click_on_home()
time.sleep(5)
import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.CartPage import CartPage
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(2)

        # Professional way to wait for a Title Change
        WebDriverWait(self.driver, 5).until(EC.title_is("Swag Labs"))

        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/test_login.png")
            assert False

    def test_add_to_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        # 1. Login
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # 2. Add to Cart & Checkout
        self.cp = CartPage(self.driver)
        self.cp.addBackpackToCart()
        self.cp.goToCart()
        self.cp.clickCheckout()

        # 3. Enter Details
        self.cp.inputPersonalDetails("Rajneesh", "Kumar", "123456")
        self.cp.clickContinue()
        self.cp.clickFinish()

        # 4. Final Validation
        msg = self.cp.getSuccessMsg()
        if msg == "Thank you for your order!":
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/test_cart_fail.png")
            assert False

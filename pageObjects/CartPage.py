from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    # Locators
    btn_add_backpack_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    link_cart_xpath = "//a[@class='shopping_cart_link']"
    btn_checkout_id = "checkout"
    txt_firstname_id = "first-name"
    txt_lastname_id = "last-name"
    txt_zip_id = "postal-code"
    btn_continue_id = "continue"
    btn_finish_id = "finish"
    msg_success_xpath = "//h2[normalize-space()='Thank you for your order!']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def addBackpackToCart(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_add_backpack_xpath))).click()

    def goToCart(self):
        self.driver.find_element(By.XPATH, self.link_cart_xpath).click()

    def clickCheckout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.btn_checkout_id))).click()

    def inputPersonalDetails(self, fname, lname, zip_code):
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)
        self.driver.find_element(By.ID, self.txt_zip_id).send_keys(zip_code)

    def clickContinue(self):
        self.driver.find_element(By.ID, self.btn_continue_id).click()

    def clickFinish(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.btn_finish_id))).click()

    def getSuccessMsg(self):
        return self.driver.find_element(By.XPATH, self.msg_success_xpath).text
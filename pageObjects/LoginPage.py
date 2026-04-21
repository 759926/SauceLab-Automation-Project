from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    button_menu_id = "react-burger-menu-btn"
    link_logout_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # 10 seconds timeout

    def setUserName(self, username):
        user_input = self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_username_id)))
        user_input.clear()
        user_input.send_keys(username)

    def setPassword(self, password):
        pass_input = self.wait.until(EC.visibility_of_element_located((By.ID, self.textbox_password_id)))
        pass_input.clear()
        pass_input.send_keys(password)

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.button_login_id))).click()

    def clickLogout(self):
        # Click menu and wait for the sidebar animation
        self.wait.until(EC.element_to_be_clickable((By.ID, self.button_menu_id))).click()
        # Wait for logout link to be interactable
        logout_link = self.wait.until(EC.element_to_be_clickable((By.ID, self.link_logout_id)))
        logout_link.click()
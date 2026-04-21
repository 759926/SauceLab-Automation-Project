import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Options: chrome, firefox, safari")


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = Options()

        # --- DISABLING BROWSER POPUPS ---
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.profile_enabled": False  # Disables address/card popups too
        }
        options.add_experimental_option("prefs", prefs)

        # --- CLEAN AUTOMATION STATE ---
        options.add_argument("--disable-infobars")  # Hides "Chrome is being controlled..."
        options.add_argument("--disable-notifications")  # Blocks site notification popups
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FFOptions()
        # Firefox handles private/automation mode differently
        options.set_preference("dom.webnotifications.enabled", False)
        driver = webdriver.Firefox(options=options)

    elif browser == "safari":
        # Safari doesn't support 'Options' the same way as Chrome/Firefox
        driver = webdriver.Safari()

    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()


# --- Optional: Custom Metadata for your Reports ---
def pytest_configure(config):
    config.metadata = {
        "Project Name": "Sauce Demo",
        "Module": "Login & Cart",
        "Tester": "Rajneesh"
    }
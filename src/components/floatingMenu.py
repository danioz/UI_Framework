from selenium.webdriver.common.by import By
from src.base.uiElement import UiElement


class FloatingMenu:
    __BTN_LOGOUT = UiElement(By.ID, 'logout_sidebar_link')

    def __init__(self):
        pass

    @staticmethod
    def clickLogout():
        FloatingMenu.__BTN_LOGOUT.waitToClick().doClick()
        from src.pages.loginPage import LoginPage
        return LoginPage()

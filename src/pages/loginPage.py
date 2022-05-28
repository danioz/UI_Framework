from selenium.webdriver.common.by import By
from src.base.basePage import BasePage
from src.base.uiElement import UiElement


class LoginPage(BasePage):
    __INPUT_USERNAME = UiElement(By.ID, 'user-name')
    __INPUT_PASSWORD = UiElement(By.ID, 'password')
    __BTN_LOGIN = UiElement(By.ID, 'login-button')
    __ERROR_MSG = UiElement(By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self):
        super().__init__()

    def getErrorMsg(self):
        return self.__ERROR_MSG.getText()

    def setUsername(self, username):
        self.__INPUT_USERNAME.setText(username)
        return self

    def setPassword(self, password):
        self.__INPUT_PASSWORD.setText(password)
        return self

    def clickLogin(self):
        self.__BTN_LOGIN.doClick()
        return self

    def doLogin(self, username, password):
        self.setUsername(username) \
            .setPassword(password) \
            .clickLogin()
        from src.pages.inventoryPage import InventoryPage
        return InventoryPage()

    def getInputs(self):
        inputs = []
        elements = UiElement(By.XPATH, '//input').getElements()
        for element in elements:
            input = UiElement.fromWebElement(element).getAttribute('id')
            inputs.append(input)
        return inputs

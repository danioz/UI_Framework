from selenium.webdriver.common.by import By
from src.base.basePage import BasePage
from src.base.uiElement import UiElement
from src.components.floatingMenu import FloatingMenu
from src.components.pageFooter import PageFooter
from src.components.pageHeader import PageHeader


class InventoryPage(BasePage):
    __TITLE = UiElement(By.CSS_SELECTOR, '.title')

    def __init__(self):
        super().__init__()

        self.header = PageHeader()
        self.footer = PageFooter()
        self.floatingButton = FloatingMenu()

    def getTitle(self):
        return self.__TITLE

    def getTextFromTitle(self):
        return self.getTitle().getText()

    def userIsLoggedIn(self):
        return self.getTitle().isVisible()


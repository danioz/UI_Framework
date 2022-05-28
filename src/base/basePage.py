from src.base.browser import Browser


class BasePage:

    def __init__(self):
        self.URL = "http://www.saucedemo.com"

    def open(self):
        Browser.getDriver().get(self.URL)
        return self

    def getActualTitle(self, wait=10):
        return Browser.getDriver().title

    def getActualUrl(self):
        return Browser.getDriver().current_url

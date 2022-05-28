from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.base.browser import Browser


class UiElement:

    def __init__(self, by, locator, **kwargs):
        self.__by = by
        self.__locator = locator
        self.__webElement = kwargs.get("webElement", None)

    @staticmethod
    def fromWebElement(webElement):
        return UiElement(by=None, locator=None, webElement=webElement)

    @property
    def by(self):
        return self.__by

    @property
    def locator(self):
        return self.__locator

    def given(self):
        return self

    def then(self):
        return self

    def also(self):
        return self

    def getElement(self, wait=10):
        if self.__webElement:
            return self.__webElement
        self.waitToAppear(wait)
        return Browser.getDriver().find_element(self.by, self.locator)

    def getElements(self, wait=10):
        self.waitToAppear(wait)
        return Browser.getDriver().find_elements(self.by, self.locator)

    def isPresent(self, wait=1):
        try:
            WebDriverWait(Browser.getDriver(), wait, poll_frequency=0.5).until(
                ec.presence_of_element_located((self.by, self.locator)))
            return True
        except:
            return False

    def isVisible(self, wait=1):
        try:
            WebDriverWait(Browser.getDriver(), wait, poll_frequency=0.5).until(
                ec.invisibility_of_element_located((self.by, self.locator)))
            return False
        except:
            return True

    def isNotVisible(self):
        pass

    def isClickable(self, wait=1):
        try:
            WebDriverWait(Browser.getDriver(), wait).until(
                ec.element_to_be_clickable((self.by, self.locator)))
            return True
        except:
            return False

    def waitToAppear(self, wait=10):
        if self.isPresent(wait):
            return self
        raise AssertionError(f"Locator did not appear: {self.locator} in {wait}")

    def waitToDisappear(self, wait=10):
        if not self.isVisible(wait):
            return self
        raise AssertionError(f'Locator did not disappear: {self.locator} in {wait}')

    def waitToClick(self, wait=10):
        if self.isClickable(wait):
            return self
        if self.isPresent():
            raise AssertionError(f"Locator did not become click-able: {self.locator} in {wait} seconds")
        raise AssertionError(f"Locator does not exists: {self.locator}")

    def doClick(self, useAC=False, wait=10):
        if useAC:
            ActionChains(Browser.getDriver()).move_to_element(
                self.getElement(wait)).click().perform()
        self.getElement(wait).click()
        return self

    def setText(self, value, wait=10):
        self.getElement(wait).send_keys(value)
        return self

    def getText(self, wait=10):
        element = self.getElement(wait)
        text = element.text
        if len(text) == 0:
            text = UiElement.fromWebElement(element).getAttribute("innerText")
        return text

    def getAttribute(self, value, wait=10):
        return self.getElement(wait).get_attribute(value)

    def hoverOverElement(self, wait=10):
        ActionChains(Browser.getDriver()).move_to_element(
            self.getElement(wait)).perform()

    def scrollIntoView(self, wait=10):
        Browser.getDriver().execute_script("arguments[0].scrollIntoView()",
                                           self.getElement(wait))
        return self

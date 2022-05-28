import unittest
import time
from src.base.browser import Browser
from src.pages.loginPage import LoginPage


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" * 30)
        print("Class 1 -> class level setUp")
        print("*#" * 30)

    def setUp(self):
        print("Class 1 -> setUp")
        self.getDriver()

    def tearDown(self):
        self.closeDriver()
        print("Class 1 -> tearDown")

    @staticmethod
    def getDriver():
        Browser.createNewDriver(1, headless=True)

    @staticmethod
    def closeDriver():
        Browser.shutdown()

    @classmethod
    def tearDownClass(cls) -> None:
        print("*#" * 30)
        print("Class 1 -> class level tearDown")
        print("*#" * 30)

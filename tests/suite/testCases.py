import time
import traceback

from src.pages.loginPage import LoginPage
from src.pages.inventoryPage import InventoryPage
from src.components.pageHeader import PageHeader
from src.components.floatingMenu import FloatingMenu
from tests.baseTest import BaseTest
from src.utils.assertUtils import Assert


class Test_Smoke(BaseTest):

    def testSmoke_ShouldBeUsername(self):
        page = LoginPage()
        page.open()

        assert page.getUsername().getAttribute('id') == 'user-name'

    def testSmoke_ShouldBePassword(self):
        page = LoginPage()
        page.open()

        assert page.getPassword().getAttribute('id') == 'password'

    def testSmoke_ShouldBeLoginButton(self):
        page = LoginPage()
        page.open()

        assert page.getLoginBtn().getAttribute('id') == 'login-button'

class Test_Error_Messages(BaseTest):

    def test_ShouldGetErrorMsg(self):
        page = LoginPage()

        page.open() \
            .clickLogin()

        assert page.getErrorMsg() == 'Epic sadface: Username is required'

    def test_ShouldGetErrorMsg_noPassword(self):
        page = LoginPage()

        page.open() \
            .setPassword('password') \
            .clickLogin()

        assert page.getErrorMsg() == 'Epic sadface: Username is required'

    def test_ShouldGetErrorMsg_noLogin(self):
        page = LoginPage()

        page.open() \
            .setUsername('username') \
            .clickLogin()
        assert page.getErrorMsg() == 'Epic sadface: Password is required'

    def test_ShouldGetErrorMsg_noUser(self):
        page = LoginPage()

        page.open() \
            .setUsername('username') \
            .setPassword('password') \
            .clickLogin()

        assert page.getErrorMsg() == 'Epic sadface: Username and password do not match any user in this service'

    def test_ShouldGetErrorMsg_lockedUser(self):
        page = LoginPage()

        page.open() \
            .setUsername('locked_out_user') \
            .setPassword('secret_sauce') \
            .clickLogin()

        assert page.getErrorMsg() == 'Epic sadface: Sorry, this user has been locked out.'

class Test_Login(BaseTest):

    def test_ShouldBeLoggedIn(self):
        page = LoginPage()
        page.open().doLogin('standard_user', 'secret_sauce')

        assert InventoryPage().getActualUrl() == 'https://www.saucedemo.com/inventory.html'

    def test_ShouldBeTitleDisplayed(self):
        page = LoginPage()
        inventoryPage = page.open().doLogin('standard_user', 'secret_sauce')

        Assert.assertTrue(inventoryPage.userIsLoggedIn(), 'User is not logged in')
        assert inventoryPage.getTextFromTitle() == 'PRODUCTS'

    def test_ShouldBeLoggedOut(self):
        page = LoginPage()
        page.open().doLogin('standard_user', 'secret_sauce')

        PageHeader.clickBurgerMenu()
        FloatingMenu.clickLogout()

        assert page.getActualUrl() == 'https://www.saucedemo.com/'




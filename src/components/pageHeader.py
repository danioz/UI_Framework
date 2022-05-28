from selenium.webdriver.common.by import By
from src.base.uiElement import UiElement


class PageHeader:
    __BURGER_MENU = UiElement(By.CSS_SELECTOR, '#react-burger-menu-btn')
    __SHOPPING_CART = UiElement(By.CSS_SELECTOR, '.shopping_cart_link')
    __CART_ITEM = UiElement(By.CSS_SELECTOR, '.shopping_cart_badge')

    def __init__(self):
        pass

    @staticmethod
    def clickShoppingCart():
        PageHeader.__SHOPPING_CART.doClick()
        from src.pages.cartPage import CartPage
        return CartPage()

    @staticmethod
    def getNumberOfItemsInCart():
        return PageHeader.__CART_ITEM.getText()

    @staticmethod
    def clickBurgerMenu():
        PageHeader.__BURGER_MENU.doClick()
        from src.components.floatingMenu import FloatingMenu
        return FloatingMenu()

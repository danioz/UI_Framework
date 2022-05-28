import threading
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


class Browser:
    CHROME = 1
    FF = 2
    OPERA = 3
    EDGE = 4

    __DRIVER_MAP = {}

    @staticmethod
    def createNewDriver(driver_id, **kwargs):
        threadObject = threading.currentThread()

        def getDriver():
            if Browser.CHROME == driver_id:
                options = webdriver.ChromeOptions()
                if kwargs.get("proxy_port"):
                    options.add_argument(f'--proxy-server={kwargs.get("proxy_port")}')
                if kwargs.get("headless"):
                    options.add_argument('--headless')
                if kwargs.get("enable-automation"):
                    options.add_argument('enable-automation')
                if kwargs.get("disable-browser-side-navigation"):
                    options.add_argument('--disable-browser-side-navigation')
                if kwargs.get("no_sandbox"):
                    options.add_argument('--no-sandbox')
                if kwargs.get("disable_shm"):
                    options.add_argument('--disable-dev-shm-usage')
                if kwargs.get("disable_notifications"):
                    options.add_argument('--disable-notifications')
                if kwargs.get("window_size"):
                    options.add_argument(f'--window-size={kwargs.get("windows_size")}')
                if kwargs.get("dev_tools_port"):
                    options.add_argument(f'--remote-debugging-port={kwargs.get("dev_tools_port")}')
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            elif Browser.FF == driver_id:
                options = Options()
                if kwargs.get("headless"):
                    options.add_argument("--headless")
                if kwargs.get("--disable-plugins"):
                    options.add_argument("--disable-plugins")

                    options.add_argument("--disable-extensions")

                    options.add_argument("--disable-popup-blocking")

                    options.add_argument("-nable-automation")

                    options.add_argument("--no-sandbox")

                    options.add_argument("--disable-dev-shm-usage")

                    options.add_argument("--disable-browser-side-navigation")

                    options.add_argument("--disable-gpu")

                    options.add_argument("--ignore-certificate-errors")

                    options.add_argument("force-device-scale-factor=1")

                    options.add_argument("high-dpi-support=1")


                driver = webdriver.Firefox(
                    executable_path=GeckoDriverManager().install(), options=options)
            elif Browser. OPERA == driver_id:
                driver = webdriver.Opera(executable_path=OperaDriverManager().install())
            elif Browser.EDGE == driver_id:
                driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            else:
                raise Exception(f"There is no support for driver_id: {driver_id}")

            return driver

        Browser.__map(threadObject, getDriver())
        return Browser.getDriver()

    @staticmethod
    def __map(thread, driver):
        Browser.__DRIVER_MAP[thread] = {"driver": driver}

    @staticmethod
    def getDriver():
        # todo
        # if threading.currentThread() not in Browser.__DRIVER_MAP:
        #     Browser.createNewDriver(???)
        return Browser.__DRIVER_MAP[threading.currentThread()]['driver']

    @staticmethod
    def shutdown():
        Browser.getDriver().quit()

    @staticmethod
    def getDriverMap():
        return Browser.__DRIVER_MAP

    @staticmethod
    def forward():
        Browser.getDriver().forward()

    @staticmethod
    def back():
        Browser.getDriver().back()







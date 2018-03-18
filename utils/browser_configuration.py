# 需要解决drivers 文件路径调用问题
import configparser
import os.path
from selenium import webdriver
from utils.logger import Logger
from utils.config import DRIVER_PATH, REPORT_PATH
import time

logger = Logger(logger="BrowserConfiguration").getlog()

CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'
FIREFOXDRIVER_PATH = DRIVER_PATH + '\geckodriver.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': FIREFOXDRIVER_PATH, 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class BrowserConfiguration(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=10):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self



    # def open_browser(self, driver):
    #     config = configparser.ConfigParser()
    #     file_path = os.path.dirname(os.getcwd()) + "/config/config.ini"
    #     print(file_path)
    #     # grader_father = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "..")
    #     # grader_father = os.path.abspath(os.path.dirname(os.getcwd()))
    #     # print(grader_father)
    #     config.read(file_path, "utf-8")
    #
    #     browser = config.get("browserType", "browserName")
    #     logger.info("you selected %s browser." %browser)
    #     url = config.get("testURL", "URL")
    #     logger.info("The test URL is: %s" %url)
    #
    #     if browser == "Firefox":
    #         driver  = webdriver.Firefox(self.driver_path_firefox)
    #         logger.info("Starting open firefox browser")
    #     elif browser == "Chrome":
    #         driver = webdriver.Chrome(self.driver_path_chrome)
    #         logger.info("Starting Chrome browser")
    #     elif browser == "Ie":
    #         driver  = webdriver.Ie(self.driver_path_ie)
    #         logger.info("Starting open firefox Ie")
    #
    #     driver.maximize_window()
    #     logger.info("Maximize the current window")
    #     driver.get(url)
    #     logger.info("Open url: %s" %url)
    #     driver.implicitly_wait(5)
    #     logger.info("implicitly 5 seconds")
    #     return driver

    def quit_browser(self):
        logger.info("Close and quit the browser")
        self.driver.quit()


if __name__ == '__main__':
    b = BrowserConfiguration('chrome').get('http://www.mi.com')
    time.sleep(3)
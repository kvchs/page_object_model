import unittest
from test.page.mi_homepage import HomePage
from utils.browser_configuration import BrowserConfiguration
import time


class TestMiHomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserConfiguration("chrome")
        cls.driver = browser.get("http://www.mi.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search(self):
        homepage = HomePage(self.driver)
        homepage.search_text("tython")
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()



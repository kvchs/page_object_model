import time
import unittest
from utils.browser_configuration import BrowserConfiguration
from test.page.baidu_homepage import HomePage


class BaiDuSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserConfiguration("chrome")
        cls.driver = browser.get('http://www.mi.com')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit_browser()

    def test_baidu_search(self):
        homepage = HomePage(self.driver)
        homepage.type_search("selenium")
        homepage.send_submit_btn()
        time.sleep(5)
        # homepage.get_screen_img()
        try:
            assert "selenium" in homepage.get_page_title()
            print("Test pass")
        except Exception as e:
            print("Test failed.", format(e))

    def test_baidu_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search("python")
        homepage.send_submit_btn()
        time.sleep(5)
        # homepage.get_screen_img()
        try:
            assert "selenium3" in homepage.get_page_title()
            print("Test pass")
        except Exception as e:
            print("Test failed.", format(e))


if __name__ == '__main__':
    unittest.main()
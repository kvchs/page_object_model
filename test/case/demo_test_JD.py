import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.POM_config import Config, DRIVER_PATH


class TestMi(unittest.TestCase):
    URL = Config().get("URL")
    # URL = "https://www.jd.com/"
    # base_path = os.path.dirname(os.path.dirname(os.path.abspath('.')))
    # print(base_path)
    # driver_path = os.path.abspath(base_path + '\drivers\geckodriver.exe')
    locator_box = (By.ID, "key")
    locator_search = (By.XPATH, ".//*[@id='search']/div/div[2]/button")
    print(DRIVER_PATH)

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_xiaomi5(self):
        self.driver.find_element(*self.locator_box).send_keys("小米5")
        self.driver.find_element(*self.locator_search).click()
        time.sleep(3)

    def test_search_xiaomi7(self):
        self.driver.find_element(*self.locator_box).send_keys("小米7")
        self.driver.find_element(*self.locator_search).click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()



# --------------------------------------------------------------------
# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# URL = "https://www.jd.com/"
# # base_path = os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd())))
# base_path = os.path.dirname(os.path.dirname(os.path.abspath(".")))
# driver_path = os.path.abspath(base_path + "\drivers\chromedriver.exe")
# locator_box = (By.ID, "key")
# locator_search = (By.XPATH, ".//*[@id='search']/div/div[2]/button")
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get(URL)
# driver.find_element(*locator_box).send_keys("python")
# driver.find_element(*locator_search).click()
# time.sleep(5)
#
# print(base_path)
# driver.quit()



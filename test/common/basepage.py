import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from utils.log import Logger
from utils.config import DRIVER_PATH, REPORT_PATH

# create a logger instance
logger = Logger().get_logger()


class BasePage(object):
    '''
    configuration public method
    '''

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        logger.info("Click forward button on current page")

    def back(self):
        self.driver.back()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def close_window(self):
        try:
            self.driver.close()
            logger.info("Close current window")
        except Exception as e:
            logger.error("No such window find, can not close it", format(e))

    def save_screen_shot(self, name='mi'):
        try:
            day = time.strftime('%Y%m%d', time.localtime(time.time()))
            screenshot_path = REPORT_PATH + '\screenshot_%s' % day
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)

            tm = time.strftime('%H%M%S', time.localtime(time.time()))
            screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
            return screenshot
        except Exception as e:
            logger.error("Failed to save screen_shot" % e)

    def find_element(self, selector):

        element = ''
        if "=>" not in selector:
            print("selector is incorrect")
        selector_key = selector.split("=>")[0]
        selector_value = selector.split("=>")[1]
        if selector_key == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("find element %s successful" % selector)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_key == "name":
            element = self.driver.find_element_by_name(selector_value)
        elif selector_key == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_key == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_key == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_key == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_key == "xpath":
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("find element %s successful" % selector)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_key == "css_selector":
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("please enter a vaild type of targeting element.")
        return element

    # 定位元素输入
    def input_text(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("input content %s " % text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.save_screen_shot()

    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("clear text in input box successful")
        except Exception as e:
            logger.error("Failed to clear input box content" % e)
            self.save_screen_shot()

    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("the element is clicked")
        except Exception as e:
            logger.error("Failed to click the element")

    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod  # 静态方法f，类可以不用实例化就可以调用该方法 C.f()，也可以实例化后调用 C().f()。
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("sleep for %d seconds" %seconds)



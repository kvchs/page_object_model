from test.common.basepage import BasePage


class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"
    news_link = "xpath=>//*[@id='u1']/a[1]"

    def type_search(self, text):
        self.input_text(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
        self.sleep(3)
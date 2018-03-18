from test.common.basepage import BasePage


class HomePage(BasePage):
    input_box = "id=>search"

    def search_text(self, text):
        self.input_text(self.input_box, text)
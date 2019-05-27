from base.base import BasePage
from page.pageElement import PageElement


class InputNewText(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def InputNewNamePage(self):
        self.send_element(PageElement.text_name_id,"15000604524")

    def InputNewTextPage(self, text):
        self.send_element(PageElement.input_text_id, text)
        self.click_element(PageElement.send_text_btn_id)

    def res_text_list(self):
        return self.get_elements(PageElement.text_list_ids)

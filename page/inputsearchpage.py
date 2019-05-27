from base.base import BasePage
from page.pageElement import PageElement


class InputSearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def input_search_text(self, text):
        self.send_element(PageElement.search_text_id, text)

    def get_search_res_list(self):
        return self.get_elements(PageElement.search_res_list_ids)

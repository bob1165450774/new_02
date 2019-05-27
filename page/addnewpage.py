from base.base import BasePage
from page.pageElement import PageElement


class AddNewPage(BasePage):
    def __init__(self,driver):
        self.driver=driver

    def click_add_new_text(self):
        self.click_element(PageElement.add_text_btn_id)
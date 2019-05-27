from base.base import BasePage
from page.pageElement import PageElement


class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_search_btn(self):
        self.click_element(PageElement.search_btn_id)

from base.base import BasePage
from page.pageElement import PageElement


class SettingPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def click_more_btn(self):
        self.click_element(PageElement.more_btn_xpath)

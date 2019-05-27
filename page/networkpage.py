from base.base import BasePage
from page.pageElement import PageElement


class NetworkPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def click_network_btn(self):
        self.click_element(PageElement.network_setting_xpath)

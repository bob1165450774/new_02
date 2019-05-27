from base.base import BasePage
from page.addnewpage import AddNewPage
from page.input_new_text import InputNewText
from page.inputsearchpage import InputSearchPage
from page.networkpage import NetworkPage
from page.searchpage import SearchPage
from page.settingnetwork import SetNetworkPage
from page.settingpage import SettingPage


class PageAll(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def get_setting_page(self):
        return SettingPage(self.driver)

    def get_network_page(self):
        return NetworkPage(self.driver)

    def get_set_network_page(self):
        return SetNetworkPage(self.driver)

    def get_add_text_page(self):
        return AddNewPage(self.driver)

    def get_input_text_page(self):
        return InputNewText(self.driver)

    def get_input_search_page(self):
        return InputSearchPage(self.driver)

    def get_search_page(self):
        return SearchPage(self.driver)

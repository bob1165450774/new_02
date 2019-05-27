from base.base import BasePage
from page.pageElement import PageElement


class SetNetworkPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def set_network(self):
        self.click_element(PageElement.network_type_xpath)
        self.click_element(PageElement.two_network_xpath)

    def get_result_network_type(self):
        return self.get_elements(PageElement.result_network_list_ids)

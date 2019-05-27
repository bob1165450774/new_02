from base import getDriver
from page.PageAll import PageAll


class TestNetwork(object):

    def setup_class(self):
        self.driver = getDriver.get_driver("com.android.settings", ".Settings")
        self.page_obj = PageAll(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_set_network(self):
        self.page_obj.get_setting_page().click_more_btn()
        self.page_obj.get_network_page().click_network_btn()
        self.page_obj.get_set_network_page().set_network()
        assert "2G" in [i.text for i in self.page_obj.get_set_network_page().get_result_network_type()]

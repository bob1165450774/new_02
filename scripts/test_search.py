import pytest

from base.getDriver import get_driver
from page.PageAll import PageAll


class TestSearch(object):

    def setup_class(self):
        self.driver = get_driver("com.android.settings", ".Settings")
        self.page_obj = PageAll(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def test_search_page(self):
        self.page_obj.get_search_page().click_search_btn()

    @pytest.mark.parametrize("search_data,expect_data", [("1", "休眠"), ("w", "WLAN直连"), ("m", "MAC地址")])
    def test_input_search(self, search_data, expect_data):
        self.page_obj.get_input_search_page().input_search_text(search_data)
        assert expect_data in [i.text for i in self.page_obj.get_input_search_page().get_search_res_list()]

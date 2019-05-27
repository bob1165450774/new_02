import os
import sys

import allure
import pytest

sys.path.append(os.getcwd())

from base import getDriver
from base.get_data import GetData
from page.PageAll import PageAll


def get_data_001():
    # [("123","123"),("hello","hello"),("#!!","#!!")]

    # with open("C:\\Users\\bob1994\\Desktop\\homework\\data\\data_001.yml", "r", encoding="utf-8") as f:

    send_expect_data = []
    data = GetData().get_data("data_001.yml").get("TestSmsData")
    for i in data.values():
        send_expect_data.append((i.get("send"), i.get("expect")))
    return send_expect_data


class TestText:
    def setup_class(self):
        self.driver = getDriver.get_driver("com.android.mms", ".ui.ConversationList")
        self.page_obj = PageAll(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤1")
    def test_add_text_name(self):
        self.page_obj.get_add_text_page().click_add_new_text()
        self.page_obj.get_input_text_page().InputNewNamePage()
        allure.attach("新增短信", "点击新建按钮")
        with open("C:\\Users\\bob1994\\Desktop\\homework\\scripts\\3397889.jpg", "rb") as f:
            allure.attach("何多苓", f.read(), allure.attach_type.PNG)

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="测试步骤2")
    @pytest.mark.parametrize("input_data,expect_data", get_data_001())
    def test_input_text(self, input_data, expect_data):
        self.page_obj.get_input_text_page().InputNewTextPage(input_data)
        allure.attach("发送短信", "读数据,发送短信")
        assert expect_data in [i.text for i in self.page_obj.get_input_text_page().res_text_list()]

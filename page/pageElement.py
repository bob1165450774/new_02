from selenium.webdriver.common.by import By


class PageElement(object):
    more_btn_xpath = (By.XPATH, "//*[contains(@text,'更多')]")
    network_setting_xpath = (By.XPATH, "//*[contains(@text,'移动网络')]")
    network_setting_xpath = (By.XPATH, "//*[contains(@text,'移动网络')]")
    network_type_xpath = (By.XPATH, "//*[contains(@text,'首选网络类型')]")
    two_network_xpath = (By.XPATH, "//*[contains(@text,'2G')]")
    result_network_list_ids = (By.ID, "android:id/summary")
    add_text_btn_id = (By.ID, "com.android.mms:id/action_compose_new")
    text_name_id = (By.ID, "com.android.mms:id/recipients_editor")
    input_text_id = (By.ID, "com.android.mms:id/embedded_text_editor")
    send_text_btn_id = (By.ID, "com.android.mms:id/send_button_sms")
    text_list_ids = (By.ID, "com.android.mms:id/text_view")
    search_btn_id = (By.ID, "com.android.settings:id/search")
    search_text_id = (By.ID, "android:id/search_src_text")
    search_res_list_ids = (By.ID, "com.android.settings:id/title")

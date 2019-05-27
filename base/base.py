from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=20, poll_frequency=2.0):
        """

        :param loc:单个元素定位信息
        :param timeout: 显示等待时长,默认设置为20s
        :param poll_frequency: 每隔2秒搜索一次,设置为2.0(原方法为此格式)
        :return: 元素对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=20, poll_frequency=2):
        """

        :param loc: 一组元素共有的定位信息
        :param timeout: 显示等待时长,默认设置为20s
        :param poll_frequency: 每隔2秒搜索一次,设置为2.0(原方法为此格式)
        :return: 一组元素
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=20, poll_frequency=2):
        """

        :return:点击元素方法
        """
        self.get_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=20, poll_frequency=2):
        """

        :param text: 输入文本
        :return: 元素对象输入文本
        """

        input_text = self.get_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

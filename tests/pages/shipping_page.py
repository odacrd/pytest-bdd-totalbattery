from tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ShippingPage(BasePage):

    SHIPPINGPAGE_H1: list[tuple] = [(By.CSS_SELECTOR, "#content_area"), (By.CSS_SELECTOR, "h1:nth-child(2)")]

    @property
    def get_shipping_h1(self):
        return self.get_textcontent(self.SHIPPINGPAGE_H1)

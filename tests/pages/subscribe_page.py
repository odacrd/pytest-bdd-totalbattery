from tests.pages.base_page import BasePage
# from tests.pages.home_page import HomePage
from selenium.webdriver.common.by import By
import time


class SubscribePage(BasePage):
    SUBSCRIBE_BTN: list[tuple] = [(By.CSS_SELECTOR, "div[style='display: inline;']"), (By.TAG_NAME, "button")]
    SUBSCRIBE_DIV: list[tuple] = [(By.CSS_SELECTOR, "div[class='hb-modal-content']"),
                                  (By.CSS_SELECTOR, "input[type='email']")]
    SUBSCRIBE_HEAD: list[tuple] = [(By.CSS_SELECTOR, "div[class='hb-modal-content']"), (By.ID, "headline")]
    SUBSCRIBE_EMAIL: list[tuple] = [(By.CSS_SELECTOR, "div[class='hb-modal-content']"),
                                    (By.CSS_SELECTOR, "input[type='email']")]

    def close_subscribe_popup(self):
        time.sleep(10)
        self.click_on(self.SUBSCRIBE_BTN)
        self.wait_for_element_not_exists(self.SUBSCRIBE_BTN, 10)
        return self
        # return HomePage(self.driver)

    def enter_email(self, emailaddress):
        self.enter_text(self.SUBSCRIBE_EMAIL, emailaddress)
        return self

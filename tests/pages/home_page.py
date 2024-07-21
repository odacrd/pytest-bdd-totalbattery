from tests.pages.base_page import BasePage
from tests.pages.store_page import StorePage
from tests.pages.subscribe_page import SubscribePage
import time
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    HOME_TAB: list[tuple] = [(By.CSS_SELECTOR, "a[title='Home']")]
    APPLICATIONS_TAB: list[tuple] = [(By.CSS_SELECTOR, "a[title='Applications']")]
    BATTERIES_TAB: list[tuple] = [(By.CSS_SELECTOR, "a[title='Batteries']")]
    STORELINK: list[tuple] = [(By.CSS_SELECTOR, "a[class='eup-button'][href*='webstore']")]
    BRANDS_TAB: list[tuple] = [(By.CSS_SELECTOR, "#menu-item-2264 > a[class='nav-link'][title='Brands']")]
    BRANDS_TOGGLE: list[tuple] = [(By.CSS_SELECTOR, "#menu-item-1648 .state-indicator")]
    SUBSCRIBE_POPUP: list[tuple] = [(By.CSS_SELECTOR, "div[style='display: inline;']")]
    SUBSCRIBE_BTN: list[tuple] = [(By.CSS_SELECTOR, "div[style='display: inline;']"), (By.TAG_NAME, "button")]


    @property
    def home_tab_text(self):
        return self.get_textcontent(self.HOME_TAB)

    @property
    def applications_tab_text(self):
        return self.get_textcontent(self.APPLICATIONS_TAB)


    def go_to_online_store(self):
        self.click_on(self.STORELINK)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return StorePage(self.driver)

    def wait_for_subscribe_popup(self):
        time.sleep(10)
        self.wait_for_clickable_element_by(self.SUBSCRIBE_BTN)
        return SubscribePage(self.driver)
    def go_to_home_page(self):
        return HomePage(self.driver)
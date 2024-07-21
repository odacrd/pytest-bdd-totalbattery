from tests.pages.base_page import BasePage
from tests.pages.cart_popup import CartPopup
from tests.pages.shipping_page import ShippingPage
import time
from selenium.webdriver.common.by import By


class StorePage(BasePage):
    SHIPPINGLINK: list[tuple] = [(By.ID, "header-top"), (By.LINK_TEXT, "SHIPPING")]
    HOMESITELINK: list[tuple] = [(By.ID, "header-top"), (By.LINK_TEXT, "HOME SITE")]
    SMALLBAT_OPTION: list[tuple] = [(By.CSS_SELECTOR, "ul[class='vnav vnav--horizontal vnav--level1']"),
                                    (By.CSS_SELECTOR, "a[href*='Small-And-Specialty']")]
    DRONES_OPTIONS: list[tuple] = [(By.CSS_SELECTOR, "li[class='vnav__item expanded']"),
                                   (By.CSS_SELECTOR, "ul[class='vnav vnav__subnav vnav--level2']"),
                                   (By.CSS_SELECTOR, "a[href*='Drones']")]
    PRODUCT_OPTIONS: list[tuple] = [(By.CLASS_NAME, "v-product-grid")]
    ADD_TO_CART: list[tuple] = [(By.ID, "btn_addtocart")]
    CART_COUNT: list[tuple] = [(By.CSS_SELECTOR,"span[class='cart__count'")]
    ONLINE_STORE_LOGO: list[tuple] = [(By.ID, "display_homepage_title"),]

    def go_to_shipping_page(self):
        self.click_on(self.SHIPPINGLINK)
        return ShippingPage(self.driver)

    def go_to_home_page(self,context):
        self.click_on(self.HOMESITELINK)
        return context['home_page']

    def go_to_small_batteries_option(self):
        self.scroll_and_click(self.SMALLBAT_OPTION)
        return self

    def go_to_drones_option(self):
        self.click_on(self.DRONES_OPTIONS)
        return self

    def go_to_product_option(self, product_title):
        self.scroll_and_click(self.PRODUCT_OPTIONS, self.select_a_by_title(product_title))
        return self

    @property
    def cart_count(self):
        return self.get_textcontent(self.CART_COUNT)
    @property
    def online_store_logo(self):
        return self.wait_for_visible_element_by(self.ONLINE_STORE_LOGO)

    def add_product_to_cart(self, product_title):
        self.go_to_product_option(product_title)
        self.click_on(self.ADD_TO_CART)
        return CartPopup(self.driver)

    def goback(self):
        self.driver.execute_script("window.history.go(-1)")
        return self


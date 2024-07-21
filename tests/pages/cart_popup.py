from tests.pages.base_page import BasePage
from tests.pages.cart_page import CartPage

import time
from selenium.webdriver.common.by import By


class CartPopup(BasePage):

    RECENT_PRICE: list[tuple] = [
        (By.CSS_SELECTOR, "div[class='soft_add_wrapper anchored']"),
        (By.CSS_SELECTOR, "div[class='soft_add_content_area']"),
        (By.CSS_SELECTOR, "li[class='product-row recently-added']"),
        (By.CSS_SELECTOR, "div[class='product-price price']")
    ]
    RECENT_QTY: list[tuple] = [
        (By.CSS_SELECTOR, "div[class='soft_add_wrapper anchored']"),
        (By.CSS_SELECTOR, "div[class='soft_add_content_area']"),
        (By.CSS_SELECTOR, "li[class='product-row recently-added']"),
        (By.CSS_SELECTOR, "div[class='product-detail']"),
        (By.CSS_SELECTOR, "div[class='product-qty quantity']")
    ]
    RECENT_DESC: list[tuple] = [
        (By.CSS_SELECTOR, "div[class='soft_add_wrapper anchored']"),
        (By.CSS_SELECTOR, "div[class='soft_add_content_area']"),
        (By.CSS_SELECTOR, "li[class='product-row recently-added']"),
        (By.CSS_SELECTOR, "div[class='product-detail']"),
        (By.CSS_SELECTOR, "div[class='product-name description']")
    ]
    RECENT_REMOVE: list[tuple] = [
        (By.CSS_SELECTOR, "div[class='soft_add_wrapper anchored']"),
        (By.CSS_SELECTOR, "div[class='soft_add_content_area']"),
        (By.CSS_SELECTOR, "li[class='product-row recently-added']"),
        (By.CSS_SELECTOR, "div[class='product-remove remove']"),
        (By.TAG_NAME, "a")
    ]
    CONTINUE_BTN: list[tuple] = [
        (By.CSS_SELECTOR, "div[class='soft_add_wrapper anchored']"),
        (By.CSS_SELECTOR, "div[class='soft_add_action_area']"),
        (By.CSS_SELECTOR, "a[class='continue_shopping']")
    ]
    VIEWCART: list[tuple] = [
        (By.CSS_SELECTOR, "div[class='soft_add_wrapper anchored']"),
        (By.CSS_SELECTOR, "div[class='soft_add_action_area']"),
        (By.CSS_SELECTOR, "a[class='check_out']")
    ]

    @property
    def get_item_name(self):
        recent_desc = self.wait_for_clickable_element_by(self.RECENT_DESC)
        self.mouseover(recent_desc)
        return recent_desc.get_property('textContent')

    @property
    def get_item_price(self):
        return float(self.get_textcontent(self.RECENT_PRICE).replace('$', ''))

    @property
    def get_item_qty(self):
        return self.get_textcontent(self.RECENT_QTY)

    def remove_product(self,context):
        self.click_on(self.RECENT_REMOVE)
        time.sleep(2)
        return context['store_page']


    def continue_shopping(self,context):
        self.mouseover(self.CONTINUE_BTN)
        self.click_on(self.CONTINUE_BTN)
        return context['store_page']


    def go_to_cart(self):
        self.click_on(self.VIEWCART)
        return CartPage(self.driver)

    def print_info(self):
        print("\nDESC: " + self.get_item_name)
        print("\nPRICE: " + self.get_item_price)
        print("\nQTY: " + self.get_item_qty)
        return self

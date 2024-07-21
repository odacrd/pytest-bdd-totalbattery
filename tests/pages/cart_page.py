from tests.pages.base_page import BasePage
from tests.pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CartPage(BasePage):
    CART_H2: list[tuple] = [(By.TAG_NAME, "h2")]
    CART_TABLE: list[tuple] = [(By.ID, "v65-cart-table")]
    CART_ROWS: list[tuple] = [(By.CSS_SELECTOR, "tr[class='v65-cart-details-row']")]
    CART_TOTAL: list[tuple] = [(By.CSS_SELECTOR, "table[id='v65-cart-table']"),
                               (By.CSS_SELECTOR, "tr[class='v65-cart-total-estimate-row']"),
                               (By.CSS_SELECTOR, "td[id='v65-cart-total-estimate-parent-cell']"),
                               (By.CSS_SELECTOR, "td[id='v65-cart-total-estimate-cell']")]
    CART_CHECKOUTBTN: list[tuple] = [(By.ID,"newSecureCheckoutBtn")]
    @property
    def header_text(self):
        return self.get_textcontent(self.CART_H2)

    @property
    def number_cart_rows(self):
        table: WebElement = self.wait_for_clickable_element_by(self.CART_TABLE)
        rows = self.find_elements_by(self.CART_ROWS, table)
        return len(rows)

    @property
    def cart_total(self):
        return (self.get_textcontent(self.CART_TOTAL)).strip().replace('$', '')

    def proceed_to_checkout(self):
        self.click_on(self.CART_CHECKOUTBTN)
        return CheckoutPage(self.driver)

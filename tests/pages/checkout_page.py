from tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CheckoutPage(BasePage):

    CHECKOUT_SUBTOTAL: list[tuple] = [(By.CSS_SELECTOR, "div[data-testid='carttotalsummaryitem-content'] span[class='float-right']")]
    CHECKOUT_EMAIL: list[tuple] = [(By.ID,"emailAddress")]
    CHECKOUT_FIRSTNAME: list[tuple] = [(By.ID, "firstName")]
    CHECKOUT_LASTNAME: list[tuple] = [(By.ID, "lastName")]
    CHECKOUT_ADDRESS: list[tuple] = [(By.ID, "address1")]
    CHECKOUT_CITY: list[tuple] = [(By.ID, "city")]
    CHECKOUT_COUNTRY: list[tuple] = [(By.ID,"country")]
    CHECKOUT_ZIP: list[tuple] = [(By.ID,"postalCode")]
    CHECKOUT_STATE: list[tuple] = [(By.ID, "state")]
    CHECKOUT_PHONE: list[tuple] = [(By.ID, "phoneNumber")]
    CHECKOUT_CONTINUE: list[tuple]=[(By.CSS_SELECTOR,"button[data-testid='address-form-submit-button']")]
    CHECKOUT_ERROR: list[tuple]=[(By.CSS_SELECTOR,"div[data-testid='formerrorlabel-input']>ul>li")]
    CHECKOUT_PAYMENT: list[tuple]=[(By.CSS_SELECTOR,"span[data-testid='buttontext-input']")]
    CHECKOUT_TOTALPAY: list[tuple] = [(By.CSS_SELECTOR, "button[data-testid='button-input'] span[data-testid='buttontext-input']")]

    @property
    def checkout_subtotal(self):
        return (self.get_textcontent(self.CHECKOUT_SUBTOTAL)).strip().replace('$', '')

    @property
    def checkout_pay(self):
        self.scroll_to_locator(self.CHECKOUT_TOTALPAY)
        return (self.get_textcontent(self.CHECKOUT_TOTALPAY)).strip().replace('Pay $', '')

    def enter_required(self):
        self.enter_text(self.CHECKOUT_EMAIL,"john.doe@test.ca")
        self.enter_text(self.CHECKOUT_FIRSTNAME, "john")
        self.enter_text(self.CHECKOUT_LASTNAME, "doe")
        self.enter_text(self.CHECKOUT_ADDRESS, "2984 Drew Drive")
        self.enter_text(self.CHECKOUT_CITY, "South Mountain")
        self.xselect(self.CHECKOUT_COUNTRY,"Canada")
        self.xselect(self.CHECKOUT_STATE, "Ontario")
        self.enter_text(self.CHECKOUT_ZIP,"k0e 1w0")

    def click_Continue(self):
        self.scroll_and_click(self.CHECKOUT_CONTINUE)

    @property
    def error_msg(self):
        self.scroll_to_locator(self.CHECKOUT_ERROR)
        return self.get_textcontent(self.CHECKOUT_ERROR)

    def enter_missing_phone_number(self):
        self.enter_text(self.CHECKOUT_PHONE,"613 732 8085")


    @property
    def continue_payment_btn(self):
        xElements = self.find_elements_by(self.CHECKOUT_PAYMENT)
        if len(xElements) > 0:
            return xElements[0]
        else:
            return None

    def continue_payment_btn_displayed(self):
        if self.continue_payment_btn is not None:
            return self.continue_payment_btn.is_displayed()
        else:
            return False
    def click_continue_payment_btn(self):
        self.scroll_and_click(self.CHECKOUT_PAYMENT)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from config.definitions import ROOT_URL
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time


class BasePage():
    def __init__(self, driver, base_url=ROOT_URL):
        self.base_url = base_url
        self.driver = driver

    def wait_for_clickable_element_by(self, tuples1: list[tuple], tuples2: list[tuple] = None):
        tuples: list[tuple]
        if tuples2 is None:
            tuples = tuples1
        else:
            tuples = tuples1 + tuples2
        xElement: WebElement = (WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(tuples[0])))
        for i in range(1, len(tuples)):
            xElement = xElement.find_element(tuples[i][0], tuples[i][1])
        return xElement

    def wait_for_visible_element_by(self, tuples1: list[tuple], tuples2: list[tuple] = None):
        tuples: list[tuple]
        if tuples2 is None:
            tuples = tuples1
        else:
            tuples = tuples1 + tuples2
        xElement: WebElement = (WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(tuples[0])))
        for i in range(1, len(tuples)):
            xElement = xElement.find_element(tuples[i][0], tuples[i][1])
        return xElement
    def find_elements_by(self, tuples: list[tuple], xelement: WebElement = None):
        if xelement is not None:
            xElements = xelement.find_elements(tuples[0][0], tuples[0][1])
        else:
            xElements = self.driver.find_elements(tuples[0][0], tuples[0][1])
        return xElements

    def wait_for_element_not_exists(self, tuple: list[tuple], timeout=1):
        start = time.time()

        notexist = "false"
        while len(self.driver.find_elements(tuple[0][0], tuple[0][1])) > 0 and time.time() - start < timeout:
            print("\ntimer: " + str(time.time() - start))
            time.sleep(1)
        if len(self.driver.find_elements(tuple[0][0], tuple[0][1])) == 0:
            notexist = "true"
        return notexist

    def scroll_and_click(self, ltuple1: list[tuple], ltuple2: list[tuple] = None):
        if ltuple2 is None:
            xelement: WebElement = self.wait_for_clickable_element_by(ltuple1)
        else:
            xelement: WebElement = self.wait_for_clickable_element_by(ltuple1, ltuple2)
        self.driver.execute_script("arguments[0].scrollIntoView();", xelement)
        time.sleep(2)
        xelement.click()

    def scroll_and_click_locator(self, ltuple: list[tuple]):
        xelement: WebElement = self.wait_for_clickable_element_by(ltuple)
        self.driver.execute_script("arguments[0].scrollIntoView();", xelement)
        time.sleep(2)
        xelement.click()

    def select_a_by_title(self, product_title):
        anchortuple: list[tuple] = [(By.CSS_SELECTOR, "a[title='" + product_title + "']")]
        return anchortuple

    def mouseover(self, tup: list[tuple]):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.wait_for_visible_element_by(tup)).perform()

    def click_on(self, tup: list[tuple]):
        self.wait_for_clickable_element_by(tup).click()

    def get_textcontent(self, tup: list[tuple]):
        self.wait_for_visible_element_by(tup)
        xElement: WebElement = self.wait_for_visible_element_by(tup)
        return self.wait_for_element_hasText(tup).get_property("textContent")

    def enter_text(self, tup: list[tuple], xvalue):
        self.wait_for_clickable_element_by(tup).send_keys(xvalue)

    def wait_for_element_hasText(self, tup: list[tuple]):
        target_element = self.xwait(5).until(lambda x: self.element_has_text(tup))
        return target_element

    def element_has_text(self, tup: list[tuple]):
        target_element = self.wait_for_visible_element_by(tup)
        if len(target_element.text.strip()) > 0:
            return target_element
        else:
            return False

    def xwait(self,xsec):
        return (WebDriverWait(self.driver, xsec))

    def xselect(self,ltup: list[tuple],optiontext):
        select = Select(WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(ltup[0])))
        select.select_by_visible_text(optiontext)

    def scroll_to_locator(self, ltuple: list[tuple]):
        xelement: WebElement = self.wait_for_visible_element_by(ltuple)
        self.driver.execute_script("arguments[0].scrollIntoView();", xelement)
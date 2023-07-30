from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException
from math import log, sin
from selenium.webdriver.support.wait import WebDriverWait
from .locators import ProductPageLocators, BasePageLocators, BasketPageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_message_total_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Message basket total is not " \
                                                                                   "presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No price of product in the message"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

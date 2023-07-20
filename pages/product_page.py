from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def push_button_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def get_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), "No message about adding product"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert product_name == product_name_message, "Product name does not match the message"

    def get_message_total_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Message basket total is not " \
                                                                                   "presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No price of product in the message"

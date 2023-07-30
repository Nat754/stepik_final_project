from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def can_see_message_about_empty_basket(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert basket_message == "Your basket is empty. Continue shopping", f"The message is: '{basket_message}'"

    def there_is_not_any_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), "There is some product in the basket"

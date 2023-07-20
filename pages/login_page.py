from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert "login" in url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_EMAIL), "Login input email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_PASSWORD), "Login input password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON_LOGIN), "Login button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_EMAIL), "Register input email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD), "Register input password is not " \
                                                                                    "presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD_CONFIRM), "Register input password " \
                                                                                            "is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON_REGISTER), "Register button is not presented"
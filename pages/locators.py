from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "registration_link")


class LoginPageLocators:
    LOGIN_INPUT_EMAIL = (By.ID, "id_login-username")
    LOGIN_INPUT_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON_LOGIN = (By.NAME, "login_submit")
    REGISTER_INPUT_EMAIL = (By.ID, "id_registration-email")
    REGISTER_INPUT_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_INPUT_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON_REGISTER = (By.NAME, "registration_submit")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, "h2.col-sm-6.h3")

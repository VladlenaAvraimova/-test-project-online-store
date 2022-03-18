from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators(object):
    BASKET_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    
class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    PASSWORD_FIELD1 = (By.ID, "id_registration-password1")
    PASSWORD_FIELD2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_FIELD = (By.ID, "id_registration-email")
    REGISTER_FORM = (By.ID, "register_form")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class ProductPageLocators(object):
    ADD_TO_BASKET = (By.XPATH, "//button [text()='Add to basket']")
    DISAPPEARED_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-warning.fade.in")
    NAME_OF_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    NAME_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div > strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")

class CartPageLocators(object):
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")
    ITEM_TITLE = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
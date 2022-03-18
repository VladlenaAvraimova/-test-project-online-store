from .locators import MainPageLocators
from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*CartPageLocators.BASKET_EMPTY_MESSAGE), "Message about empty basket isn't present"

    def should_not_be_title_item(self):
        assert self.is_not_element_present(*CartPageLocators.ITEM_TITLE), \
        "List item is presented, but should not be"
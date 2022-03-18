from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage): 
    def add_to_basket(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        product_link.click()

    def should_be_message_about_add_item_to_basket(self):
        name_of_book_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET)
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        assert name_of_book_in_basket.text == name_of_book.text, "Name isn't correct"

    def should_be_correct_price(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        price_book_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_BASKET)
        assert price_book.text == price_book_in_basket.text, "Price isn't correct"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def should_disappeared_messages_in_basket(self):
        assert self.should_disappeared_messages_in_basket(*ProductPageLocators.DISAPPEARED_MESSAGE), \
        "Message is should be disappeared, but it don't"

from .base import BasePageElement
from locators.account import AccountLocators


class AccountElements(BasePageElement):

    def __init__(self):
        super().__init__()
        self.address_book_link = self.driver.find_element(*AccountLocators.ADDRESS_BOOK_LINK)
        self.edit_account_link = self.driver.find_element(*AccountLocators.EDIT_ACCOUNT_LINK)

    def open_address_book_page(self):
        if self.driver.current_url.endswith("account/address"):
            return
        return self.address_book_link.click()

    def open_user_edit_page(self):
        return self.edit_account_link.click()
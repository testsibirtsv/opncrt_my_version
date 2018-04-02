"""
Contains AddressBookAssistant class that provides help with
interacting with the Address Book page elements.
"""

import re
from typing import List
from selenium.webdriver.support.ui import Select
from pages.base import BasePage
from elements.addressbook_11111 import AddressBookElements


class AddressBookPage(BasePage):
    """Used to work with the Address Book page."""

    def __init__(self):
        super().__init__()
        self.addr = AddressBookElements()

        self.addr.continue_btn

    def create(self, address):
        """
        Open Address Book page, then open and fill Add Address form
        and submit creation.

        :param address: object with parameters for fields in Add Address form.
        """
        self.open_address_book_page()
        self.open_form_page()
        self.fill_address_form(address)
        self.get_continue_button().click()





    def open_address_book_page(self):
        """
        Open Address Book page.

        :return: None if we still on Address Book page.
        """
        driver = self.conf.driver
        if driver.current_url.endswith("account/address"):
            return
        driver.find_element_by_link_text("Address Book").click()





from .base import BasePageElement
from locators.addressbook import AddressBookLocators


class AddressBookElements(BasePageElement):

    def __init__(self):
        super().__init__()
        self.alert_message = self.driver.find_element(*AddressBookLocators.ALERT_MESSAGE)
        self.edit_btn_list = self.driver.find_elements(*AddressBookLocators.EDIT_BUTTONS_LIST)
        self.content_list = self.driver.find_elements(*AddressBookLocators.CONTENT_LIST)
        self.delete_btn_list = self.driver.find_elements(*AddressBookLocators.CONTENT_LIST)
        self.edit_btn = self.driver.find_element(*AddressBookLocators.EDIT_BUTTON)
        self.delete_btn = self.driver.find_element(*AddressBookLocators.DELETE_BUTTON)
        self.new_address_btn = self.driver.find_element(*AddressBookLocators.NEW_ADDRESS_BUTTON)

    def get_alert_message_text(self):
        """
        Receive a message from the address book after adding,
        editing or deleting a record.
        """
        return self.alert_message.text

    def records_count(self):
        """
        Count the number of address records on the Address Book page.

        """
        return len(self.edit_btn_list)

    def open_edit_page_by_position(self, position):
        """
        Edit address book entry from the Address Book page
        by it's positional index.

        :param position: positional index of address entry
        in list of addresses on the Address Book page.
        """
        self.edit_btn_list[position].click()

    def delete_record_by_index(self, index):
        """
        Delete Address Book entry from Address Book page
        by it's positional index.

        :param index: positional index of address entry
        in list of addresses on Address Book page.
        """
        self.delete_btn_list[index].click()

    def open_form_page(self):
        """
        Open Add Address form o
        n Address Book page.
        """
        self.new_address_btn.click()

from pages.base import BasePage
from elements.addressbook import AddressBookElements
from elements.account import AccountElements
from models.addressbook import AddressBook
import re


class AddressBookPage(BasePage):

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

    def edit_record_by_index(self, updated_values, index: int):
        """
        Open Address Book page, then open already existing address entry,
        fill Add Address form with new data and submit changes.

        :param updated_values: object with parameters for fields in Add Address form.
        :param index: position of address in list on Address Book page.
        """

        self.open_address_book_page()
        self.open_edit_page_by_position(index)
        self.fill_address_form(updated_values)
        self.get_continue_button_from_form().click()

    def get_content_info_from_list(self):
        """
        Get text of each individual address record in table on the Address Book page,
        filter and convert it into object, append them to list and return it.

        :return: list of objects.
        """
        self.open_address_book_page()
        address_list = []
        for line in self.get_content_list():
            content = re.sub(r'\s', '', line.text)
            address_list.append(AddressBook(content=content))
        return address_list

    def get_content_info_from_form(self, address_obj):
        """
        Get text from object, filter and convert it into another object.

        :param address_obj: object that we used to create/edit Add Address form.
        :return: object with filtered text.
        """
        self.open_address_book_page()
        info_from_object = []
        for attr in address_obj.__dict__.items():
            if attr[1] is not None:
                info_from_object.append(attr[1])
        content = re.sub(r'\s', '', "".join(info_from_object))
        return AddressBook(content=content)

    def get_content_info_by_index(self, index):
        """
        Get text from address record  by index in table on the Address Book page,
        filter and convert it into object.

        :return: object.
        """
        self.open_address_book_page()
        info = self.get_content_list()[index].text
        content = re.sub(r'\s', '', info)
        return AddressBook(content=content)

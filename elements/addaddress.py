from .base import BasePageElement
from selenium.webdriver.support.ui import Select
from locators.addaddress import AddAddressLocators


class AddAddressElements(BasePageElement):

    def __init__(self):
        super().__init__()
        self.firstname_error = self.driver.find_element(*AddAddressLocators.FIRSTNAME_ERROR)
        self.lastname_error = self.driver.find_element(*AddAddressLocators.LASTNAME_ERROR)
        self.address1_error = self.driver.find_element(*AddAddressLocators.ADDRESS1_ERROR)
        self.city_error = self.driver.find_element(*AddAddressLocators.CITY_ERROR)
        self.postcode_error = self.driver.find_element(*AddAddressLocators.POSTCODE_ERROR)
        self.region_error = self.driver.find_element(*AddAddressLocators.REGION_ERROR)
        self.firstname_field = self.driver.find_element(*AddAddressLocators.FIRSTNAME_FIELD)
        self.lastname_field = self.driver.find_element(*AddAddressLocators.LASTNAME_FIELD)
        self.company_field = self.driver.find_element(*AddAddressLocators.COMPANY_FIELD)
        self.address1_field = self.driver.find_element(*AddAddressLocators.ADDRESS1_FIELD)
        self.address2_field = self.driver.find_element(*AddAddressLocators.ADDRESS2_FIELD)
        self.city_field = self.driver.find_element(*AddAddressLocators.CITY_FIELD)
        self.postcode_field = self.driver.find_element(*AddAddressLocators.POSTCODE_FIELD)
        self.country_option = self.driver.find_element(*AddAddressLocators.COUNTRY_OPTION)
        self.region_option = self.driver.find_element(*AddAddressLocators.REGION_OPTION)
        self.continue_btn = self.driver.find_element(*AddAddressLocators.CONTINUE_BUTTON)

    def fill_address_form(self, address):
        """
        Fill fields with data in Add Address form.

        :param address: object with parameters for fields.
        """
        self.change_text_field_data(self.firstname_field, address.first_name)
        self.change_text_field_data(self.lastname_field, address.last_name)
        self.change_text_field_data(self.company_field, address.company)
        self.change_text_field_data(self.address1_field, address.address_1)
        self.change_text_field_data(self.address2_field, address.address_2)
        self.change_text_field_data(self.city_field, address.city)
        self.change_text_field_data(self.postcode_field, address.post_code)
        self.change_drop_list_data(self.country_option, address.country)
        self.change_drop_list_data(self.region_option, address.region_state)

    @staticmethod
    def change_drop_list_data(ddlist_option, value):
        """
        Select option in dropdown list in Add Address form.

        :param ddlist_option: option's id in dropdown list.
        :param value: option's text in dropdown list.
        """
        if value is not None:
            data_select = Select(ddlist_option)
            data_select.select_by_visible_text(value)

    @staticmethod
    def change_text_field_data(field_name, value):
        """
        Set text into Add Address form field.

        :param field_name: field's id in Add Address form.
        :param value: field's text in Add Address form.
        """
        if value is not None:
            field_name.click()
            field_name.clear()
            field_name.send_keys(value)

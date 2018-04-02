from .base import BasePageElement
from locators.editaccount import EditAccountLocators


class EditAccountElements(BasePageElement):

    def __init__(self):
        super().__init__()
        self.continue_btn = self.driver.find_element(*EditAccountLocators.CONTINUE_BUTTON)
        self.firstname_field = self.driver.find_element(*EditAccountLocators.FIRSTNAME_FIELD)
        self.lastname_field = self.driver.find_element(*EditAccountLocators.LASTNAME_FIELD)
        self.email_field = self.driver.find_element(*EditAccountLocators.EMAIL_FIELD)
        self.telephone_field = self.driver.find_element(*EditAccountLocators.TELEPHONE_FIELD)

    @staticmethod
    def change_data_in_text_fields(form_field, data):
        """
        Enter the data in the textfield.

        :param form_field: textfield's id.
        :param data: data entered in the textfield.
        """
        if data is not None:
            form_field.click()
            form_field.clear()
            form_field.send_keys(data)

    def fill_edit_account_form(self, user_data):
        """
        Change user data in the Edit Account form.

        :param user_data: data entered in the textfield.
        """
        self.change_data_in_text_fields(self.firstname_field, user_data.first_name)
        self.change_data_in_text_fields(self.lastname_field, user_data.last_name)
        self.change_data_in_text_fields(self.email_field, user_data.email)
        self.change_data_in_text_fields(self.telephone_field, user_data.telephone)
        self.continue_btn.click()

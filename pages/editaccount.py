from pages.base import BasePage
from elements.editaccount import EditAccountElements
from elements.account import AccountElements


class EditAccountPage(BasePage):

    def edit(self):
        open_user_edit_page()
        fill_edit_account_form()
        self.continue_btn.click()
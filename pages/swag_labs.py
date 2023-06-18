from selenium.common.exceptions import NoSuchFrameException
from pages.base_page import BasePage


class SwagLabs(BasePage):
    def exist_logo(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchFrameException:
            return False
        return True

    def exist_username(self):
        try:
            self.find_element(locator='#login_button_container > div > form > div:nth-child(1)')
        except NoSuchFrameException:
            return False
        return True

    def exist_password(self):
        try:
            self.find_element(locator='#login_button_container > div > form > div:nth-child(2)')
        except NoSuchFrameException:
            return False
        return True

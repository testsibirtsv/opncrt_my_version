"""
TODO
"""
from selenium.webdriver.common.by import By
from locators.base import BasePageLocators

# pylint: disable=too-few-public-methods
class HomePageLocators(BasePageLocators):
    """
    TODO
    """
    COMPONENTS_TAB = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/a')
    SHOPPING_CART_TAB = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')
    MONITORS = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[2]/a')
    PHONES = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[6]/a')

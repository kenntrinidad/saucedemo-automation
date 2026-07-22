from playwright.sync_api import Page

from config import BTN_CHECKOUT


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def checkout(self) -> None:
        self.page.locator(BTN_CHECKOUT).click()

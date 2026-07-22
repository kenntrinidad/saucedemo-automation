from playwright.sync_api import Page

from config import INVENTORY_ITEMS, BTN_ADD_TO_CART_BACKPACK, CART_BADGE, CART_LINK


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def product_count(self) -> int:
        return self.page.locator(INVENTORY_ITEMS).count()

    def add_backpack_to_cart(self) -> None:
        self.page.locator(BTN_ADD_TO_CART_BACKPACK).click()

    def cart_badge(self):
        return self.page.locator(CART_BADGE)

    def go_to_cart(self) -> None:
        self.page.locator(CART_LINK).click()

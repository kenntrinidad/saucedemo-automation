from playwright.sync_api import Page

from config import (
    FLD_FIRSTNAME,
    FLD_LASTNAME,
    FLD_POSTALCODE,
    BTN_CONTINUE,
    BTN_FINISH,
    TXT_COMPLETE_HEADER,
)


class CheckoutStepOnePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.page.locator(FLD_FIRSTNAME).fill(first_name)
        self.page.locator(FLD_LASTNAME).fill(last_name)
        self.page.locator(FLD_POSTALCODE).fill(postal_code)
        self.page.locator(BTN_CONTINUE).click()


class CheckoutOverviewPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def finish(self) -> None:
        self.page.locator(BTN_FINISH).click()

    def confirmation_header(self):
        return self.page.locator(TXT_COMPLETE_HEADER)

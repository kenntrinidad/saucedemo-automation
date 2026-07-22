from playwright.sync_api import Page

from config import URL, FLD_USERNAME, FLD_PASSWORD, BTN_LOGIN, TXT_ERROR


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self) -> None:
        self.page.goto(URL)

    def login(self, username: str, password: str) -> None:
        self.page.locator(FLD_USERNAME).fill(username)
        self.page.locator(FLD_PASSWORD).fill(password)
        self.page.locator(BTN_LOGIN).click()

    def error_message(self):
        return self.page.locator(TXT_ERROR)

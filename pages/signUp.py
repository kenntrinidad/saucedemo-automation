from auto_ex_config import *
from playwright.sync_api import Page

def signup(page: Page) -> None:
    #page.wait_for_selector(LINK_SIGNUP)
    page.locator(LINK_SIGNUP).click()
    #expect(page).to_have_title(PAGE_TITLE)
    print(page.title())
    page.locator(SIGNUP_NAME).fill(NAME)
    page.wait_for_timeout(2000)
    page.locator(SIGNUP_EMAIL).fill(EMAIL)
    page.wait_for_timeout(2000)
    page.locator(BTN_SIGNUP).click()
    page.wait_for_timeout(2000)
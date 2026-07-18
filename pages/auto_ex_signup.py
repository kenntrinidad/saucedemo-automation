from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page, expect, TimeoutError as PlaywrightTimeoutError
import os
from typing import Tuple, Optional
from auto_ex_config import *

def launch_browser() -> Tuple[Playwright, Browser, BrowserContext, Page]:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    browsercontext = browser.new_context()
    page = browser.new_page()
    print("Browser Launched")
    page.wait_for_timeout(3000)
    return playwright, browser, browsercontext, page

def open_site(page: Page) -> None:
    page.goto(URL)
    print("Go to website")

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

    error_banner = page.get_by_text(ERROR_EMAIL_EXISTS_TEXT)

    try:
        error_banner.wait_for(state="visible", timeout =5_000)
        print(f"Sign Up Failed: account already exist for {EMAIL}")
    except PlaywrightTimeoutError:
        print(f"Sign Up form proceed")




if __name__ == "__main__":
    playwright, browser, browsercontext, page = launch_browser()
    open_site(page)
    signup(page)


    browser.close()
    playwright.stop()
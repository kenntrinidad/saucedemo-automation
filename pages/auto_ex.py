from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page
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


if __name__ == "__main__":
    playwright, browser, browsercontext, page = launch_browser()
    open_site(page)
    browser.close()
    playwright.stop()
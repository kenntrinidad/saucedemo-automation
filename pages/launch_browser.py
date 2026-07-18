from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page
from typing import Tuple


def launch_browser() -> Tuple[Playwright, Browser, BrowserContext, Page]:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    browsercontext = browser.new_context()
    page = browsercontext.new_page()
    print("Browser Launched")

    return playwright, browser, browsercontext, page


if __name__ == "__main__":
    launch_browser()
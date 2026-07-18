import os
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page
from typing import Optional, Tuple

LINK = "https://www.saucedemo.com/"

# This is working Open Browser
"""with sync_playwright() as p:
    browser: Browser = p.chromium.launch(headless=False) # Ito yun browser
    context: BrowserContext = browser.new_context() # Ito yung context ng browser
    page: Page = context.new_page() # Ito yung page na binuksan sa browser

    print("Browser opened successfully")
    page.goto(LINK)
    print("Browser is ready")
    print("Browser will stay open for 30 seconds")
    page.wait_for_timeout(30000)  # Wait for 5 seconds to ensure the page is fully loaded
    print("30 seconds have passed. Closing browser.")
    browser.close()"""

def launch_browser(
        headless: bool = False,
        slow_mo: int = 500,
) -> Tuple[Playwright, Browser, BrowserContext, Page]:
    playwright = sync_playwright().start()
    browser: Browser = playwright.chromium.launch(headless=False) # Ito yun browser
    context: BrowserContext = browser.new_context() # Ito yung context ng browser
    page: Page = context.new_page() # Ito yung page na binuksan sa browser

    print("Browser opened successfully")
    page.goto(LINK)
    print("Browser is ready")

    title = page.title()
    print(f"Page title: {title}")

    #page.wait_for_timeout(10000)  # Wait for 10 seconds to ensure the page is fully loaded
    return playwright, browser, context, page

def main():
    playwright, browser, context, page = launch_browser()
    #print("30 seconds have passed. Closing browser.")
    #page.wait_for_timeout(30000)  # Wait for 30 seconds before closing the browser

    context.close()
    browser.close()
    playwright.stop()
    print("Browser closed successfully")

if __name__ == "__main__":
    main()


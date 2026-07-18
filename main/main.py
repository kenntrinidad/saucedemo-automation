from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page, expect, TimeoutError as PlaywrightTimeoutError
from typing import Tuple, Optional
from config import *

EXPECTED_TITLE = "Swag Labs"

def launch_browser() -> Tuple[Playwright, Browser, BrowserContext, Page]:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    browsercontext = browser.new_context()
    page = browsercontext.new_page()
    print("Browser Launched")
    page.wait_for_timeout(3000)

    return playwright, browser, browsercontext, page

def navigate_url(page: Page):
    page.goto(URL)
    try:
        expect(page).to_have_title(EXPECTED_TITLE, timeout=5_000)
        print("Correct title - proceeding")
    
    except PlaywrightTimeoutError:
        print(f"Wrong title. Got {page.title()!r}), expected: {EXPECTED_TITLE!r}")

    #page.wait_for_timeout(3000)

def sign_in(page: Page):
    page.locator(FLD_USERNAME).fill(STANDARD_USERNAME)
    page.locator(FLD_PASSWORD).fill(PASSWORD)
    #page.wait_for_timeout(2000)
    page.locator(BTN_LOGIN).click()
    print("Successful Logged In")
    #page.wait_for_timeout(5000)

def add_to_cart(page: Page):
    page.locator("data-test=inventory-item-name").filter(
        has_text=ITEM_1
    ).click()
    print(f"'{ITEM_1} found and clicked'")
    #page.wait_for_timeout(3000)
    page.locator(BTN_ADDTOCART).click()
    print(f"'{ITEM_1} added in the cart")
    


    # Click Cart button

    page.locator(BTN_CART).click()
    print("Cart icon clicked")
    page.wait_for_timeout(1000)
    page.locator(BTN_CHECKOUT).click()
    print("Clicked Checkout Button")

    #input information
    page.locator(FLD_FIRSTNAME).fill(FIRSTNAME)
    page.wait_for_timeout(1000)
    page.locator(FLD_LASTNAME).fill(LASTNAME)
    page.wait_for_timeout(1000)
    page.locator(FLD_ZIPCODE).fill(ZIPCODE)
    page.locator(BTN_CONTINUE).click()
    print("Continue Button Clicked")
    page.wait_for_timeout(1000)
    page.locator(BTN_FINISH).click()
    page.wait_for_timeout(1000)
    print("Finish")



if __name__ == "__main__":
    playwright, browser, browsercontext, page = launch_browser()
    navigate_url(page)
    sign_in(page)
    add_to_cart(page)

    browsercontext.close()
    browser.close()
    playwright.stop()

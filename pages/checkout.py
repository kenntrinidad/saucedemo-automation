from playwright.sync_api import Page
from testcase1_signin_standarduser import testcase1
from launch_browser import launch_browser
from config import *


def add_to_cart(page: Page):
    page.locator("data-test=inventory-item-name").filter(
        has_text=ITEM_1
    ).click()
    print(f"'{ITEM_1} found and clicked'")
    page.wait_for_timeout(3000)
    page.locator(BTN_ADDTOCART).click()
    print(f"'{ITEM_1} added in the cart")
    


    # Click Cart button

    page.locator(BTN_CART).click()
    print("Cart icon clicked")
    page.wait_for_timeout(2000)
    page.locator(BTN_CHECKOUT).click()
    print("Clicked Checkout Button")

    #input information
    page.locator(FLD_FIRSTNAME).fill(FIRSTNAME)
    page.wait_for_timeout(2000)
    page.locator(FLD_LASTNAME).fill(LASTNAME)
    page.wait_for_timeout(2000)
    page.locator(FLD_ZIPCODE).fill(ZIPCODE)
    page.locator(BTN_CONTINUE).click()
    print("Continue Button Clicked")
    page.wait_for_timeout(3000)
    page.locator(BTN_FINISH).click()
    page.wait_for_timeout(5000)
    print("Finish")

if __name__ == "__main__":
    playwright, browser, browsercontext, page = launch_browser()
    testcase1(page)
    add_to_cart(page)

    browsercontext.close()
    browser.close()
    playwright.stop()
    
    

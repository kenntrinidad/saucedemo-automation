from config import *


def checkout(page):
    """playwright, browser, context, page = add_to_cart_all()"""
    page.wait_for_timeout(2000)
    page.locator(BTN_BASKET).click()
    print("Shopping cart button clicked.")

    page.wait_for_timeout(2000)
    page.locator(BTN_CHECKOUT).scroll_into_view_if_needed()
    page.locator(BTN_CHECKOUT).click()
    print("Checkout button clicked.")

    #Input Details
    page.locator(FIELD_FIRST_NAME).click()
    page.locator(FIELD_FIRST_NAME).press_sequentially(FIRST_NAME, delay=100)
    page.locator(FIELD_LAST_NAME).click()
    page.locator(FIELD_LAST_NAME).press_sequentially(LAST_NAME, delay=100)
    page.locator(FIELD_POSTAL_CODE).click()
    page.locator(FIELD_POSTAL_CODE).press_sequentially(POSTAL_CODE, delay=100)

    page.locator(BTN_CONTINUE).click()
    print("Continue button clicked.")

    page.wait_for_timeout(2000)
    page.locator(BTN_FINISH).click()
    print("Finish button clicked.")

    page.wait_for_timeout(2000)
    print("Checkout process completed successfully.")
    #return playwright, browser, context, page


"""def main():
    playwright, browser, context, page = checkout()
    page.wait_for_timeout(10000)

    context.close()
    browser.close()
    playwright.stop()

if __name__ == "__main__":
    main()"""
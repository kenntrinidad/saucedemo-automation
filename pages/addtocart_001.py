
from config import BTN_ADDTOCARD, BTN_BACKTOPRODUCTS, ITEM_1, ITEM_2, ITEM_3, ITEM_4, ITEM_5, ITEM_6



def add_to_cart_all(page):
    #playwright, browser, context, page = login()
    page.wait_for_timeout(2000)

    # Add to Cart ITEM_1
    page.locator("[data-test='inventory-item-name']").filter(
    has_text=ITEM_1
).click()
    print(f"'{ITEM_1}' selected.")
    page.wait_for_timeout(2000)
    page.locator(BTN_ADDTOCARD).click()
    print(f"'{ITEM_1}' added to cart.")
    page.wait_for_timeout(1000)
    page.locator(BTN_BACKTOPRODUCTS).click()
    print("Navigated back to products page.")
    page.wait_for_timeout(1000)

    # Add to Cart ITEM_2
    page.locator("[data-test='inventory-item-name']").filter(
    has_text=ITEM_2
).click()
    print(f"'{ITEM_2}' selected.")
    page.wait_for_timeout(2000)
    page.locator(BTN_ADDTOCARD).click()
    print(f"'{ITEM_2}' added to cart.")
    page.wait_for_timeout(1000)
    page.locator(BTN_BACKTOPRODUCTS).click()
    print("Navigated back to products page.")
    page.wait_for_timeout(1000)

    # Add to Cart ITEM_3
    page.locator("[data-test='inventory-item-name']").filter(
    has_text=ITEM_3
).click()
    print(f"'{ITEM_3}' selected.")
    page.wait_for_timeout(2000)
    page.locator(BTN_ADDTOCARD).click()
    print(f"'{ITEM_3}' added to cart.")
    page.wait_for_timeout(1000)
    page.locator(BTN_BACKTOPRODUCTS).click()
    print("Navigated back to products page.")
    page.wait_for_timeout(1000)

    # Add to Cart ITEM_4
    page.locator("[data-test='inventory-item-name']").filter(
    has_text=ITEM_4
).click()
    print(f"'{ITEM_4}' selected.")
    page.wait_for_timeout(2000)
    page.locator(BTN_ADDTOCARD).click()
    print(f"'{ITEM_4}' added to cart.")
    page.wait_for_timeout(1000)
    page.locator(BTN_BACKTOPRODUCTS).click()
    print("Navigated back to products page.")
    page.wait_for_timeout(1000)

    # Add to Cart ITEM_5
    page.locator("[data-test='inventory-item-name']").filter(
    has_text=ITEM_5
).click()
    print(f"'{ITEM_5}' selected.")
    page.wait_for_timeout(2000)
    page.locator(BTN_ADDTOCARD).click()
    print(f"'{ITEM_5}' added to cart.")
    page.wait_for_timeout(1000)
    page.locator(BTN_BACKTOPRODUCTS).click()
    print("Navigated back to products page.")
    page.wait_for_timeout(1000)

    # Add to Cart ITEM_6
    page.locator("[data-test='inventory-item-name']").filter(
    has_text=ITEM_6
).click()
    print(f"'{ITEM_6}' selected.")
    page.wait_for_timeout(2000)
    page.locator(BTN_ADDTOCARD).click()
    print(f"'{ITEM_6}' added to cart.")
    page.wait_for_timeout(1000)
    page.locator(BTN_BACKTOPRODUCTS).click()
    print("Navigated back to products page.")
    page.wait_for_timeout(1000)


    #return playwright, browser, context, page

"""def main():
    playwright, browser, context, page = add_to_cart_all()
    page.wait_for_timeout(10000)

    context.close()
    browser.close()
    playwright.stop()

if __name__ == "__main__":
    main()"""
import os
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page
from typing import Optional, Tuple

from openBrowser import launch_browser
from login_001 import login
from config import URL
from addtocart_001 import add_to_cart_all
from checkout_001 import checkout
#from login_swag import login
#from addtocart_all import add_to_cart_all
#from checkout import checkout


def main():

    # Step 1 - Open Browser
    playwright, browser, context, page = launch_browser(URL)

    print("Browser opened successfully")
    page.goto(URL)
    print("Browser is ready")
    print(f"Opened: {URL}")

    title = page.title()
    print(f"Page title: {title}")


    try:
        # Step 2 - Login
        login(page)
        print("login successful")
        page.wait_for_timeout(2000)  # Wait for 2 seconds to ensure the page is fully loaded
        #print("5 seconds have passed. Closing browser.")
        
        # Step 3 - Add all products
        add_to_cart_all(page)
        print("add to cart successful")
        page.wait_for_timeout(2000)  # Wait for 2 seconds to ensure the page is fully loaded
        print("5 seconds have passed. Closing browser.")

        checkout(page)
        print("checkout successful")
        page.wait_for_timeout(2000)  # Wait for 2 seconds to ensure the page is fully loaded
        print("5 seconds have passed. Closing browser.")



    finally:
        context.close()
        browser.close()
        playwright.stop()
        print("Browser closed successfully.")
        

    """try:
        # Step 2 - Login
        playwright, browser, context, page = login()

        # Step 3 - Add all products
        playwright, browser, context, page = add_to_cart_all()

        # Step 4 - Checkout
        playwright, browser, context, page = checkout()

        print("✅ Automation completed successfully.")

        page.wait_for_timeout(5000)

    finally:
        context.close()
        browser.close()
        playwright.stop()
        print("Browser closed successfully.")
    """

if __name__ == "__main__":
    main()
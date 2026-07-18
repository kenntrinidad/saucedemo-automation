from openBrowser import launch_browser
from login_swag import login

def add_to_cart():
    playwright, browser, context, page = login()

    page.locator("xpath=/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").click()
    print("Add to cart button clicked.")

    return playwright, browser, context, page

def main():
    playwright, browser, context, page = add_to_cart()
    page.wait_for_timeout(10000)

    context.close()
    browser.close()
    playwright.stop()

if __name__ == "__main__":
    main()
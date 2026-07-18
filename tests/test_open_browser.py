from pages.openBrowser import launch_browser

def test_open_browser():
    playwright, browser, context, page = launch_browser()

    try:
        # Verify the page title
        assert page.title() == "Swag Labs"

        # Verify the URL
        assert page.url == "https://www.google.com/"

        print("Browser launched successfully.")
        print(f"Title : {page.title()}")
        print(f"URL   : {page.url}")

    finally:
        context.close()
        browser.close()
        playwright.stop()
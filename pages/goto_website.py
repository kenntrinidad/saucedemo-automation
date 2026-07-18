from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://automationexercise.com/")

    expected_title = "Automation Exercise"

    actual_title = page.title()

    if actual_title == expected_title:
        print("Test Passed: The page title is correct.")
        print(f"Actual Title: {actual_title}")
    else:
        print("Test Failed: The page title is incorrect.")
        print(f"Expected Title: {expected_title}")
        print(f"Actual Title: {actual_title}")

        browser.close()



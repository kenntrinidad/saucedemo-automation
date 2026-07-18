from playwright.sync_api import Page, expect
from testcase1_signin_standarduser import testcase1

def test_signin(page: Page) -> None:
    testcase1(page)

# pytest automation_swag\test_signin.py
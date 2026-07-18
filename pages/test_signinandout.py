from playwright.sync_api import Page, expect
from testcase1_signin_standarduser import testcase1
from testcase2_logout import logout

def test_signin(page: Page) -> None:
    testcase1(page)

def test_logout(page: Page) -> None:
    logout(page)

# to execute base this pytest automation_swag\test_signinandout.py
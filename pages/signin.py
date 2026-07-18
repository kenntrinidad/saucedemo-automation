from playwright.sync_api import Page
from config import *

def signin(page: Page):
    page.locator(FLD_USERNAME).fill(STANDARD_USERNAME)
    page.wait_for_timeout(1000)
    page.locator(FLD_PASSWORD).fill(PASSWORD)
    page.wait_for_timeout(1000)
    page.locator(BTN_LOGIN).click()
    print("Success Logged in")
    page.wait_for_timeout(3000)



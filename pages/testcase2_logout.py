from testcase1_signin_standarduser import testcase1
from config import *
from playwright.sync_api import Page
from launch_browser import launch_browser
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page


def logout(page: Page) -> None:
    testcase1(page)

    page.locator(HAMBURGER).click()
    print("Clicked Hamburher Menu")
    page.wait_for_timeout(1000)
    page.locator(BTN_LOGOUT).click()
    print("Clicked Logout Button")
    print("Successfully Logged Out")

if __name__ == "__main__":
    playwright, browser, browsercontext, page = launch_browser()
    logout(page)
    
    browsercontext.close()
    browser.close()
    playwright.stop()
    
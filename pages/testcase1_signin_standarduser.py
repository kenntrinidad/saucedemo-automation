from playwright.sync_api import Page

from launch_browser import launch_browser
from navigate_url import navigate_url
from signin import signin


def testcase1(page: Page) -> None:
    navigate_url(page)
    signin(page)

   

if __name__ == "__main__":
    playwright, browser, browsercontext, page = launch_browser()
    testcase1(page)

    browsercontext.close()
    browser.close()
    playwright.stop()

    
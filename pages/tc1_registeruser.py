from launch_browser import launch_browser
from navigate_url import navigate_url
from signUp import signup


def registeruser():
    playwright, browser, browsercontext, page = launch_browser()
    print("Browser opened successfully")
    page.wait_for_timeout(2000)

    navigate_url(page)

    signup(page)

    
    
    browsercontext.close()
    browser.close()
    playwright.stop()


if __name__ == "__main__":
    registeruser()
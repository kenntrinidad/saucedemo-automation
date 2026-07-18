from pages.openBrowser import launch_browser
from pages.config import *
import pytest

LINK = (URL)

@pytest.fixture

def page():
    playwright, browser, context, page = launch_browser

    page.goto(LINK)

    yield page

    context.close()
    browser.close()
    playwright.stop()   



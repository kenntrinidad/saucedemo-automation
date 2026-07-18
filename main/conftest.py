import pytest

from main import *

@pytest.fixture
def page():
    playwright, browser, browsercontext, page = launch_browser()
    yield page

    browsercontext.close()
    browser.close()
    playwright.stop()

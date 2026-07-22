import pytest
from playwright.sync_api import Page

from launch_browser import launch_browser


@pytest.fixture
def page() -> Page:
    playwright, browser, browsercontext, page = launch_browser()
    yield page

    browsercontext.close()
    browser.close()
    playwright.stop()

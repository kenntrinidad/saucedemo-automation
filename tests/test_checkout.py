import pytest
import os
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page
from typing import Optional, Tuple

from pages.openBrowser import launch_browser
from pages.login_swag import login
from pages.addtocart_all import add_to_cart_all
from pages.checkout import checkout

@pytest.fixture
def test_checkout(page):
    launch_browser(page)
    login(page)
    add_to_cart_all(page)
    checkout(page)

    assert page.url.endswith("https://www.saucedemo.com/checkout-complete.html")

"""if __name__ == "__main__":
    main()"""
from playwright.sync_api import Page

from main import navigate_url, sign_in, add_to_cart


def test_navigate_to_site(page: Page) -> None:
    navigate_url(page)


def test_sign_in(page: Page) -> None:
    navigate_url(page)
    sign_in(page)


def test_add_to_cart(page: Page) -> None:
    navigate_url(page)
    sign_in(page)
    add_to_cart(page)


# pytest main\test_main.py -v
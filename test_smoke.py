

# Run with: pytest -m smoke -v

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutStepOnePage, CheckoutOverviewPage

from config import (
    STANDARD_USER,
    LOCKED_OUT_USER,
    PASSWORD,
    INVALID_PASSWORD,
    CHECKOUT_FIRSTNAME,
    CHECKOUT_LASTNAME,
    CHECKOUT_POSTALCODE,
)


@pytest.mark.smoke
def test_TC001_valid_login_lands_on_inventory(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(STANDARD_USER, PASSWORD)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.smoke
def test_TC002_invalid_password_shows_error(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(STANDARD_USER, INVALID_PASSWORD)

    expect(login_page.error_message()).to_be_visible()
    expect(login_page.error_message()).to_contain_text("do not match")


@pytest.mark.smoke
def test_TC007_locked_out_user_shows_error(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    expect(login_page.error_message()).to_be_visible()
    expect(login_page.error_message()).to_contain_text("locked out")
    # Should not proceed past login
    expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.smoke
def test_TC012_all_six_products_render(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(page)
    assert inventory_page.product_count() == 6


@pytest.mark.smoke
def test_TC017_add_single_item_updates_cart_badge(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()

    expect(inventory_page.cart_badge()).to_have_text("1")


@pytest.mark.smoke
def test_TC030_and_TC032_and_TC037_and_TC040_full_checkout_flow(page: Page) -> None:
    """
    Combines TC-030 (checkout proceeds), TC-032 (valid info proceeds to
    overview), TC-037 (overview reflects cart contents), and TC-040
    (finish completes the order) — these are sequential steps of one
    continuous flow, so they're covered together in a single smoke test.
    """
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.checkout()  # TC-030
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    checkout_step_one = CheckoutStepOnePage(page)
    checkout_step_one.fill_info(
        CHECKOUT_FIRSTNAME, CHECKOUT_LASTNAME, CHECKOUT_POSTALCODE
    )  # TC-032
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    # TC-037: at minimum, confirm the item we added appears in the overview
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

    checkout_overview = CheckoutOverviewPage(page)
    checkout_overview.finish()  # TC-040
    expect(checkout_overview.confirmation_header()).to_have_text(
        "THANK YOU FOR YOUR ORDER"
    )


@pytest.mark.smoke
def test_TC045_logout_redirects_to_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(STANDARD_USER, PASSWORD)

    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()

"""Centralized config: URL, test data, and locators for SauceDemo."""

URL = "https://www.saucedemo.com/"

# Test users (SauceDemo's documented standard test accounts)
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"
INVALID_PASSWORD = "wrong_password"

# --- Login page ---
FLD_USERNAME = "#user-name"
FLD_PASSWORD = "#password"
BTN_LOGIN = "#login-button"
TXT_ERROR = '[data-test="error"]'

# --- Inventory page ---
INVENTORY_ITEMS = ".inventory_item"
BTN_ADD_TO_CART_BACKPACK = '[data-test="add-to-cart-sauce-labs-backpack"]'
CART_BADGE = ".shopping_cart_badge"
CART_LINK = ".shopping_cart_link"

# --- Cart page ---
BTN_CHECKOUT = "#checkout"

# --- Checkout step one ---
FLD_FIRSTNAME = "#first-name"
FLD_LASTNAME = "#last-name"
FLD_POSTALCODE = "#postal-code"
BTN_CONTINUE = "#continue"

# --- Checkout overview ---
BTN_FINISH = "#finish"
TXT_COMPLETE_HEADER = ".complete-header"

# --- Menu ---
BTN_BURGER_MENU = "#react-burger-menu-btn"
LINK_LOGOUT = "#logout_sidebar_link"

# Sample checkout info
CHECKOUT_FIRSTNAME = "Kenn"
CHECKOUT_LASTNAME = "Trinidad"
CHECKOUT_POSTALCODE = "1600"

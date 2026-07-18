# SauceDemo Automation Suite

Test automation suite for [saucedemo.com](https://www.saucedemo.com/), built with **Playwright (Python)** and **pytest**, following the **Page Object Model (POM)** pattern.

This project covers the core user flows on SauceDemo — login, product browsing, cart management, and checkout — including negative-path and known-bug scenarios using SauceDemo's special test users (`locked_out_user`, `problem_user`, `performance_glitch_user`).

## Tech Stack

- **Python 3.10+**
- **Playwright** (sync API) — browser automation
- **pytest** + **pytest-playwright** — test framework and fixtures
- **python-dotenv** — environment/config management

## Features Covered

| Area | Coverage |
|---|---|
| Login | Valid/invalid credentials, locked-out user, empty fields, special test users |
| Inventory | Sorting, add/remove to cart, cart badge state |
| Product Detail | Data consistency with listing, add/remove from detail page |
| Cart | Item accuracy, removal, empty-cart edge case |
| Checkout | Form validation, order summary accuracy, order completion |
| Cross-cutting | Menu actions, logout, session/auth redirect, known UI bugs, performance |

Full test case list: [`SauceDemo_Test_Cases.xlsx`](./SauceDemo_Test_Cases.xlsx)

## Project Structure

```
automation_swag/
├── conftest.py             # pytest fixtures — browser/page setup and teardown
├── launch_browser.py         # launches Playwright browser, context, and page
├── navigate_url.py           # navigates to the target URL, verifies page title
├── signin.py                 # login flow
├── main.py                   # shared flow functions (navigate, sign in, add to cart)
├── config.py                  # locators, URLs, and test data constants
├── test_main.py               # pytest test cases
└── SauceDemo_Test_Cases.xlsx  # full manual test case documentation
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
playwright install
```

## Running Tests

```bash
pytest                          # run full suite
pytest test_main.py -v           # run a specific file, verbose output
pytest -k "login"                 # run tests matching a keyword
```

## Design Notes

- **Single source of browser truth** — only `launch_browser()` creates a `Browser`/`BrowserContext`/`Page`; every other function receives `page` as a parameter rather than launching its own. This keeps tests isolated and avoids orphaned browser processes.
- **Fixture-driven setup** — `conftest.py` handles browser launch and teardown automatically for any test requesting the `page` fixture, so individual test files stay focused on test logic.
- **Web-first assertions over hardcoded waits** — uses `expect(...).to_have_title(...)` and Playwright's built-in auto-waiting instead of fixed `time.sleep()`/`wait_for_timeout()` calls, for more reliable and faster test runs.
- **Independent, focused test cases** — each test covers one flow (navigate, sign in, checkout) so failures point directly to the broken step rather than requiring a full trace through a long combined test.

## Author

Rod Kenneth S. Trinidad — Senior QA Engineer & AI Automation Specialist
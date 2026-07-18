from playwright.async_api import Page
from config import *


def navigate_url(page: Page):
    page.goto(URL)
    print("Navigate to URL")

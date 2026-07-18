
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def login(page):
    #playwright, browser, context, page = launch_browser()


    page.locator("xpath=/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").click()
    page.locator("xpath=/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").press_sequentially(USERNAME, delay=100)
    print(f"Username '{USERNAME}' entered successfully.")
    
    page.locator("xpath=/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").click()
    page.locator("xpath=/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").press_sequentially(PASSWORD, delay=100)
    print(f"Password '{PASSWORD}' entered successfully.")
    page.locator("xpath=/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
    print("Login button clicked.")

    title = page.title()
    print(f"Page title: {title}")
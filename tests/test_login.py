
from playwright.sync_api import expect
from models.login_page import LoginPage

def test_user_can_login(page) -> None:
    login_page = LoginPage(page)

    login_page.navigate("https://www.saucedemo.com/")
    # We need to send just the credentials. The click on the Login button is handled in the login class method
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()


def test_incorrect_password(browser) -> None:
    # Create a context explicitly with NO storage state (empty)
    context = browser.new_context(storage_state=None)
    page = context.new_page()

    login_page = LoginPage(page)

    login_page.navigate("https://www.saucedemo.com/")
    login_page.login("standard_user", "wrong_password")

    expect(page.locator("[data-test='error']")).to_be_visible()
    expect(page.locator("[data-test='error']")).to_contain_text(
           "Username and password do not match any user in this service")

    # Close the error message
    login_page.error_button.click()
    expect(page.locator("[data-test='error']")).not_to_be_visible()

    # Clear the old password
    login_page.password_input.clear()
    expect(login_page.password_input).to_be_empty()



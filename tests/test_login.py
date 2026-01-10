import pytest
from playwright.sync_api import expect
from models.login_page import LoginPage
from data.users import test_users


def get_user_id(data):
    # This grabs the 'user' key from your dictionary to use as the label
    return f"{data['user']}"


# This ficture runs a loop in the background to read the dictionary file
@pytest.mark.parametrize("user_data", test_users, ids=get_user_id)
def test_login(browser, user_data) -> None:
    # Access data using dictionary syntax
    username = user_data["user"]
    password = user_data["password"]
    expected_outcome = user_data["result"]

    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")

    login_page.login(username, password)

    if expected_outcome == "success":
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.get_by_text("Products")).to_be_visible()
    else:
        expect(page.locator("[data-test='error']")).to_be_visible()
        expect(page.locator("[data-test='error']")).to_contain_text(expected_outcome)

        # Close the error message
        login_page.error_button.click()
        expect(page.locator("[data-test='error']")).not_to_be_visible()

        # Clear the old password
        login_page.password_input.clear()
        expect(login_page.password_input).to_be_empty()

    context.close()



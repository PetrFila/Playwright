import pytest
import os
from playwright.sync_api import BrowserType
from models.login_page import LoginPage

# Define where to save the cookies
STORAGE_STATE = "state.json"


@pytest.fixture(scope="session")
def global_login(browser_type: BrowserType):
    """
    1. Runs once per session.
    2. Logs in.
    3. Saves cookies to 'state.json'.
    """
    # We launch a separate browser just for this setup step
    browser = browser_type.launch()
    page = browser.new_page()

    # Use your existing Page Object!
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # THE MAGIC: Save the cookies/storage to disk
    page.context.storage_state(path=STORAGE_STATE)

    browser.close()
    return STORAGE_STATE


# This fixture overrides the default context creation
@pytest.fixture(scope="session")
def browser_context_args(global_login):
    """
    Tell Playwright: "Whenever you create a new browser context for a test,
    please load the cookies from this file."
    """
    return {
        "storage_state": global_login
    }
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Define locators for the login page so they can be reused
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")
        self.error_button = page.locator("[data-test='error-button']")

    # Define actions
    def navigate(self, url):
        # Website to navigate to
        self.page.goto(url)

    def login(self,username:str, password:str) -> None:
        # Actions to take on the login page
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

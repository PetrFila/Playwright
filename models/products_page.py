from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

        self.backpack_add_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.t_shirt_add_button = page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.shopping_cart_link = page.locator("[data-test='shopping-cart-link']")

    def click_add_item_to_cart(self, item):
        if item == "backpack":
            self.backpack_add_button.click()
        if item == "t_shirt":
            self.t_shirt_add_button.click()

    def click_shopping_cart_link(self):
        self.shopping_cart_link.click()
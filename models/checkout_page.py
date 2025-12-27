from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator("[class='cart_item']")
        self.inventory_name = page.locator("[data-test='inventory-item-name']")
        self.remove_button = page.get_by_role("button", name="Remove")
        self.continue_shopping_button = page.get_by_role("button", name="Go back Continue Shopping")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def get_items_count(self) -> int:
        return self.cart_items.count()

    def get_inventory_names(self) -> list[str]:
        return self.inventory_name.all_inner_texts()

    def click_remove_button(self):
       self.remove_button.click()

    def click_continue_shopping(self):
       self.continue_shopping_button.click()

    def click_checkout(self):
       self.checkout_button.click()

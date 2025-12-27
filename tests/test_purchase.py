from playwright.sync_api import expect
from models.products_page import ProductsPage


def add_product(page, click_shopping_cart_link = False):
    page.goto("https://www.saucedemo.com/inventory.html")
    product_page = ProductsPage(page)
    product_page.click_add_item_to_cart("backpack")
    if click_shopping_cart_link:
        product_page.click_shopping_cart_link()


# This uses the global_login fixture from the conftest.py file which Pytest automatically handles.
# There is no need to import anything.
def test_add_product(page):
    add_product(page)

    expect(page.locator("[data-test='remove-sauce-labs-backpack']")).to_contain_text("Remove")
    expect(page.locator("[data-test='shopping-cart-badge']")).to_be_visible()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")


def test_checkout_page(page):
    add_product(page, True)

    expect(page.locator("[data-test='title']")).to_have_text("Your Cart")

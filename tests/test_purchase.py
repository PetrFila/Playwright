from playwright.sync_api import expect
from models.products_page import ProductsPage

# This uses the logged_in_page fixture from the conftest.py file which Pytest automatically handles.
# There is no need to import anything.
def test_add_product(logged_in_page):
    page = logged_in_page
    product_page = ProductsPage(logged_in_page)
    product_page.click_add_item_to_cart("backpack")

    expect(page.locator("[data-test='remove-sauce-labs-backpack']")).to_contain_text("Remove")
    expect(page.locator("[data-test='shopping-cart-badge']")).to_be_visible()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text("1")


def test_checkout_page(logged_in_page):
    page = logged_in_page
    product_page = ProductsPage(logged_in_page)
    product_page.click_add_item_to_cart("backpack")
    product_page.click_shopping_cart_link()

    expect(page.locator("[data-test='title']")).to_have_text("Your Cart")




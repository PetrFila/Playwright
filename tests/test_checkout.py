from playwright.sync_api import expect

from models.products_page import ProductsPage
from models.checkout_page import CheckoutPage


def add_product(page):
    product_page = ProductsPage(page)
    product_page.click_add_item_to_cart("backpack")
    product_page.click_add_item_to_cart("t_shirt")
    product_page.click_shopping_cart_link()

# This uses the logged_in_page fixture from the conftest.py file which Pytest automatically handles.
# There is no need to import anything.
def test_checkout_page(logged_in_page):
    page = logged_in_page
    add_product(page)

    expect(page.locator("[data-test='title']")).to_have_text("Your Cart")

    cart_page = CheckoutPage(page)
    assert cart_page.get_items_count() == 2

    item_names = cart_page.get_inventory_names()
    assert "Sauce Labs Backpack" in item_names
    assert "Sauce Labs Bolt T-Shirt" in item_names
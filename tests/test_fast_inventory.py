from playwright.sync_api import expect


def test_inventory_loads_instantly(page):
    # The 'page' fixture is already authenticated because of browser_context_args!

    # 1. Go directly to the internal page
    page.goto("https://www.saucedemo.com/inventory.html")

    # 2. Assert (It should work immediately)
    expect(page.locator(".title")).to_have_text("Products")
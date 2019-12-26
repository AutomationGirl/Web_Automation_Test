from behave import *
from Features.pages.search_page import ProductSearch


@when("I navigate to application url")
def step_impl(context):
    ProductSearch(context.driver).open_application()


@step("Cancel popup if displayed")
def step_impl(context):
    ProductSearch(context.driver).click_on_cancel()


@step("Search product {product_name}")
def step_impl(context, product_name):
    ProductSearch(context.driver).search_product(product_name)


@then("Verify searched category {product_category}")
def step_impl(context, product_category):
    ProductSearch(context.driver).verify_search_result(product_category)


@step("Apply two filters on colour and brand")
def step_impl(context):
    ProductSearch(context.driver).apply_filter()


@step("Verify filter {b_name} brand and {c_name} colour are selected")
def step_impl(context, b_name, c_name):
    ProductSearch(context.driver).verify_filter(b_name, c_name)


@then("Verify result")
def step_impl(context):
    ProductSearch(context.driver).filter_result()


@step("Click on first product detail")
def step_impl(context):
    ProductSearch(context.driver).product_details()


@step("Select size of product")
def step_impl(context):
    ProductSearch(context.driver).choose_product_size()


@then("Click on buy now")
def step_impl(context):
    ProductSearch(context.driver).click_on_buy_now()


@then("Should show login page")
def step_impl(context):
    ProductSearch(context.driver).login_page()

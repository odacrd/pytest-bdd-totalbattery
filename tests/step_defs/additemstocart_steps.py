import time

from pytest_bdd import parsers
from tests.step_defs.common_steps import *


@given("the Subscribe dialog has been closed")
def step_function(context):
    subscribe_popup = context['home_page'].wait_for_subscribe_popup() \
        .enter_email("tester@test.com") \
        .close_subscribe_popup()


@given("the user has navigated to the Total Battery online store")
def step_function(context):
    context['store_page'] = context['home_page'].go_to_online_store()
    store_page = context['store_page']
    assert store_page.online_store_logo is not None

@given("the user navigates to the Shipping Info page")
def step_function(context):
    shipping_page = context['store_page'].go_to_shipping_page()
    assert shipping_page.get_shipping_h1 == "OUR SHIPPING CHARGES"
    time.sleep(5)

@then("the user navigates back to the Home page")
def step_function(context):
    home_page = context['store_page'].go_to_home_page(context)
    assert home_page.home_tab_text == "Home"
    time.sleep(5)


@when("the user picks 'Small and Specialty Batteries - Drones'")
def step_function(context):
    # select Small and Specialty Batteries - Drones
    context['store_page'].go_to_small_batteries_option() \
        .go_to_drones_option()


@when(parsers.parse("first item added is {item1}"))
def step_function(context, item1):
    store_page = context['store_page']
    cart_popup = store_page.add_product_to_cart(item1)
    context['money'] += cart_popup.get_item_price
    store_page = cart_popup.continue_shopping(context)
    assert store_page.cart_count == "1"

@when("the user navigates back one page")
def step_function(context):
    store_page = context['store_page']
    store_page.goback()

@when(parsers.parse("next item added is {item2}"))
def step_function(context, item2):
    store_page = context['store_page']
    cart_popup = store_page.add_product_to_cart(item2)
    context['money'] += cart_popup.get_item_price
    context['cart_page'] = cart_popup.go_to_cart()
    assert context['cart_page'].header_text == 'Your Cart'
    assert store_page.cart_count == "2"


@then(parsers.parse("the actual total equals the calculated total and the {expected_total}"))
def step_function(context, expected_total):
    cart_page = context['cart_page']
    money = context['money']
    calulated_total = str(round(money, 2))
    assert cart_page.header_text == 'Your Cart'

    print("Expected Cart Total:" + expected_total)
    print("Actual Cart Total:" + cart_page.cart_total)
    print("Calculated Total:" + calulated_total)
    assert cart_page.cart_total == calulated_total
    assert cart_page.cart_total == expected_total
    time.sleep(5)

@given("the shopping cart is empty")
def step_function(context):
    store_page = context['store_page']
    assert store_page.cart_count == "0"
    money = float(0.00)
    context['money'] = money

@when("the user proceeds to checkout")
def step_function(context):
    cart_page = context['cart_page']
    context['checkout_page'] = cart_page.proceed_to_checkout()

@then(parsers.parse("the checkout subtotal equals the {expected_total}"))
def step_function(context, expected_total):
    checkout_page = context['checkout_page']
    print("Expected Cart Total:" + expected_total)
    print("Checkout SubTotal:" + checkout_page.checkout_subtotal)
    assert checkout_page.checkout_subtotal == expected_total
    time.sleep(5)

@when("user enters all required data except phone number")
def step_function(context):
    checkout_page = context['checkout_page']
    checkout_page.enter_required()
    checkout_page.click_Continue()


@then("an Error Message is displayed")
def step_function(context):
    checkout_page = context['checkout_page']
    print("\nerror msg: " + checkout_page.error_msg)
    assert checkout_page.error_msg == "Oops, some fields require attention below"
    time.sleep(5)

@when("user enters missing phone number")
def step_function(context):
    checkout_page = context['checkout_page']
    checkout_page.enter_missing_phone_number()
    checkout_page.click_Continue()


@then("'Continue Payment' button is displayed")
def step_function(context):
    checkout_page = context['checkout_page']
    assert checkout_page.continue_payment_btn_displayed() is True
    time.sleep(5)

@when("'Continue Payment' button is clicked")
def step_function(context):
    checkout_page = context['checkout_page']
    checkout_page.click_continue_payment_btn()


@then(parsers.parse("the 'Pay' amount is {pay_amount}"))
def step_function(context,pay_amount):
    checkout_page = context['checkout_page']
    print("\npay_amount: " + checkout_page.checkout_pay)
    assert checkout_page.checkout_pay == pay_amount
    time.sleep(5)


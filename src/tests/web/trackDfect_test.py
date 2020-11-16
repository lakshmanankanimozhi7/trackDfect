from src.helpers.trackDfect_helpers import Helper
import pytest
import logging
from src.tests.base_test import BaseTest




class trackDfectTest(BaseTest):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    """
        Test buy product in amazon app
    """

    def test_buy_product_in_amazon(self):
        trackDefect_helper = Helper()

        #Visit Amazon page
        trackDefect_helper.visit_amazon_page()

        #Read product name from excel and search that product in search bar
        trackDefect_helper.search_product(product_name=trackDefect_helper.get_product_name_form_excel_sheet())

        #Click search button
        trackDefect_helper.click_search_button()

        #Store the price of the product in product page
        price_of_product = trackDefect_helper.check_price_of_the_product_in_product_page()

        #Select the product
        trackDefect_helper.select_uno_card()

        #Add the product to the cart
        trackDefect_helper.click_add_to_cart_button()

        #Verify cart added successfully
        trackDefect_helper.verify_added_to_cart_message()

        #check price of the product in cart
        price_in_cart = trackDefect_helper.check_price_of_the_product()

        #Click proceed to buy button
        trackDefect_helper.click_proceed_to_buy_button()

        #Login to the account
        trackDefect_helper.enter_email_or_phone_number_text_box(email="lakshmanankanimozhi7@gmail.com")
        trackDefect_helper.click_continue_button()
        trackDefect_helper.type_password_text_box(password="Test@123")
        trackDefect_helper.click_login_button()

        #select address and visit final payment page
        trackDefect_helper.click_deliver_to_this_address_button()
        trackDefect_helper.click_continue_button_in_delivery_option_page()

        #Visit cart page and delete the product from cart
        trackDefect_helper.switch_window_by_index(index=0)
        trackDefect_helper.visit_cart_page()
        trackDefect_helper.click_delete_product_from_cart()

        #Verify empty cart message
        trackDefect_helper.check_cart_is_empty_message()

        #verify price in product page and cart page are same
        assert price_of_product == price_in_cart







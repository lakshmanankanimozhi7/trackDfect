from src.pages.web_page_element.page_elements import AmazonPage
from src.tests.base_test import BaseTest
import src.framework.global_config as config
import time
import xlsxwriter
import xlrd
from src.tests.base_test import BaseTest


class Helper(BaseTest):

    amazon_page = AmazonPage()

    """Visit Amazon page"""
    def visit_amazon_page(self):
        self.amazon_page.open_url(uri=self.amazon_page.APP_URL)

    """search product in search bar"""
    def search_product(self,product_name):
        self.amazon_page.type(self.amazon_page.search_bar,product_name)

    """click search button"""
    def click_search_button(self):
        self.amazon_page.click(self.amazon_page.search_button)

    """Select product"""
    def select_uno_card(self):
        self.amazon_page.click(self.amazon_page.select_uno_card)

    """click add to cart button"""
    def click_add_to_cart_button(self):
        self.switch_window_by_index(index=1)
        self.amazon_page.scroll_to_element(self.amazon_page.add_to_cart_button)
        config.DRIVER.implicitly_wait(5)
        self.amazon_page.click(self.amazon_page.add_to_cart_button)

    """check price of the product in cart page"""
    def check_price_of_the_product(self):
        price = self.amazon_page.get_attribute(self.amazon_page.price_of_the_product,'innerText')
        price = price.split("\xa0")
        price = price[1].split(".")[0]
        return price

    """verfiy add to cart message"""
    def verify_added_to_cart_message(self):
        self.amazon_page.is_element_present(self.amazon_page.added_to_cart_message)
        message = self.amazon_page.get_attribute(self.amazon_page.added_to_cart_message,'innerText')
        assert message == "Added to Cart"

    """visit cart page"""
    def visit_cart_page(self):
        self.amazon_page.click(self.amazon_page.cart_page)

    """click proceed to pay button"""
    def click_proceed_to_buy_button(self):
        self.amazon_page.click(self.amazon_page.proceed_to_buy_button)

    """enter email or phone number of the user"""
    def enter_email_or_phone_number_text_box(self,email):
        self.amazon_page.type(self.amazon_page.email_or_phone_number_text_box,email)

    """click continue button"""
    def click_continue_button(self):
        self.amazon_page.click(self.amazon_page.continue_button)

    """type password of the user"""
    def type_password_text_box(self,password):
        self.amazon_page.type(self.amazon_page.password_text_box,password)

    """click login button"""
    def click_login_button(self):
        self.amazon_page.click(self.amazon_page.login_button)

    """click delete button in cart page to remove the product from the cart"""
    def click_delete_product_from_cart(self):
        self.amazon_page.click(self.amazon_page.delete_product_from_cart)
        time.sleep(10)

    """Select address"""
    def click_deliver_to_this_address_button(self):
        self.amazon_page.click(self.amazon_page.deliver_to_this_address_button)

    """click continue button in delivery page"""
    def click_continue_button_in_delivery_option_page(self):
        self.amazon_page.click(self.amazon_page.continue_button_in_delivery_option_page)

    def switch_window_by_index(self,index):
        print(config.DRIVER.current_window_handle)
        handles = config.DRIVER.window_handles
        config.DRIVER.switch_to.window(handles[index])

    """verify cart is empty after removing the product from the cart"""
    def check_cart_is_empty_message(self):
        message = self.amazon_page.get_attribute(self.amazon_page.cart_is_empty_message,"innerText")
        assert message == "Your Amazon Cart is empty."

    """create excel store product names in the sheet and read the product name for search"""
    def get_product_name_form_excel_sheet(self):
        workbook = xlsxwriter.Workbook("product_list.xlsx")
        worksheet = workbook.add_worksheet("Amazon_products")
        worksheet.write(0, 0, "Uno cards")
        workbook.close()
        loc = ("product_list.xlsx")
        workbook = xlrd.open_workbook(loc)
        worksheet = workbook.sheet_by_name("Amazon_products")
        product_name = worksheet.cell_value(0,0)
        return product_name

    """check price of the product in product page"""
    def check_price_of_the_product_in_product_page(self):
        price = self.amazon_page.get_attribute(self.amazon_page.price_of_the_product_in_product_page,'innerText')
        print(price)
        return price
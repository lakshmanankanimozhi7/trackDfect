from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AmazonPage(BasePage):
    search_bar = (By.CSS_SELECTOR,'#twotabsearchtextbox')
    search_button = (By.CSS_SELECTOR,'#nav-search-submit-text')
    select_uno_card = (By.CSS_SELECTOR,'.rush-component.s-latency-cf-section .s-main-slot div[data-index="5"] img')
    add_to_cart_button = (By.CSS_SELECTOR,'#add-to-cart-button')
    price_of_the_product_in_product_page = (By.CSS_SELECTOR,'.rush-component.s-latency-cf-section .s-main-slot div[data-index="5"] .a-price-whole')
    price_of_the_product =(By.CSS_SELECTOR,'#hlb-subcart .a-color-price.hlb-price')
    added_to_cart_message = (By.CSS_SELECTOR,'#huc-v2-order-row-confirm-text  h1')
    cart_page = (By.CSS_SELECTOR,'#nav-cart-text-container')
    proceed_to_buy_button = (By.CSS_SELECTOR,'#hlb-ptc-btn #hlb-ptc-btn-native')
    email_or_phone_number_text_box = (By.CSS_SELECTOR,'.a-row #ap_email')
    continue_button = (By.CSS_SELECTOR,'#continue')
    password_text_box = (By.CSS_SELECTOR,'.a-section #ap_password')
    login_button = (By.CSS_SELECTOR,'#signInSubmit')
    proceed_to_buy_button_in_cart_page = (By.CSS_SELECTOR,'#sc-buy-box-ptc-button-announce')
    net_banking_payment_method = (By.CSS_SELECTOR,'#pp-o5L74Q-109')
    delete_product_from_cart = (By.CSS_SELECTOR,'#activeCartViewForm span[data-action="delete"] input')
    deliver_to_this_address_button = (By.CSS_SELECTOR,'.a-nostyle #address-book-entry-0 .ship-to-this-address .a-declarative.a-button-text')
    continue_button_in_delivery_option_page = (By.CSS_SELECTOR,'.a-spacing-medium .save-sosp-button-box .sosp-continue-button input[type="submit"]')
    cart_is_empty_message = (By.CSS_SELECTOR,'#sc-active-cart .a-row.sc-cart-header h1')
    get_id_of_payment_page = (By.CSS_SELECTOR,'#apx-content .a-section.a-spacing-none.pmts-widget-section.pmts-portal-root-oPrdAmiuuoPz.pmts-portal-component')

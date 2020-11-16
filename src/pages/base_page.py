import src.framework.global_config as config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
)
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    APP_URL = "https://www.amazon.in/"

    def wait_for_page_load(self):
        state = config.DRIVER.execute_script("return document.readyState;")
        return state == "complete"

    def maximize_window(self):
        config.DRIVER.maximize_window()

    # return the element if its present on the dom
    def find_presence_of_element(self, selector, timeout=config.TIMEOUT):
        element = WebDriverWait(config.DRIVER, timeout).until(
            expected_conditions.presence_of_element_located(selector)
        )
        assert element is not None
        return element

    def find_element(self, loc, max_retries=1, timeout=config.TIMEOUT):
        retries = 0
        while True:
            try:
                element = WebDriverWait(
                    config.DRIVER, timeout, poll_frequency=config.POLL_FREQUENCY
                ).until(expected_conditions.visibility_of_element_located(loc))
                return element
            except Exception as e:
                if retries < max_retries:
                    retries += 1
                    continue
                else:
                    raise e

    def wait_for_element_not_to_be_present(self, selector, timeout=config.TIMEOUT):
        status = WebDriverWait(config.DRIVER, timeout, poll_frequency=1).until(
            expected_conditions.invisibility_of_element_located(selector)
        )

        assert status is True
        return status

    def click(self, selector, max_retries=2, timeout=config.TIMEOUT):
        element = self.find_element(selector, max_retries=max_retries, timeout=timeout)
        element.click()

    def click_presence_of_element(self, selector, timeout=config.TIMEOUT):
        element = self.find_presence_of_element(selector, timeout=timeout)
        element.click()

    def get_element_selector(self, selector, index="1"):
        if type(selector) is tuple:
            element = selector[1] if type(selector) is tuple else selector
            element = element.format(index)
            loc_list = list(selector)
            loc_list[1] = element
            selector = tuple(loc_list)
            return selector
        else:
            selector.format(index)
            return selector

    def click_by_index(self, selector, index="1"):
        if type(selector) is tuple:
            element = selector[1] if type(selector) is tuple else selector
            element = element.format(index)
            loc_list = list(selector)
            loc_list[1] = element
            selector = tuple(loc_list)
            self.click(selector)
        else:
            selector.format(index)
            self.click(selector)

    def click_presence_of_element_by_index(self, selector, index="1"):
        if type(selector) is tuple:
            element = selector[1] if type(selector) is tuple else selector
            element = element.format(index)
            loc_list = list(selector)
            loc_list[1] = element
            selector = tuple(loc_list)
            self.click_presence_of_element(selector)
        else:
            selector.format(index)
            self.click_presence_of_element(selector)

    def verify_element_by_index(self, selector, max_retries=2, index="1"):
        if type(selector) is tuple:
            element = selector[1] if type(selector) is tuple else selector
            element = element.format(index)
            loc_list = list(selector)
            loc_list[1] = element
            selector = tuple(loc_list)
            return self.find_element(selector, max_retries=max_retries)
        else:
            selector.format(index)
            return self.find_element(selector, max_retries=max_retries)

    def is_element_displayed_by_index(self, selector, index="1"):
        if type(selector) is tuple:
            element = selector[1] if type(selector) is tuple else selector
            element = element.format(index)
            loc_list = list(selector)
            loc_list[1] = element
            selector = tuple(loc_list)
            return self.is_element_displayed(selector)
        else:
            selector.format(index)
            return self.is_element_displayed(selector)

    def click_and_wait(self, selector, max_retries=2, timeout=config.TIMEOUT):
        self.click(selector, max_retries=max_retries, timeout=timeout)

    def click_and_hold(self, selector):
        ActionChains(config.DRIVER).click_and_hold(selector).move_by_offset(
            10, 0
        ).release().perform()

    def clear(self, selector, count=20, timeout=config.TIMEOUT):
        element = self.find_element(selector, timeout)
        element.click()
        element.send_keys(count * Keys.BACK_SPACE)

    def get_text(self, selector, timeout=config.TIMEOUT):
        self.wait_for_presence(selector, timeout=timeout)
        return self.find_element(selector, timeout).text

    def get_text_by_index(self, selector, timeout=config.TIMEOUT, index="1"):
        if type(selector) is tuple:
            element = selector[1] if type(selector) is tuple else selector
            element = element.format(index)
            loc_list = list(selector)
            loc_list[1] = element
            selector = tuple(loc_list)
            return self.get_text(selector, timeout=timeout)
        else:
            selector.format(index)
            return self.get_text(selector, timeout=timeout)

    def type(self, selector, text, timeout=config.TIMEOUT):
        self.clear(selector, timeout=timeout)
        self.find_element(selector, timeout).send_keys(text)

    def type_amount(self, selector, text, timeout=config.TIMEOUT):
        self.find_element(selector, timeout).send_keys(10 * Keys.BACK_SPACE)
        self.find_element(selector, timeout).send_keys(text)

    def get_attribute(self, selector, attribute, timeout=config.TIMEOUT):
        return self.find_element(selector, timeout).get_attribute(attribute)

    def is_element_present(self, selector, timeout=config.TIMEOUT):
        return True if self.find_presence_of_element(selector, timeout) else False

    def is_element_displayed(self, selector, max_retries=1, timeout=config.TIMEOUT):
        return (
            True
            if self.find_element(
                selector, max_retries=max_retries, timeout=timeout
            ).is_displayed()
            else False
        )

    def is_element_enabled(self, selector, timeout=config.TIMEOUT):
        return True if self.find_element(selector, timeout).is_enabled() else False

    def is_element_selected(self, selector, timeout=config.TIMEOUT):
        return True if self.find_element(selector, timeout).is_selected() else False

    def navigate_back(self):
        config.DRIVER.execute_script("window.history.go(-1);")

    def open_tab(self):
        config.DRIVER.find_element_by_tag_name("body").send_keys(Keys.COMMAND + "t")

    def close_tab(self):
        config.DRIVER.find_element_by_tag_name("body").send_keys(Keys.COMMAND + "w")

    def open_window(self):
        current_handle = config.DRIVER.current_window_handle
        config.DRIVER.execute_script("window.open('');")
        return current_handle

    def get_window_handles(self):
        handles = config.DRIVER.window_handles
        return handles

    def open_url(self, uri):
        config.DRIVER.get(uri)
        self.wait_for_page_load()
        self.maximize_window()
        #config.DRIVER.set_window_size(1024, 768)

    def get_current_url(self):
        print(config.DRIVER.current_url)
        return config.DRIVER.current_url

    def refresh(self):
        print(self.get_current_url())
        self.open_url(self.get_current_url())

    def reload(self):
        config.DRIVER.refresh()
        self.wait_for_page_load()

    def get_title(self):
        return config.DRIVER.title

    def wait_for_presence(self, selector, max_retries=2, timeout=config.TIMEOUT):
        """

        :rtype: object
        """
        # UtilsHelper.wait(1)
        retries = 0
        while True:
            try:
                element = WebDriverWait(config.DRIVER, timeout).until(
                    expected_conditions.visibility_of_element_located(selector)
                )

                return element

            except StaleElementReferenceException as e:
                if retries < max_retries:
                    retries += 1
                    continue
                else:
                    raise e

    def wait_for_element_not_present(
        self, selector, max_retries=3, timeout=config.TIMEOUT
    ):
        retries = 0
        while True:
            try:
                status = WebDriverWait(config.DRIVER, timeout).until(
                    expected_conditions.invisibility_of_element_located(selector)
                )
                return status
            except Exception as e:
                if retries < max_retries:
                    retries += 1
                    continue
                else:
                    self.logger.error("wait_for_element_not_present: %s" % e)
                    raise e

    def select(self, locator, timeout=config.TIMEOUT):
        return Select(self.find_element(locator, timeout))

    def select_by_visible_text(self, text):
        return Select(self)

    def set_text(self, loc, text):
        element = loc[1] if type(loc) is tuple else loc
        script = (
            "var el = document.querySelector('" + element + "');"
            "el.value = '" + text + "';"
        )
        self.logger.info(script)
        config.DRIVER.execute_script(script)

    # Scroll methods
    def scroll_to_height(self, height=0):
        config.DRIVER.execute_script("window.scrollTo(0, %d)" % height)

    def scroll_to_top(self):
        self.scroll_to_height()

    def scroll_to_bottom(self):
        config.DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, selector):
        element = self.find_presence_of_element(selector)
        config.DRIVER.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_element_by_index(self, selector, index="1", timeout=config.TIMEOUT):
        selector = self.get_element_selector(selector, index)
        element = self.find_presence_of_element(selector, timeout)
        config.DRIVER.execute_script("arguments[0].scrollIntoView();", element)

    def accept_alert(self):
        try:
            WebDriverWait(config.DRIVER, 3).until(
                expected_conditions.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )

            alert = config.DRIVER.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutError:
            print("no alert")

    def hover(self, locator):
        ActionChains(config.DRIVER).move_to_element(locator).perform()

    def verify_element_not_present(self, loc):
        try:
            config.DRIVER.find_element_by_css_selector(loc)
            return True
        except NoSuchElementException:
            return False

    def enter_key(self, loc):
        element = self.find_element(loc=loc)
        element.send_keys(Keys.ENTER)

    def click_enter_button(self, selector, timeout=config.TIMEOUT):
        self.find_element(selector, timeout).send_keys(u"\ue007")

    def click_tab(self, selector, timeout=config.TIMEOUT):
        self.find_element(selector, timeout).send_keys(Keys.TAB)

    def scroll_to_element_by_index_and_click(self, selector, index="1", timeout=config.TIMEOUT):
        selector = self.get_element_selector(selector, index)
        element = self.find_presence_of_element(selector, timeout)
        config.DRIVER.execute_script("arguments[0].scrollIntoView();", element)
        self.click(selector)




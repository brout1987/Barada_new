from SeleniumOperations import SeleniumOperations
from selenium.webdriver.support.ui import Select
from Locators import Locators
import time

class SipTg:
    def __init__(self, sel_op_obj):
        self.driver = sel_op_obj.driver
        self.sel_op = sel_op_obj

    def create_tg(self):
        self.sel_op.sip_tg_types()
        self.driver.find_element_by_link_text(Locators.tgLinkTest).click()
        time.sleep(5)







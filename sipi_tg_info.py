from SeleniumOperations import SeleniumOperations
from selenium.webdriver.support.ui import Select
from Locators import Locators
import time

class SipiTg:
    def __init__(self,selOp_obj):
        self.driver = selOp_obj.driver
        self.sel_obj = selOp_obj

    def create_tg(self):
        self.sel_obj.sipi_tg_types()
        self.driver.find_element_by_link_text(Locators.tgLinkTest).click()
        time.sleep(5)



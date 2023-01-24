from Locators import Locators
from selenium import webdriver

class ServiceTrigger:
    def __init__(self,sel_opr_obj):
        self.driver = sel_opr_obj.driver
        self.sel_obj = sel_opr_obj

    def Create_ser_trig(self):
        self.sel_obj.create_plan_policies()
        self.driver.find_element_by_xpath(Locators.servTrigPath).click()
        try:
            title = "Plan Groups"
            current_window = self.driver.current_window_handle
            self.sel_obj.switch_to_new_window(current_window, title)

        finally:
            self.driver.close()
            self.driver.switch_to_window(current_window)
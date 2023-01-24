from SeleniumOperations import SeleniumOperations
from Locators import Locators


class Routing:
    def __init__(self, sel_opr_obj):
        self.driver = sel_opr_obj.driver
        self.sel_obj = sel_opr_obj

    def CreateRouting(self):

        self.sel_obj.create_plan_policies()
        self.driver.find_element_by_xpath(Locators.routingPath).click()
        try:
            title = "Routing Plans and Policies"
            current_window = self.driver.current_window_handle
            self.sel_obj.switch_to_new_window(current_window, title)

        finally:
            self.driver.close()
            self.driver.switch_to_window(current_window)

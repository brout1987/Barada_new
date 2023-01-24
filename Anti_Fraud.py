import time

from Locators import Locators


class AntiFraud:
    def __init__(self, Sel_opr_obj):
        self.driver = Sel_opr_obj.driver
        self.sel_obj = Sel_opr_obj

    def anti_fraud_routing(self):
        self.sel_obj.create_plan_policies()
        self.driver.find_element_by_xpath(Locators.antiFraudPath).click()
        try:
            title = "Anti-Fraud Routing Plans and Policies"
            current_window = self.driver.current_window_handle
            self.sel_obj.switch_to_new_window(current_window, title)
        finally:
            self.driver.close()
            self.driver.switch_to_window(current_window)
            time.sleep(5)

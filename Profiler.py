import time

from Locators import Locators
from SeleniumOperations import SeleniumOperations
from selenium.webdriver.support.ui import Select


class Profiler:
    def __init__(self, sel_opr_obj):
        self.driver = sel_opr_obj.driver
        self.se_obj = sel_opr_obj

    def upload_profiler(self):
        parent_window = self.driver.current_window_handle
        self.se_obj.sip_pofiler()
        self.driver.find_element_by_id(Locators.uploadProfId).click()
        self.driver.find_element_by_id(Locators.fileId).send_keys('C:\\Users\\gs-1020\\Desktop\\ICE-Profiler\\ice-new1.xml')
        self.driver.find_element_by_xpath(Locators.profNamePath).send_keys('Barada_prof1')
        self.driver.find_element_by_id(Locators.saveBtnId).click()
        self.driver.switch_to_window(parent_window)

    def create_profiler(self):
        parent_window = self.driver.current_window_handle
        self.se_obj.sip_pofiler()
        self.driver.find_element_by_id(Locators.createProfId).click()
        self.driver.find_element_by_id(Locators.profNameId).send_keys('Delete_prof')
        self.driver.find_element_by_id(Locators.parameterNameId).click()
        select_params_name = self.driver.find_element_by_id(Locators.parameterNameId)
        Select(select_params_name).select_by_value('SipRequestLine')
        self.driver.find_element_by_xpath(Locators.settingImgPath).click()
        select_filed = self.driver.find_element_by_id(Locators.attributesFiledId)
        Select(select_filed).select_by_visible_text('Method')
        self.driver.find_element_by_id(Locators.saveBtnId).click()
        select_name = self.driver.find_element_by_id(Locators.operatorId)
        Select(select_name).select_by_visible_text('Equal')
        select_value = self.driver.find_element_by_id(Locators.valueId)
        Select(select_value).select_by_value('String')
        self.driver.find_element_by_xpath(Locators.valueSettingImgPath).click()
        self.driver.find_element_by_id('v_1_1_c_Value').send_keys('INVITE')
        self.driver.find_element_by_id(Locators.saveBtnId).click()
        self.driver.find_element_by_xpath(Locators.nextBtnImgPath).click()
        self.driver.find_element_by_id('a_1').click()
        select_action = self.driver.find_element_by_id('a_1')
        Select(select_action).select_by_visible_text('Delete')
        select_parameter = self.driver.find_element_by_id('ap_1')
        Select(select_parameter).select_by_visible_text('SipHeader')
        self.driver.find_element_by_xpath('//*[@id="c_ap_1"]//img').click()
        select_header_attr = self.driver.find_element_by_id('ap_1_c_Header')
        Select(select_header_attr).select_by_value('Allow')
        self.driver.find_element_by_id(Locators.saveBtnId).click()
        time.sleep(5)




from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from SeleniumOperations import SeleniumOperations
from sip_tg_info import SipTg
from sipi_tg_info import SipiTg
from Create_routing import Routing
from Service_trigger import ServiceTrigger
from Anti_Fraud import AntiFraud
from Profiler import Profiler

from TG_locators import TG_Locators
import pytest


@pytest.mark.parametrize("username,password,message",
                         [("acxmanager", "acxmgr", "Success")])
@pytest.mark.sanity
def test_login_functionality(username, password, message):
    selOp_obj = SeleniumOperations()
    selOp_obj.wait_for_element_visible(locator='xpath', path='//*[text()="Veraz Login"]')
    selOp_obj.login_functionality(username=username, password=password, message=message)
    tg_obj = SipTg(selOp_obj)
    tg_obj.create_tg()
    # sipi_tg_obj = SipiTg(selOp_obj)
    # sipi_tg_obj.create_tg()
    # routing_obj = Routing(selOp_obj)
    # routing_obj.CreateRouting()
    # ser_tri_obj = ServiceTrigger(selOp_obj)
    # ser_tri_obj.Create_ser_trig()
    # sip_prof_obj = Profiler(selOp_obj)
    # sip_prof_obj.upload_profiler()
    # anti_fraud_obj = AntiFraud(selOp_obj)
    # anti_fraud_obj.anti_fraud_routing()
    # sip_prof_obj.create_profiler()







#
#     try:
#         errormsg = chromeBrowser.find_element_by_id('notification-message')
#         print(errormsg.text)
#     except:
#         pass
#     if message == 'Success':
#         assert welcome.text == 'Welcome: ACXMANAGER'
#         assert errormsg == None
#         #        create_TG(chromeBrowser)
#         create_sipi_tg(chromeBrowser)
#     #        profiler(chromeBrowser)
#     #        create_routing_plan(chromeBrowser)
#     #        create_service_trigger(chromeBrowser)
#     #        create_antiford_plan(chromeBrowser)
#     # time.sleep(10)
#     else:
#         assert welcome == None
#         assert message == errormsg.text
#
#     chromeBrowser.close()
#
#
#
#
#



#
#

#
#
# def profiler(chromeBrowser):
#     profiles = chromeBrowser.find_element_by_id('I_PROFILES')
#     profiles.click()
#     sipprofiler = chromeBrowser.find_element_by_xpath('//*[text()="SIP Profiler"]')
#     sipprofiler.click()
#     #    time.sleep(10)
#
#     parent_handle = chromeBrowser.current_window_handle
#     title = "Dialogic - Sip Profiler Configuration"
#     switch_to_window(chromeBrowser, parent_handle, title)
#
#     uploadfile = chromeBrowser.find_element_by_id('btn-addSipProfiler')
#     uploadfile.click()
#     file_upload = chromeBrowser.find_element_by_id('filepc')
#     file_upload.send_keys('C:\\Users\\gs-1020\\Desktop\\Desktop\\ICE-Profiler\\ice-new1.xml')
#     inputname = chromeBrowser.find_element_by_xpath(
#         '//*[@class="popup-tbox FormElement ui-widget-content ui-corner-all"]')
#     inputname.send_keys('Barada_prof')
#     submit_button = chromeBrowser.find_element_by_id('btnSave')
#     submit_button.click()
#
#     time.sleep(5)
#
#
# def switch_to_window(driver, parent_window, title):
#     flag = False
#     handles = driver.window_handles
#     for handle in handles:
#         if handle != parent_window:
#             driver.switch_to_window(handle)
#             if title in driver.title:
#                 flag = True
#                 break
#     if flag == False:
#         raise Exception("Wrong Window")
#
#
#

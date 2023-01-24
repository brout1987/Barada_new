from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest

@pytest.mark.parametrize("username,password,message",
                         [("acxmanager","acxmgr","Success")])
                         # ("acxmgr","acxmanager","Invalid Login Credentials")])

def test_login_functionality (username,password,message):


    chromeBrowser = webdriver.Ie('C:\\IE_Driver\\IEDriverServer.exe')
    chromeBrowser.maximize_window()
    chromeBrowser.get("http://192.168.201.8/apex/f?p=1000:101:2506354389470765::::FAPP_CALLER_APP,FAPP_CALLER_PAGE:1001,3")

#   element = chromeBrowser.find_element_by_id('apex_layout_5919512191508810').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[1]
#   print(element)

#   userinput = element.find_elements_by_tag_name('td')[1].find_elements_by_tag_name('input')[1]
#   print(f"user input  :{userinput}")
    time.sleep(5)
    #print("Deepika here")
    userinput = chromeBrowser.find_element_by_id('P101_USERNAME')
    userinput.send_keys(username)
    passinput = chromeBrowser.find_element_by_id('P101_PASSWORD')
    passinput.send_keys(password)

    # if chromeBrowser.find_elements_by_xpath('//*[@value="Login"]').size:
        # print("Login button found1")
    # if chromeBrowser.find_element_by_xpath('//*[@class="button-alt1"]').size:
        # print("Login button found2")
    chromeBrowser.find_element_by_xpath('//*[@class="button-alt1"]').send_keys(Keys.ENTER)
    time.sleep(10)
    welcome = None
    errormsg = None

    try:
        welcome = chromeBrowser.find_element_by_xpath('//*[@class="app-user"]')
        print(welcome.text)
    except:
        pass

#    logoutinput = chromeBrowser.find_element_by_link_text('Logout')
#    logoutinput.click()

    try:
        errormsg = chromeBrowser.find_element_by_id('notification-message')
        print(errormsg.text)
    except:
        pass
    if message == 'Success':
        assert welcome.text == 'Welcome: ACXMANAGER'
        assert errormsg == None
        create_TG(chromeBrowser)
        # create_sipi_tg(chromeBrowser)
        # create_routing_plan(chromeBrowser)
        # create_service_trigger(chromeBrowser)
        # create_antiford_plan(chromeBrowser)
        time.sleep(10)
    else:
        assert welcome == None
        assert message == errormsg.text

    chromeBrowser.quit()

def create_TG(chromeBrowser):
    trunkgroup = chromeBrowser.find_element_by_link_text('Trunk Groups (TG)')
    trunkgroup.send_keys(Keys.ENTER)
    time.sleep(5)
    createtg = chromeBrowser.find_element_by_xpath('//*[@class="topbar-content"]//img')
    print('create tg - ', createtg)
    # WebDriverWait(chromeBrowser, 20).until(EC.element_to_be_clickable(
    #     (By.XPATH, "//*[@class='topbar-content']//img")))
    ActionChains(chromeBrowser).move_to_element(createtg).click(createtg).perform()
    print('done clicking')
    # ActionChains(chromeBrowser).move_to_element(createtg).click(createtg).perform()
    #send_keys(Keys.ENTER).perform()
    time.sleep(5)
    """
    selectinput = chromeBrowser.find_element_by_xpath('//*[@class="selectlist"]')
    selectitem = Select(selectinput)
    selectitem.select_by_visible_text("SIP")
    trunkgroupname = chromeBrowser.find_element_by_id('P2_CLLI_NAME')
    trunkgroupname.send_keys('SIP-Egr')
    inputcountry = chromeBrowser.find_element_by_id('TC_ID')
    selectcounrty = Select(inputcountry)
    selectcounrty.select_by_visible_text("India")
    ipconfiguration = chromeBrowser.find_element_by_name('IP Configuration')
    ipconfiguration.click()
    gatewayadress = chromeBrowser.find_element_by_id('P2_RGW_IP_ADDRESS')
    gatewayadress.send_keys('10.10.10.22')
    gatewayport = chromeBrowser.find_element_by_id('P2_RGW_PORT')
    gatewayport.send_keys('9877')
    submitinput = chromeBrowser.find_element_by_xpath('//*[@id="jam"] ')
    submitinput.click()
    time.sleep(5)
    alert = Alert(chromeBrowser)
    alert.accept()
    unlockinput = chromeBrowser.find_element_by_id('Unlock')
    unlockinput.click()
    time.sleep(5)
    unlocktg = Alert(chromeBrowser)
    unlocktg.accept()
    localgatewayinput = chromeBrowser.find_element_by_xpath('//*[text()="Local Gateways"]')
    localgatewayinput.click()
    insertinput = chromeBrowser.find_element_by_xpath('//*[@class="topbar-content"]//img')
    insertinput.click()
    lgwname = chromeBrowser.find_element_by_id('P132_LGW_NAME')
    selectlgw = Select(lgwname)
    selectlgw.select_by_visible_text('LGW1')
    savelgw = chromeBrowser.find_element_by_id('jam')
    savelgw.click()
    time.sleep(5)
    alert.accept()
    trunkgroup = chromeBrowser.find_element_by_link_text('Trunk Groups (TG)')
    trunkgroup.click()
    """


#assert "Invalid Login" in errormsg.text
def plan_and_policies(chromeBrowser):
    routingpolicies = chromeBrowser.find_element_by_id('I_POLICIES')
    routingpolicies.click()
    planpolicies = chromeBrowser.find_element_by_id('P_PLAN_AND_POLICIES')
    ActionChains(chromeBrowser).move_to_element(planpolicies).perform()
    time.sleep(5)

def create_routing_plan(chromeBrowser):
    plan_and_policies(chromeBrowser)
    routinginput = chromeBrowser.find_element_by_xpath('//*[text()="Routing"]')
    routinginput.click()
    time.sleep(2)
    parentwindow = chromeBrowser.current_window_handle
    chromeBrowser.switch_to.window(chromeBrowser.window_handles[1])
#    chromeBrowser.get("http://192.168.201.8/jgui/cgi-bin/routing.cgi?app=jgui&n=ACXMANAGER&i=ILLHLKPPJHKGOGOMLKMK&d=emsdb01&h=vmems&k=404&s=340468&PlanGroupType=RT&PlanGroupTypeDesc=Routing")
    chromeBrowser.close()
    chromeBrowser.switch_to.window(parentwindow)


def create_service_trigger(chromeBrowser):
    plan_and_policies(chromeBrowser)
    servicetriggerinput = chromeBrowser.find_element_by_xpath('//*[text()="Service Trigger"]')
    servicetriggerinput.click()
    time.sleep(5)
    parentwindow = chromeBrowser.current_window_handle
    chromeBrowser.switch_to.window(chromeBrowser.window_handles[1])
    chromeBrowser.close()
    chromeBrowser.switch_to.window(parentwindow)


def create_antiford_plan(chromeBrowser):
    plan_and_policies(chromeBrowser)
    antifrodinput = chromeBrowser.find_element_by_xpath('//*[text()="Anti-Fraud"]')
    antifrodinput.click()
    time.sleep(2)
    parentwindow = chromeBrowser.current_window_handle
    chromeBrowser.switch_to.window(chromeBrowser.window_handles[1])
    chromeBrowser.close()
    chromeBrowser.switch_to.window(parentwindow)

def create_sipi_tg(chromeBrowser):
    trunkgroup = chromeBrowser.find_element_by_link_text('Trunk Groups (TG)')
    trunkgroup.click()
    createtg = chromeBrowser.find_element_by_xpath('//*[@class="topbar"]//img')
    createtg.click()
    selectinput = chromeBrowser.find_element_by_xpath('//*[@class="selectlist"]')
    selectitem = Select(selectinput)
    selectitem.select_by_visible_text('SIP')
    createsiptg = chromeBrowser.find_element_by_id('P2_CLLI_NAME')
    createsiptg.send_keys('SIPI-Ing')
    selectcountry = chromeBrowser.find_element_by_id('TC_ID')
    selectcountryitem = Select(selectcountry)
    selectcountryitem.select_by_visible_text('India')
    ipconfiguration = chromeBrowser.find_element_by_name('IP Configuration')
    ipconfiguration.click()
    time.sleep(10)
#    trunkgrouptype = chromeBrowser.find_element_by_xpath('//*[contains(text(),"SIP-ISUP Direct")]')
#    trunkgrouptype.click()
    trunkgrouptype = chromeBrowser.find_elements_by_name('f01')
    print('trunkgrouplist ',len(trunkgrouptype))
    for trunk in trunkgrouptype:
        print(f"Truck value : {trunk.get_attribute('value')} {trunk}")
        if trunk.get_attribute('value') == 'I':
            trunk.click()
    time.sleep(10)
    inputremoteip = chromeBrowser.find_element_by_id('P2_RGW_IP_ADDRESS')
    inputremoteip.send_keys('10.10.10.22')
    inputremoteport = chromeBrowser.find_element_by_id('P2_RGW_PORT')
    inputremoteport.send_keys('6540')
    submitinput = chromeBrowser.find_element_by_xpath('//*[@id="jam"] ')
    submitinput.click()
    time.sleep(5)
    alert = Alert(chromeBrowser)
    alert.accept()
    unlockinput = chromeBrowser.find_element_by_id('Unlock')
    unlockinput.click()
    time.sleep(5)
    unlocktg = Alert(chromeBrowser)
    unlocktg.accept()








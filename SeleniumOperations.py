import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Locators import Locators
import random
import uuid
import time


class SeleniumOperations:

    def __init__(self, browser="chrome", wait_time=5):
        browser = browser.casefold()
        if browser == "chrome":
            self.driver = webdriver.Chrome('C:\\Chrome_Driver\\chromedriver.exe')
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "IE":
            self.driver = webdriver.Ie()
            # todo: create ie driver
        else:
            raise Exception(f"Invalid browser : {browser}")
        self.wait_time = wait_time
        self.driver.get(Locators.loginPath)

    def wait_for_element_visible(self, locator, path):
        locator = locator.casefold()
        if locator == 'xpath':
            return WebDriverWait(self.driver, self.wait_time).until(ec.visibility_of_element_located((By.XPATH, path)))
        elif locator == 'id':
            return WebDriverWait(self.driver, self.wait_time).until(ec.visibility_of_element_located((By.ID, path)))
        elif locator.lower() == 'name':
            return WebDriverWait(self.driver, self.wait_time).until(ec.visibility_of_element_located((By.NAME, path)))
        else:
            raise Exception("Invalid locator : {locator}")
        # Todo : add same for link text, partial link text, class name and tag name

    def wait_for_all_elements_visible(self, locator, path):
        locator = locator.casefold()
        if locator == 'xpath':
            return WebDriverWait(self.driver, self.wait_time).until(
                ec.visibility_of_all_elements_located((By.XPATH, path)))
        elif locator == 'id':
            return WebDriverWait(self.driver, self.wait_time).until(
                ec.visibility_of_all_elements_located((By.ID, path)))
        elif locator.lower() == 'name':
            return WebDriverWait(self.driver, self.wait_time).until(
                ec.visibility_of_all_elements_located((By.NAME, path)))
        else:
            raise Exception("Invalid locator : {locator}")

    def wait_for_element_clickable(self, locator, path):
        locator = locator.casefold()
        if locator == 'xpath':
            return WebDriverWait(self.driver, self.wait_time).until(ec.element_to_be_clickable((By.XPATH, path)))
        elif locator == 'id':
            return WebDriverWait(self.driver, self.wait_time).until(ec.element_to_be_clickable((By.ID, path)))
        elif locator == 'name':
            return WebDriverWait(self.driver, self.wait_time).until(ec.element_to_be_clickable((By.NAME, path)))
        else:
            raise Exception(f"Invalid locator: {locator}")

    def login_functionality(self, username, password, message):
        welcome = None
        errormsg = None
        self.driver.find_element_by_id(Locators.usernameId).send_keys(username)
        self.driver.find_element_by_id(Locators.passwordId).send_keys(password)
        self.wait_for_element_clickable(locator='xpath', path=Locators.loginBtnXpath).click()
        if WebDriverWait(self.driver, 10).until(ec.alert_is_present()):
            self.accept_alert()
        welcome = self.driver.find_element_by_xpath(Locators.welcomePgXpath)
        if message == 'Success':
            assert welcome.text == 'Welcome: ACXMANAGER'
            assert errormsg == None

            # Todo : add for invisibility of element

    def submit_button(self):
        self.wait_for_element_visible(locator='xpath', path=Locators.submitBtnXpath).click()
        # self.driver.find_element_by_xpath(Locators.submitBtnXpath).click()
        self.accept_alert()

    def unlock_tg(self):
        self.wait_for_element_visible(locator='id', path=Locators.unlockBtnId).click()
        # self.driver.find_element_by_id(Locators.unlockBtnId).click()
        self.accept_alert()

    def accept_alert(self, message=None):
        alert = Alert(self.driver)
        if message:
            alert.send_keys(message)
        alert.accept()

    def sip_local_gateway(self):
        self.driver.find_element_by_xpath(Locators.localGtwId).click()
        self.driver.find_element_by_xpath(Locators.gatewayImg).click()
        sip_lgw_obj = self.driver.find_element_by_id(Locators.gatewaynameId)
        Select(sip_lgw_obj).select_by_visible_text(Locators.sipGtwName)
        self.submit_button()

    def sipi_local_gateway(self):
        self.driver.find_element_by_xpath(Locators.localGtwId).click()
        self.driver.find_element_by_xpath(Locators.gatewayImg).click()
        sipi_lgw_obj = self.driver.find_element_by_id(Locators.gatewaynameId)
        Select(sipi_lgw_obj).select_by_visible_text(Locators.sipiGtwName)
        self.submit_button()

    def sip_tg_types(self, tg_name="SIPI-Ing"):
        self.driver.find_element_by_link_text(Locators.tgLinkTest).click()
        # available_tgs = self.driver.find_elements_by_xpath(Locators.tgNamePath.replace("***", tg_name))
        # if available_tgs:
            # tg_name = tg_name + "_" + str(round(time.time()))

        try:
            self.driver.find_element_by_xpath(Locators.tgNamePath.replace("***", tg_name))
            print("create TG with new name")
            tg_name = tg_name + "_" + str(round(time.time()))
        except Exception:
            pass
        self.driver.find_element_by_xpath(Locators.createTgXpath).click()
        selectInput = self.driver.find_element_by_xpath(Locators.selectXpath)
        Select(selectInput).select_by_visible_text("SIP")
        self.driver.find_element_by_id(Locators.tgNameId).send_keys(tg_name)
        inputCountry = self.driver.find_element_by_id(Locators.countryId)
        Select(inputCountry).select_by_visible_text("India")
        self.wait_for_element_visible(locator='name', path=Locators.ipConfigName).click()
        # self.driver.find_element_by_name(Locators.ipConfigName).click()
        self.driver.find_element_by_id(Locators.gatewayId).send_keys('10.10.10.22')
        self.driver.find_element_by_id(Locators.gatewayPortId).send_keys('2007')
        self.submit_button()
        self.unlock_tg()
        self.sip_local_gateway()

    def sipi_tg_types(self,tg_name="SIPI-Egr"):

        self.driver.find_element_by_link_text(Locators.tgLinkTest).click()
        try:
            self.driver.find_element_by_xpath(Locators.tgNamePath.replace("***",tg_name))
            print("Create TG with new name")
            tg_name = tg_name + "_" + str(round(time.time()))
        except Exception:
            pass

        self.driver.find_element_by_link_text(Locators.tgLinkTest).click()
        self.driver.find_element_by_xpath(Locators.createTgXpath).click()
        selectInput = self.driver.find_element_by_xpath(Locators.selectXpath)
        Select(selectInput).select_by_visible_text("SIP")
        self.driver.find_element_by_id(Locators.tgNameId).send_keys(tg_name)
        inputCountry = self.driver.find_element_by_id(Locators.countryId)
        Select(inputCountry).select_by_visible_text("India")
        self.wait_for_element_visible(locator='name', path=Locators.ipConfigName).click()
        # self.driver.find_element_by_name(Locators.ipConfigName).click()
        self.driver.find_element_by_id(Locators.gatewayId).send_keys(Locators.sipiGtwIP)
        self.driver.find_element_by_id(Locators.gatewayPortId).send_keys(Locators.sipiGtwPort)
        tg_type = self.driver.find_elements_by_name(Locators.tgTypeName)
        for tg in tg_type:
            if tg.get_attribute('value') == 'I':
                tg.click()
        self.submit_button()
        self.unlock_tg()
        self.driver.find_element_by_xpath(Locators.sipIsupParXpath).click()
        self.driver.find_element_by_xpath(Locators.nextImgXpath).click()
        self.wait_for_element_clickable(locator='xpath', path=Locators.sipibehaviorXpath).click()
        param_val_obj = self.driver.find_element_by_id(Locators.paramValId)
        Select(param_val_obj).select_by_visible_text(Locators.paramValText)
        self.submit_button()
        self.driver.find_element_by_link_text(Locators.egrSipiMaptext).click()
        self.driver.find_element_by_xpath(Locators.isupEtsiXpath).click()
        self.submit_button()
        self.driver.find_element_by_xpath(Locators.detailsParxpah).click()
        self.sipi_local_gateway()

    def switch_to_new_window(self,parent_window,title):
        flag = False
        handles = self.driver.window_handles
        print("handles: ",handles)
        for handle in handles:
            if handle != parent_window:
                self.driver.switch_to_window(handle)
                if title in self.driver.title:
                    flag = True
                    break

        if not flag:
            raise Exception("Wrong window")

    def create_plan_policies(self):
        self.wait_for_element_clickable(locator='xpath',path=Locators.policiesPath).click()
        plan_policies_obj = self.driver.find_element_by_id(Locators.planPloicId)
        ActionChains(self.driver).move_to_element(plan_policies_obj).perform()

    def sip_pofiler(self):
        self.driver.find_element_by_id(Locators.profilesId).click()
        self.driver.find_element_by_xpath(Locators.sipProfierPath).click()
        parent_handle = self.driver.current_window_handle
        title = "Dialogic - Sip Profiler Configuration"
        self.switch_to_new_window(parent_handle,title)











    def close_browser(self):
        pass

    def quit_browser(self):
        pass

    # todo : check diff betn close and quit browser

class Locators:
    # login page
    loginPath = "http://192.168.201.8/apex/f?p=1000:101:1581531011352939::::FAPP_CALLER_APP,FAPP_CALLER_PAGE:1001,3"
    usernameId = "P101_USERNAME"
    passwordId = "P101_PASSWORD"
    loginBtnXpath = '//button[@value="Login"]'
    welcomePgXpath = '//*[@class="app-user"]'


    # Create TG page
    tgLinkTest = 'Trunk Groups (TG)'
    createTgXpath = '//*[@class="topbar"]//img'
    selectXpath = '//*[@class="selectlist"]'
    tgNameId = 'P2_CLLI_NAME'
    countryId = 'TC_ID'
    ipConfigName = 'IP Configuration'
    gatewayId = 'P2_RGW_IP_ADDRESS'
    gatewayPortId = 'P2_RGW_PORT'

    # Sip TG IP/PORT
    sipTgNameKeys = 'SIP-Barada-Egr'
    gatewayIpKeys = '10.10.10.22'
    gatewayPortKeys = '2009'
    tgNamePath = "//a[text()='***']"

    # Policies/Plan and Policies/Routing

    policiesPath = '//*[text()="Policies"]'
    planPloicId = "P_PLAN_AND_POLICIES"
    routingPath = '//*[text()="Routing"]'
    servTrigPath = '//*[text()="Service Trigger"]'
    antiFraudPath = '//*[text()="Anti-Fraud"]'

    # SIPI TG IP/PORT

    sipiTgNameKeys = 'SIPI-Ing'
    sipiGtwPort = '1123'
    sipiGtwIP = '10.10.10.22'
    tgTypeName = 'f01'
    sipIsupParXpath = '//*[text()="SIP-ISUP Parameters"]'
    nextImgXpath = '//*[@class="pagination"]//img'
    sipibehaviorXpath = '//*[text()="OutCall - SIP-I Behavior"]'
    paramValId = 'P91_CHAR_VALUE'
    paramValText = 'Always SIP-I'
    egrSipiMaptext = 'Egress SIP-I mapping'
    isupEtsiXpath = '//a[text()="ISUP-ETSI"]'
    detailsParxpah = '//*[text()="Detail"]'

    # SIP Profiler

    profilesId = 'I_PROFILES'
    sipProfierPath = '//*[text()="SIP Profiler"]'
    uploadProfId= 'btn-addSipProfiler'
    fileId = 'filepc'
    profNamePath = '//*[@class="popup-tbox FormElement ui-widget-content ui-corner-all"]'
    saveBtnId = 'btnSave'
    createProfId = 'btn-createSipProfiler'
    profNameId = 'profilerName'
    parameterNameId = 'p_1_1'
    settingImgPath = '//*[@id="c_p_1_1"]/img'
    attributesFiledId = 'p_1_1_c_Field'
    operatorId = 'o_1_1'
    valueId = 'v_1_1'
    valueSettingImgPath = '//*[@id="c_v_1_1"]/img'
    nextBtnImgPath = '//*[@id="nextPButton"]//img'












    # Submit Button
    submitBtnXpath = '//*[@id="jam"] '
    unlockBtnId = 'Unlock'

    # Local Gateway
    localGtwId = '//*[text()="Local Gateways"]'
    gatewayImg = '//*[@class="topbar-content"]//img'
    gatewaynameId = 'P132_LGW_NAME'
    sipGtwName = 'LGW1'
    sipiGtwName = 'LGW-SPICE1'



    #





    #welcome page
    tgname_id = ""
    sipIpath = ""









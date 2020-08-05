from selenium import webdriver
import geckodriver_autoinstaller
from webdriverdownloader import GeckoDriverDownloader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
import time

# creating dataframe for data extract
df = pd.DataFrame(
    columns=['IFG/FPC', 'Consumer Unit', 'Qty1', 'Length_1', 'Width_1', 'Height_1', 'Gross_weight_1', 'Net_weight_1',
             'Inner Pack', 'Qty2', 'Length_2', 'Width_2', 'Height_2', 'Gross_weight_2', 'Net_weight_2', 'Customer Unit',
             'Qty3', 'Length_3',
             'Width_3', 'Height_3', 'Gross_weight_3', 'Net_weight_3', 'Pallet Layer', 'Qty4', 'Length_4', 'Width_4',
             'Height_4', 'Gross_weight_4',
             'Net_weight_4', 'Pallet', 'Qty5', 'Length_5', 'Width_5', 'Height_5', 'Gross_weight_5', 'Net_weight_5',
             'Pallet EU Gross weight w/o\' Pallet', 'Qty6', 'Length_6', 'Width_6', 'Height_6', 'Gross_weight_6',
             'Net_weight_6', 'Related Master', 'Transition FPC', 'TransitionCAS'])
# scodes are list of IFG/FPC materials which will be loaded from excel file
# for now all focus was directed at Selenium stuff, so I provide test 10 elements in simple list
scodes = ['82445757', '82458207', '82458210', '82458271', '82458732', '82459554',
          '82459558', '82459720', '82459721', '82459731']
# we assume, that user will have Geckodriver delivered in .exe file with application
# for testing purposes we exclude Geckodriver downloading stuff
# because it's not known if client's VPN will interact with github properly

# gdd = GeckoDriverDownloader()
# paths = gdd.download_and_install()
# try:
#     gecko_path = paths[0]
# except:
#     gecko_path = paths[1]

# driver = webdriver.Firefox(executable_path=gecko_path)

driver = webdriver.Firefox()
driver.get('http://3dspace.prosper.cotyinc.com/3dspace/')


# base frames in material search window
def frames_base():
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.NAME, 'content')))
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.NAME, 'detailsDisplay')))
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.NAME, 'portalDisplay')))


# frames of Properties window where loop searches for IFG item
def properties_frames():
    driver.switch_to.default_content()
    WebDriverWait(driver, 30).until(
        EC.frame_to_be_available_and_switch_to_it((By.NAME, 'windowShadeFrame')))
    WebDriverWait(driver, 30).until(
        EC.frame_to_be_available_and_switch_to_it((By.NAME, 'structure_browser')))


driver.implicitly_wait(30)

# logging into system, main window, for now automated
# but possibly, client would want to get login window and automate only after this point
login_ele = driver.find_element_by_xpath(
    "//input[@name='username']").send_keys('login')
pass_ele = driver.find_element_by_xpath(
    "//input[@name='password']").send_keys('password')
log_in = driver.find_element_by_xpath("//input[@type='submit']").click()

# 'All' searching button despite 'Search for code'
search_list = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@id='AEFGlobalFullTextSearch']//a[@href='#']"))).click()
types_list = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
    (By.XPATH, "//a[@id='AEFTypesGlobalSearch']"))).click()
all_search = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[contains(text(), 'All...')]"))).click()

for scode in scodes:
    driver.find_element_by_xpath(
        "//input[@id='GlobalNewTEXT']").send_keys('%s' % scode)
    driver.find_element_by_xpath("//a[@class='btn search']").click()
    driver.implicitly_wait(100)
    # switching to frame with IFG items
    properties_frames()
    # searching for individual finished good positioning
    # looking for right code and conditional enter if same as scode
    correctness = []
    # ifg_check is checking number of row containing Invidivual Finished Good
    # ifg_text is text value of item in n-th row from ifg_check to compare with searched material
    ifg_check = driver.find_element_by_xpath(
        "//td[@title='Individual Finished Good']").get_attribute('rmbrow')
    ifg_text = driver.find_element_by_xpath(
        "//td[@rmbrow='%s']" % ifg_check).text.strip()
    # ifg_element - element containing IF to be clicked further
    properties_frames()
    time.sleep(1)
    properties_frames()
    ifg_element = driver.find_element_by_xpath(
        "//td[@rmbrow='%s']/a[1]" % ifg_check).click()
    # if searched material is same as IF number it was IFG
    # if not, it could be FPC, must be checked in item properties
    # it decides if we proceed further data scraping
    if ifg_text == scode:
        correctness.append('Yes')
    else:
        frames_base()
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, 'coty_ProductSpecsPropertiesPage')))
        fpc_check = driver.find_element_by_xpath(
            "//tr[@id='calc_coty_TransitionFPCNotEditable']//td[@class='field']")
        if fpc_check.text == scode:
            correctness.append('Yes')
        else:
            correctness.append('No')
    print(correctness)
    # continue if IFG/FPC is ok, if number not matched in system, comment added to dataframe
    if 'No' in correctness:
        df = df.append({'IFG/FPC': scode, 'Consumer Unit': 'Please check if IFG/FPC number is correct'},
                       ignore_index=True)
    else:
        frames_base()
        driver.find_element_by_xpath('//td[@title="Spec View"]').click()
        # searching for position of each Component in 'Weight and Dimensions' table
        # collecting related data to dataframe
        frames_base()
        driver.implicitly_wait(10)
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, 'CPNProductDataViewAttribute')))

        cons_unit = str(int(driver.find_element_by_xpath(
            "//*[contains(text(), 'Consumer Unit')]/following-sibling::td/following-sibling::td").text.strip()) + 1)
        inner_pack = str(int(driver.find_element_by_xpath(
            "//*[contains(text(), 'Inner Pack')]/following-sibling::td/following-sibling::td").text.strip()) + 1)
        cust_unit = str(int(driver.find_element_by_xpath(
            "//*[contains(text(), 'Customer Unit')]/following-sibling::td/following-sibling::td").text.strip()) + 1)
        pal_layer = str(int(driver.find_element_by_xpath(
            "//*[contains(text(), 'Pallet Layer')]/following-sibling::td/following-sibling::td").text.strip()) + 1)
        # pallet = str(int(driver.find_element_by_xpath("//*[contains(text(), 'Pallet ')]/following-sibling::td/following-sibling::td").text.strip()) + 1)
        pal_eu = str(int(driver.find_element_by_xpath(
            "//*[contains(text(), 'Pallet EU Gross Weight w/o Pallet')]/following-sibling::td/following-sibling::td").text.strip()) + 1)
        # I was not able to get into pallet item data so for now
        # I give attribute 6 like the most possible occurence during testing
        pallet = '6'

        # variables to be extracted per each component

        cons = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[1]" % cons_unit).text.strip()
        q_one = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[4]" % cons_unit).text.strip()
        l_one = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[5]" % cons_unit).text.strip()
        w_one = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[6]" % cons_unit).text.strip()
        h_one = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[7]" % cons_unit).text.strip()
        gw_one = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[8]" % cons_unit).text.strip()
        nw_one = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[9]" % cons_unit).text.strip()

        inner = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[1]" % inner_pack).text.strip()
        q_two = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[4]" % inner_pack).text.strip()
        l_two = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[5]" % inner_pack).text.strip()
        w_two = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[6]" % inner_pack).text.strip()
        h_two = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[7]" % inner_pack).text.strip()
        gw_two = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[8]" % inner_pack).text.strip()
        nw_two = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[9]" % inner_pack).text.strip()

        cust = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[1]" % cust_unit).text.strip()
        q_three = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[4]" % cust_unit).text.strip()
        l_three = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[5]" % cust_unit).text.strip()
        w_three = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[6]" % cust_unit).text.strip()
        h_three = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[7]" % cust_unit).text.strip()
        gw_three = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[8]" % cust_unit).text.strip()
        nw_three = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[9]" % cust_unit).text.strip()

        pallay = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[1]" % pal_layer).text.strip()
        q_four = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[4]" % pal_layer).text.strip()
        l_four = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[5]" % pal_layer).text.strip()
        w_four = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[6]" % pal_layer).text.strip()
        h_four = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[7]" % pal_layer).text.strip()
        gw_four = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[8]" % pal_layer).text.strip()
        nw_four = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[9]" % pal_layer).text.strip()

        pal = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[1]" % pallet).text.strip()
        q_five = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[4]" % pallet).text.strip()
        l_five = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[5]" % pallet).text.strip()
        w_five = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[6]" % pallet).text.strip()
        h_five = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[7]" % pallet).text.strip()
        gw_five = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[8]" % pallet).text.strip()
        nw_five = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[9]" % pallet).text.strip()

        paleu = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[1]" % pal_eu).text.strip()
        q_six = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[4]" % pal_eu).text.strip()
        l_six = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[5]" % pal_eu).text.strip()
        w_six = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[6]" % pal_eu).text.strip()
        h_six = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[7]" % pal_eu).text.strip()
        gw_six = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[8]" % pal_eu).text.strip()
        nw_six = driver.find_element_by_xpath(
            "//table[@id='coty_PackingIndividualCharacteristicList']/tbody[1]/tr[%s]/td[9]" % pal_eu).text.strip()

        # appending line regarding correct IFG/FPC item to dataframe which will be transfered to user's Excel
        # in next steps
        df = df.append({'IFG/FPC': scode, 'Consumer Unit': cons, 'Qty1': q_one, 'Length_1': l_one, 'Width_1': w_one,
                        'Height_1': h_one, 'Gross_weight_1': gw_one, 'Net_weight_1': nw_one,
                        'Inner Pack': inner, 'Qty2': q_two, 'Length_2': l_two, 'Width_2': w_two, 'Height_2': h_two,
                        'Gross_weight_2': gw_two, 'Net_weight_2': nw_two,
                        'Customer Unit': cust, 'Qty3': q_three, 'Length_3': l_three, 'Width_3': w_three,
                        'Height_3': h_three, 'Gross_weight_3': gw_three, 'Net_weight_3': nw_three,
                        'Pallet Layer': pallay, 'Qty4': q_four, 'Length_4': l_four, 'Width_4': w_four,
                        'Height_4': h_four, 'Gross_weight_4': gw_four, 'Net_weight_4': nw_four,
                        'Pallet': pal, 'Qty5': q_five, 'Length_5': l_five, 'Width_5': w_five, 'Height_5': h_five,
                        'Gross_weight_5': gw_five, 'Net_weight_5': nw_five,
                        'Pallet EU Gross weight w/o\' Pallet': paleu, 'Qty6': q_six, 'Length_6': l_six,
                        'Width_6': w_six, 'Height_6': h_six, 'Gross_weight_6': gw_six, 'Net_weight_6': nw_six},
                       ignore_index=True)

        def remove_string(x):
            df[x] = df[x].str.replace('[a-zA-Z]', '', regex=True).str.strip()

        for column in ['Qty1', 'Length_1', 'Width_1', 'Height_1', 'Gross_weight_1', 'Net_weight_1',
                       'Qty2', 'Length_2', 'Width_2', 'Height_2', 'Gross_weight_2', 'Net_weight_2', 'Qty3', 'Length_3',
                       'Width_3', 'Height_3', 'Gross_weight_3', 'Net_weight_3', 'Qty4', 'Length_4', 'Width_4',
                       'Height_4',
                       'Gross_weight_4', 'Net_weight_4', 'Qty5', 'Length_5', 'Width_5', 'Height_5', 'Gross_weight_5',
                       'Net_weight_5',
                       'Qty6', 'Length_6', 'Width_6', 'Height_6', 'Gross_weight_6', 'Net_weight_6']:
            remove_string(column)

        driver.switch_to.default_content()
        driver.find_element_by_xpath(
            "//input[@id='GlobalNewTEXT']").send_keys(Keys.BACKSPACE)

# after loop steps and filling dataframe, the next steps should be
# interact with user's excel file from which we have loaded list of IFG/FPC scodes
# then fill the sheet with extracted data and try to run VBA macro created by Roman Lareniuk from COTY

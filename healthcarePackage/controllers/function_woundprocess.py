from controllers import config, login, servers, function_mdo, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import pyautogui, sys
#import autoit
import os
from selenium.webdriver.common.action_chains import ActionChains


todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")

def addwoundoasis(
        woundtype, 
        woundlocation
        ):
        
    #editbtn = config.driver.get('//*[@id="titleNoteBar"]/div[4]/div[2]/button').click()
    integendo = config.driver.find_element_by_xpath('//*[@id="integumentary"]').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,500)")
 
    time.sleep(3)
    woundyes = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/label/input').click()
    woundplus =  config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[6]/td/table/tbody/tr/td[4]/div/a').click()
    time.sleep(3)
    
    
    wound_type = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[3]/div/div[1]/input')
    wound_type.click()
    wound_type.send_keys(woundtype)
    time.sleep(2)
    
    woundloc = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[5]/div/div[1]/input')
    woundloc.click()
    woundloc.send_keys(woundlocation)
    time.sleep(2)
    
    woundcomment = config.driver.find_element_by_xpath('//*[@id="integForm"]/fieldset/div[1]/table[1]/tbody/tr[7]/td/table/tbody/tr/td[7]/input').send_keys('Added from automated testing.')
    time.sleep(2)
    
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button[3]').click()
    time.sleep(5)
    
    assessnow = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()
    
    
def dragpin():
    time.sleep(3)
    
    source1 = config.driver.find_element_by_xpath('//*[contains(@id, "pinid")]')
    #source1 = config.driver.find_element_by_xpath('//*[@id="pinid1"]')
    target1 = config.driver.find_element_by_xpath('//*[@id="dragball"]/div')
    time.sleep(5)
    actions2 = ActionChains(config.driver)
    time.sleep(5)
    actions2.drag_and_drop(source1, target1).perform()
    time.sleep(5)
    

def completewoundassessment(
        stages, 
        grantissue, 
        nectissue, 
        granneccoverage, 
        exuamount, 
        exutype, 
        edges, 
        periwoundtissue, 
        healingstatus, 
        woundrelatedpain
        ):
    
    time.sleep(3)
     

    scrolldown = config.driver.execute_script("window.scrollTo(0,1000)")
    
    time.sleep(6)
    
    # --- Click the dropdown
    # --- Get all data on dropdown
    # --- Select the option
    
    # Stages
    stages_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//input').click()
    stages_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[6]//li[contains(string(), "'+ stages +'")]').click()
    
    time.sleep(2)
    
    # Granulation Tissue
    grantissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]//input').click()
    grantissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[7]//li[contains(string(), "'+ grantissue +'")]').click()
    
    # Necrotic Tissue
    nectissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]//input').click()
    nectissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[8]//li[contains(string(), "'+ nectissue +'")]').click()
    
    # Granulation and Necrosis Coverage
    granneccoverage_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]//input').click()
    granneccoverage_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[9]//li[contains(string(), "'+ granneccoverage +'")]').click()
    
    # Exudate Amount
    exuamount_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]//input').click()
    exuamount_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[10]//li[contains(string(), "'+ exuamount +'")]').click()
    
    # Exudate Type
    exutype_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]//input').click()
    exutype_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[11]//li[contains(string(), "'+ exutype +'")]').click()
    
    # Edge Type
    edges_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]//input').click()
    edges_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[12]//li[contains(string(), "'+ edges +'")]').click()
    
    
    # Healing Status
    healingstatus_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]//input').click()
    healingstatus_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[14]//li[contains(string(), "'+ healingstatus +'")]').click()
    
    # Wound Related Pain 
    woundrelatedpain_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]//input').click()
    woundrelatedpain_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[15]//li[contains(string(), "'+ woundrelatedpain +'")]').click()
    
    
    # Periwound Tissue 
    periwoundtissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]/table-column-periwound/div/div[2]/div[1]').click()
    periwoundtissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div/div/table-column/ul/li[13]//li[contains(string(), "'+ periwoundtissue +'")]').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")
    
    time.sleep(2)
    
    
    # Upload Function
    # -- 1. find the wound.png file path
    # -- 2. Click upload Element
    # -- 3. use autoit function for upload -- import autoit
    
    woundimage = os.getcwd()+"\wound.png"
    print(woundimage)
    upload = config.driver.find_element(By.XPATH, '//*[@id="myImg"]').click()
    time.sleep(5)
    #autoit.control_set_text("Open","Edit1", woundimage)
    #time.sleep(5)
    #autoit.control_send("Open","Edit1","{ENTER}")
    autoit.control_send("[CLASS:#32770;TITLE:Open]", "Edit1", woundimage)
    autoit.control_click("[CLASS:#32770;TITLE:Open]", "Button1")


def digitalmeasurement():
    time.sleep(10)
    digitalmesbtn = config.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[3]/div[2]/div[2]/span/div/div/a').click()
    time.sleep(15)
    scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")
    editdigitalmesbtn =  config.driver.find_element_by_xpath('//*[@id="onProcessFalse-0-0"]/div[3]/div[2]/div[2]/span/div/div/a').click()
    time.sleep(8)
    
    #displaygrid = config.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div/div[2]/div/div/table/tbody/tr/td[2]/table[2]/tbody/tr[1]/td/fieldset/label/input').click()
    displaygrid = config.driver.find_element_by_name('grid.show').click()
    
    time.sleep(3)
    pyautogui.click(884, 359)
    pyautogui.click(826, 362)
    pyautogui.click(777, 378)
    pyautogui.click(731, 392)
    pyautogui.click(683, 412)
    pyautogui.click(639, 433)
    pyautogui.click(594, 466)
    pyautogui.click(562, 513)
    pyautogui.click(553, 566)
    pyautogui.click(568, 618)
    pyautogui.click(590, 655)
    pyautogui.click(623, 693)
    pyautogui.click(682, 718)
    pyautogui.click(743, 742)
    pyautogui.click(816, 754)
    pyautogui.click(896, 756)
    pyautogui.click(963, 744)
    pyautogui.click(1027, 726)
    pyautogui.click(1097, 694)
    pyautogui.click(1168, 645)
    pyautogui.click(1216, 597)
    pyautogui.click(1238, 544)
    pyautogui.click(1230, 481)
    pyautogui.click(1200, 435)
    pyautogui.click(1150, 393)
    pyautogui.click(1080, 365)
    pyautogui.click(1016, 356)
    pyautogui.click(958, 356)
    pyautogui.click(884, 359)
    time.sleep(5)
    
    gran = config.driver.find_element_by_xpath('/html/body//div/div/form/div/div[2]/div/div/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td/input[2]').send_keys('80')
    time.sleep(3)
    
    savemeasurementbtn = config.driver.find_element_by_xpath('/html/body//div/div/form/div/div[2]/div/div/table/tbody/tr/td[2]/div[3]/button[2]').click()
    time.sleep(3)
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,0)")
    
    # Save Assessment
    time.sleep(3)
    savewoundbtn = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/td[2]/button').click()
    
def woundanalytics():
    
    time.sleep(5)
    scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")
    time.sleep(3)
    woundanalyticsbtn =  config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/data/form/div/fieldset/div/div/div/div/div[2]/span').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")
    time.sleep(3)
    
    previewreport = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td[2]/div').click()
    time.sleep(3)
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")
    time.sleep(5)
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,0)")
    time.sleep(5)
    
    prntreport = config.driver.find_element_by_xpath('//*[@id="createRpt"]').click()
    
    time.sleep(10)
    
    pyautogui.keyDown('ctrl') # hold ctrl key
    pyautogui.press('s') # press s key
    pyautogui.keyUp('ctrl') # release ctrl key
    pyautogui.press('enter')
    
    time.sleep(3)
    autoit.control_send("Save As","Edit1","{ENTER}")
    

def addwounddirectly(
        woundtype, 
        woundlocation
        ):
    scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")
    
    time.sleep(3)
    patient_dashboard.gettab("woundmanagement")
    time.sleep(3)
    
    #click the first wound visit and click edit button
    firstwoundass = config.driver.find_element_by_xpath('//*[@id="table-responsive"]/table/tbody[2]/tr').click()
    time.sleep(3)
    editbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td[2]/button').click()
    
    time.sleep(3)
    
    # --- Mouse locator based on the selected wound location 
    if woundlocation == "Buttock (R)":
        buttock_r = pyautogui.click(1062, 798)
        
    elif woundlocation == "Buttock (L)":
        buttock_l = pyautogui.click(1005, 788) 
        
    elif woundlocation == "Sacrum":
        sacrum = pyautogui.click(1035, 783) 
        
    elif woundlocation == "Coccyx":
        coccyx = pyautogui.click(1035, 801)
        
    elif woundlocation == "Trochanter (R)":
        trochanter_r = pyautogui.click(851, 805)
        
    elif woundlocation == "Trochanter (L)":
        trochanter_l = pyautogui.click(767, 807)
         
    elif woundlocation == "Ischial tuberosity (R)":
        ischialtuberosity_r = pyautogui.click(819, 815) 
        
    elif woundlocation == "Ischial tuberosity (L)":
        ischialtuberosity_l = pyautogui.click(794, 818)
        
    elif woundlocation == "Lateral ankle (R)":
        lateralankle_r = pyautogui.click(1055, 1002)
        
    elif woundlocation == "Lateral ankle (L)":
        lateralankle_r = pyautogui.click(1017, 999)
        
    elif woundlocation == "Medial ankle (R)":
        medialankle_r = pyautogui.click(875, 1003)
         
    elif woundlocation == "Medial ankle (L)":
        medialankle_r = pyautogui.click(787, 1001) 
        
    elif woundlocation == "Heel (R)":
        heel_r = pyautogui.click(950, 984)
        
    elif woundlocation == "Heel (L)":
        heel_l = pyautogui.click(887, 985)
        
    elif woundlocation == "Plantar":
        plantar = pyautogui.click(948, 935) 
        
    elif woundlocation == "Toes":
        toes = pyautogui.click(1136, 920) 
        
    elif woundlocation == "Abdomen":
        abdomen = pyautogui.click(807, 753)
        
    elif woundlocation == "Groin":
        groin = pyautogui.click(807, 808)   
    
    pinyes = config.driver.find_element_by_xpath('//*[@id="coorask"]/div/button[1]').click()
    
    time.sleep(3)
    
    # wound location
    woundloc_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[3]//input').click()
    woundloc_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[3]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[3]//li[contains(string(), "'+ woundlocation +'")]').click()
    
    # wound Type
    woundtype_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[4]//input').click()
    woundtype_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[4]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[4]//li[contains(string(), "'+ woundtype +'")]').click()
    
    """ # Stages
    stages_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[6]/span/table-inputs/div/div[1]/input').click()
    stages_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[6]/span/table-inputs/div/div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[6]/span/table-inputs/div/div[2]/ul/li[contains(string(), "'+ stages +'")]').click()
    time.sleep(2)
    
    # Granulation Tissue
    grantissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[7]/span/table-inputs/div/div[1]/input').click()
    grantissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[7]/span/table-inputs/div/div[2]').text
    time.sleep(2)
    print(grantissue_items)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/table-column/ul/li[7]//li[contains(string(), "'+ grantissue +'")]').click()
    
    # Necrotic Tissue
    nectissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[8]//input').click()
    nectissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[8]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[8]//li[contains(string(), "'+ nectissue +'")]').click()
    
    # Granulation and Necrosis Coverage
    granneccoverage_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[9]//input').click()
    granneccoverage_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[9]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[9]//li[contains(string(), "'+ granneccoverage +'")]').click()
    
    # Exudate Amount
    exuamount_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[10]//input').click()
    exuamount_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[10]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[10]//li[contains(string(), "'+ exuamount +'")]').click()
    
    # Exudate Type
    exutype_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[11]//input').click()
    exutype_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[11]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[11]//li[contains(string(), "'+ exutype +'")]').click()
    
    # Edge Type
    edges_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[12]//input').click()
    edges_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[12]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[12]//li[contains(string(), "'+ edges +'")]').click()
    
    
    # Healing Status
    healingstatus_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[14]//input').click()
    healingstatus_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[14]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[14]//li[contains(string(), "'+ healingstatus +'")]').click()
    
    # Wound Related Pain 
    woundrelatedpain_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[15]//input').click()
    woundrelatedpain_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[15]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[15]//li[contains(string(), "'+ woundrelatedpain +'")]').click()
    
    
    # Periwound Tissue 
    periwoundtissue_dd = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[13]/table-column-periwound/div/div[2]/div[1]').click()
    periwoundtissue_items = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[13]//div[2]').text
    time.sleep(2)
    finditem = config.driver.find_element_by_xpath('//*[@id="goTabSection"]/div/woundcare-table/div[2]/div[2]/div[2]/div/div/table-column/ul/li[13]//li[contains(string(), "'+ periwoundtissue +'")]').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,5000)") """
    
    time.sleep(2)
   
   
    
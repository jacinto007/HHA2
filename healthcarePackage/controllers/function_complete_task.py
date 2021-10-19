from controllers import config, login, servers, function_mdo
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
    

#functions based from complete_task

def skillednursing(
        ti,
        to,
        vstemp,
        vspulse,
        vsres,
        vslasys,
        vsladyl,
        vso2room,
        vso2o2,
        vso2lpm,
        vsbs
        ):
    time.sleep(3)
    print('skilled nursing')
    
     #Tab button
    vssensoryintegendo = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[1]')
    cardionutrielim = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[2]')
    neuromusculo = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[3]')
    caremaninterv = config.driver.find_element_by_xpath('//*[@id="oasis-tabs"]/label[4]')
    
    # time in and out
    timein = config.driver.find_element_by_name("timeIn").send_keys(ti)
    timeout = config.driver.find_element_by_name("timeOut").send_keys(to)
    
    time.sleep(5)
        
    vs_temp = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/div/input').send_keys(vstemp)
    vs_temp_scan = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[1]/td[3]/div[2]/label[2]/input').click() #scan
        
    vs_pulse = config.driver.find_element_by_name("VS0003").send_keys(vspulse)
    vs_pulse_radial = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[2]/td[3]/div[2]/label[1]/input').click()
    vs_res = config.driver.find_element_by_name("VS0006").send_keys(vsres)
        
    vs_lefta_sys = config.driver.find_element_by_name("VS0009").send_keys(vslasys)
    vs_lefta_dyl = config.driver.find_element_by_name("VS0057").send_keys(vsladyl)
    vs_lefta_sitting = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[4]/td[3]/div/label[1]/input').click()
        
    vs_o2room = config.driver.find_element_by_name("VS0021").send_keys(vso2room)
    vs_o2o2 = config.driver.find_element_by_name("VS0022").send_keys(vso2o2)
    vs_o2lpm = config.driver.find_element_by_name("VS0023").send_keys(vso2lpm)
        
    vs_bs = config.driver.find_element_by_name("VS0024").send_keys(vsbs)
    vs_bs_rbs = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[10]/td[3]/div[2]/label[2]/input').click()
        
    vs_weight_actual = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[11]/td[3]/div[2]/label[1]/input').click()
    vs_height_actual = config.driver.find_element_by_xpath('//*[@id="vital_signs"]/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/div/input').click()
        
    m1242_nopain = config.driver.find_element_by_xpath('//*[@id="pain_assessment"]/tbody/tr/td/div[1]/label/input').click()
      
    #All sensory status will be WNL
    ss_eyes_wnl = config.driver.find_element_by_xpath('//*[@id="sensory_assessment"]/tbody/tr[1]/td/div/div/label/input').click()
    ss_ear_wnl = config.driver.find_element_by_name("SENSORY0039").click()
    ss_mouth_wnl = config.driver.find_element_by_name("SENSORY0059").click() 
    ss_nose_wnl = config.driver.find_element_by_name("SENSORY0055").click() 
    ss_throat_wnl = config.driver.find_element_by_name("SENSORY0063").click() 
    ss_speech_wnl = config.driver.find_element_by_name("SENSORY0067").click() 
    ss_touch_wnl = config.driver.find_element_by_name("SENSORY0070").click() 
        
    integstat = config.driver.find_element_by_xpath('//*[@id="integumentary_status_temp"]/tbody/tr/th[2]/div[1]/div/label/input').click()
    scrolldown = config.driver.execute_script("window.scrollTo(0,6500)")
    time.sleep(3)
    items = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table/tbody/tr[5]/td/fieldset/table/tbody').text
    endosystem = items.split('\n')
    removeitem = {"Other"}
    endosystem = [ele for ele in endosystem if ele not in removeitem]
    for x in endosystem:
        finditem = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table/tbody/tr[5]/td/fieldset/table/tbody//label[contains(string(), "'+ x +'")]')
        finditem.click()
    
    # CADRIOPULMONARY/NUTRITION/ELIMINATION
    time.sleep(5)
    cardionutrielim.click()
    
    time.sleep(5)
    shortofbreath = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table[1]/tbody/tr/td/table[2]/tbody/tr/td[1]/div/label/input').click()
    resps_wnl = config.driver.find_element_by_xpath('//*[@id="respiratory"]/tr/td[2]/table/tbody/tr/td[2]/div/label/input').click()
    cardio_wnl = config.driver.find_element_by_xpath('//*[@id="cardiovascular_temp"]/tr/td[2]/table/tbody/tr/td[2]/div/label/input').click()
    uppergistat_wnl = config.driver.find_element_by_xpath('//*[@id="upper_gastrointestinal"]/tr/td[2]/div/label/input').click()
    lowergistat_wnl = config.driver.find_element_by_xpath('//*[@id="lower_gastrointestinal"]/tbody/tr/th[2]/div/div/label/input').click()
    genitostat_wnl = config.driver.find_element_by_xpath('//*[@id="genitourinary_status_temp"]/tbody/tr/th[2]/div/div/label/input').click()
    abnelim_no = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table[3]/tbody/tr[2]/td/table[3]/tbody/tr[1]/td[2]/label[1]/input').click()
    spx_no = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table[3]/tbody/tr[2]/td/table[4]/tbody/tr/td[2]/label/input').click()
    
    # NEUROLOGIC/MUSCULOSKELETAL
    time.sleep(5)
    neuromusculo.click()    
    time.sleep(5)
    neurostat_wnl = config.driver.find_element_by_xpath('//*[@id="neurological_status_temp"]/tbody/tr/th[2]/div/div/label/input').click()
    thought_wnl = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table/tbody/tr/td/table[4]/tbody/tr/th[2]/div[1]/div/label/input').click()
    musculo_wnl = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/fieldset/fieldset/div/div/table/tbody/tr/td/table[5]/tbody/tr/th[2]/div[1]/div/label/input').click()
    scrolldown = config.driver.execute_script("window.scrollTo(0,6500)")
        
    items = config.driver.find_element_by_xpath('//*[@id="activities permitted"]').text
    activitiespermitted = items.split('\n')
    removeitem = {"Other:  "}
    activitiespermitted = [ele for ele in activitiespermitted if ele not in removeitem]
    for x in activitiespermitted:
        finditem = config.driver.find_element_by_xpath('//*[@id="activities permitted"]//label[contains(string(), "'+ x +'")]')
        finditem.click()
        
    # CARE MANAGMENT/INTERVENTIONS
    time.sleep(5)
    caremaninterv.click()  
    time.sleep(5)
    items = config.driver.find_element_by_xpath('//*[@id="home_medication"]').text
    homemed = items.split('\n')
    removeitem = {"Medication discrepancy noted during this visit", "Oral medications (tablets/capsules) prepared in a pill box", "Use of medication schedule in taking medications"}
    homemed = [ele for ele in homemed if ele not in removeitem]
    for x in homemed:
        finditem = config.driver.find_element_by_xpath('//*[@id="home_medication"]//label[contains(string(), "'+ x +'")]')
        finditem.click()
    
    time.sleep(3)
    
    #save
    save = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[3]/div[2]/div/button[3]').click()
    
    
    
def rnskilledassesment(oasistask, visitdate):
    time.sleep(3)
    
    sadd = config.driver.find_element_by_xpath('/html/body//div/div/div/form/div/div/div[2]/div/fieldset/div/div[1]/div[2]/table/tbody/tr/td/div[2]/div/div/div/a').click()
    #/html/body/div[11]/div/div/div/form/div/div/div[2]/div/fieldset/div/div[1]/div[2]/table/tbody/tr/td/div[2]/div/div/div/a
    skilledassesmentask = config.driver.find_element_by_xpath('/html/body//div/div/div/form/div/div/div[2]/div/fieldset/div/div[1]/div[2]/table/tbody/tr/td/div[2]/div/div/div/div/ul//li[contains(string(), "'+ oasistask +'")]')
    skilledassesmentask.click()
    
    time.sleep(3)
    visitdateoasis = config.driver.find_element_by_xpath('//*[@id="visitdate"]').send_keys(visitdate)
    plannteddate = config.driver.find_element_by_xpath('//*[@id="taskdate"]').send_keys(visitdate)
    timein = config.driver.find_element_by_xpath('//*[@id="timein"]').send_keys(todaytime)
    timeout = config.driver.find_element_by_xpath('//*[@id="timeout"]').send_keys(plustime)
    
    time.sleep(3)
    
    savebtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Save")]').click()
    
    if oasistask == "RN - OASIS D1 Discharge from Agency":
        function_mdo.dischargeorder(visitdate)
        
    elif oasistask == "RN - OASIS D1 Recertification":
        function_mdo.recertorder(visitdate)

    
    
def rnjschhalvn():
    time.sleep(3)
    print('RN - Joint Supervisory (CHHA/LVN)')


def ptieval():
    time.sleep(3)
    print('PT - Initial Eval')

def ptvisit():
    time.sleep(3)
    print('PT - PT Visit')

def otieval():
    time.sleep(3)
    print('OT - Initial Eval')

def otvisit():
    time.sleep(3)
    print('OT - OTA Visit')

def stieval():
    time.sleep(3)
    print('ST - Initial Eval')

def stvisit():
    time.sleep(3)
    print('ST - ST Visit')

def mswass():
    time.sleep(3)
    print('MSW - Assessment - MSW - Follow-up Visit')

def chhavisit():
    time.sleep(3)
    print('CHHA - HHA Visit')

def oasisdcsummary(oasistask, visitdate):
    time.sleep(3)
    print('oasisdcsummary')
    function_mdo.transferorder(visitdate)

def oasisroc(oasistask, visitdate):
    time.sleep(3)
    print('oasisroc')
    function_mdo.rocorder(visitdate)














 
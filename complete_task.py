from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
    
# -----------------------------------------------------------------------
# FUNCTIONS FOR ALL TASKS GOES HERE this includes passing of variables
# -----------------------------------------------------------------------

def snv():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    #check the task if it's in progress on scheduled
    task = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a')

    taskstatus = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[3]/div/span').text
    print(taskstatus)

    if taskstatus == "In Progress":
        task.click()
        time.sleep(3)
        editbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[3]/div[2]/div/button').click() #edit button
        time.sleep(3)
        
    elif taskstatus == "Scheduled":
        task.click()
        time.sleep(3)

        
    vstemp = "97.4"
    vspulse = "85"
    vsres = "28"
    vslasys =  "117"
    vsladyl = "70"
    vso2room = "88"
    vso2o2 = "92"
    vso2lpm = "2"
    vsbs = "128"
    
    
    function_complete_task.skillednursing(
        todaytime,
        plustime,
        vstemp,
        vspulse,
        vsres,
        vslasys,
        vsladyl,
        vso2room,
        vso2o2,
        vso2lpm,
        vsbs
        )
    
    #discard changes
    #discardyes = config.driver.find_element_by_xpath('/html/body/div[13]/div/div/div/div/button[1]').click()
    
    time.sleep(2)
    
    patient_dashboard.gettab("task")


def rnjschhalvn():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    
    function_complete_task.rnjschhalvn()
    # code goes here -----------------


def ptieval():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    
    function_complete_task.ptieval()
    # code goes here -----------------


def ptvisit():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    
    function_complete_task.ptvisit()
    # code goes here -----------------
    
    
def otieval():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5) 
    
    function_complete_task.otieval()   
    # code goes here -----------------
    
    
def otvisit():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    
    function_complete_task.otvisit()    
    # code goes here -----------------
     
     
def stieval():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    
    function_complete_task.stieval()    
    # code goes here -----------------   
    
    
def stvisit():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)  
    
    function_complete_task.stvisit()  
    # code goes here ----------------- 
      
           
def mswass():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)    
    
    function_complete_task.mswass()
    # code goes here -----------------        
           
              
def chhavisit():
    time.sleep(5)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)    
    
    function_complete_task.chhavisit()
    # code goes here -----------------             
 
def oasisdcsummary(task, visitdate):
    time.sleep(5)
    function_complete_task.oasisdcsummary(task, visitdate)
    # code goes here -----------------        
           

def oasisroc(task, visitdate):
    time.sleep(5)
    function_complete_task.oasisroc(task, visitdate)
    # code goes here -----------------        
           
           
def rnskilledassesment(task, visitdate, rnskilledass):
    time.sleep(5)
    
    #Open newly created 
    current_scheduledtask = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]//a[contains(string(), "'+ task +'")]').click()
    
    #discharge = "RN - OASIS D1 Discharge from Agency"
    #recert = "RN - OASIS D1 Recertification"
    
    oasistask = rnskilledass #Change this option if you want to recert of discharge
    
    print(oasistask)
    print(visitdate)
    time.sleep(5)
    
    function_complete_task.rnskilledassesment(oasistask, visitdate)  
    
    
    
    
# -----------------------------------------------------------------------
# MAIN FUNCTION FOR COMPLETE TASK
# -----------------------------------------------------------------------

def completetask(task):
    
    time.sleep(5)
    
    rnskilledassesment = "RN - Skilled Assessment"
    oasisdcaegency = "RN - OASIS D1 Discharge from Agency"
    oasisdcnvisit = "RN - OASIS D1 Discharge Non-visit"
    oasisfollowup = "RN - OASIS D1 Other Follow-Up"
    oasistfrfdc = "RN - OASIS D1 Transfer (discharged)"
    oasistfrnotdc = "RN - OASIS D1 Transfer (not discharged)"
    oasisdcsummary = "RN - Discharge (Summary Only)"
    oasisroc = "RN - OASIS D1 Resumption of Care"

    lvnskilledvisit = "LVN/LPN - Skilled Visit"
    lvnwoundvisit = "LVN/LPN - Wound Visit"
    prnskilledvisit = "PRN - Skilled Visit"
    rneducvisit = "RN - Education Visit"
    rnivvisit = "RN - IV Visit"
    rnjschha = "RN - Joint Supervisory (CHHA)"
    rnjslvn = "RN - Joint Supervisory (LVN)"
    rnskilledvisit = "RN - Skilled Visit"
    rnsupvisit = "RN - Supervisory Visit"
    rnwoundvisit = "RN - Wound Visit"
    
    ptieval = "PT - Initial Eval"
    ptievalsoc = "PT - Initial Eval-SOC"
    ptvisit = "PT - PT Visit"
    ptavisit = "PTA - PTA Visit"
    
    otieval = "OT - Initial Eval"
    otievalsoc = "OT - Initial Eval-SOC"
    otvisit = "OT - OT Visit"
    otavisit = "OTA - OTA Visit"
    
    stieval = "ST - Initial Eval"
    stievalsoc = "ST - Initial Eval-SOC"
    stvisit = "ST - ST Visit"
    
    mswass = "MSW - Assessment"
    mswfollowup = "MSW - Follow-up Visit"
    chhavisit = "CHHA - HHA Visit"

    
    if (((task == rnwoundvisit or task == rnivvisit) or (task == lvnskilledvisit or task == lvnwoundvisit)) or ((task == prnskilledvisit or task == rneducvisit) or (task == rnskilledvisit or task == rnsupvisit))):
        snv()
        
    elif task == rnjschha or task == rnjslvn:
        rnjschhalvn()
        
    elif task == ptieval or task == ptievalsoc:
        ptieval()
        
    elif task == ptvisit or task == ptavisit:
        ptvisit()
        
    elif task == otieval or task == otievalsoc:
        otieval()
        
    elif task == otvisit or task == otavisit:
        otvisit()
    
    elif task == stieval or task == stievalsoc:
        stieval()
        
    elif task == stvisit:
        stvisit()
    
    elif task == mswass or task == mswfollowup:
        mswass()
        
    elif task == chhavisit:
        chhavisit()
    
    elif task == rnskilledassesment:
        rnskilledassesment(task)
    
    elif task == oasisdcsummary:
        oasisdcsummary()  
        
    elif task == oasisroc:
        oasisroc()  

    
    


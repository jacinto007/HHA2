from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, patient_dashboard, function_woundprocess
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import pyautogui, sys
#import autoit
import os
import pandas as pd
import random

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")

def complete_woundprocess(test_server, searchpatient):
    
    if test_server == "qa":
        servers.qaserver()
        config.driver.get("https://qado.medisource.com/patients/admitted")
        servers.searchpatientrecord(searchpatient)
        time.sleep(2)
        
    elif test_server == "live":
        servers.liveserver()
        config.driver.get("https://app.medisource.com/patients/admitted")
        servers.searchpatientrecord(searchpatient)
        time.sleep(2)
        
    time.sleep(5)
    task = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a')
    time.sleep(5)
    taskstatus = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[3]/div/span').text
    print(taskstatus)
    
    if taskstatus == "In Progress":
        task.click()
        time.sleep(3)
        editbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[4]/div[2]/button').click() #edit button
        time.sleep(3)
            
    elif taskstatus == "Scheduled":
        task.click()
        time.sleep(3)
    
    # -- Declare Values 
    
    woundtype = "Pressure Ulcer"
    woundlocation = "Buttock (R)"
    

    function_woundprocess.addwoundoasis(
        woundtype,
        woundlocation
        )
    
    function_woundprocess.dragpin()
    
    # Declare as variable the data xlsx file - put it on the same folder as the project
    datafile = os.getcwd()+"\data.xlsx" 
    
    wound_df = pd.read_excel(datafile, 'wound_assessment')
    
    # Randomize location
    col_location = wound_df['LOCATION'].tolist()
    location = random.choice(col_location)
    
    # Randomize stages
    col_stages = wound_df['STAGES'].tolist()
    stages = random.choice(col_stages) # convert to int
    stages = str(stages) #convert to string 
    
    
    # Randomize grantissue
    col_grantissue = wound_df['GRANTISSUE'].tolist()
    grantissue = int(random.choice(col_grantissue))
    grantissue = str(grantissue)
    
    # Randomize nectissue
    col_nectissue = wound_df['NECTISSUE'].tolist()
    nectissue = int(random.choice(col_nectissue))
    nectissue = str(nectissue)
    
    # Randomize granneccoverage
    col_granneccoverage = wound_df['GRANNECCOVERAGE'].tolist()
    granneccoverage = int(random.choice(col_granneccoverage))
    granneccoverage = str(granneccoverage)
    
    # Randomize granneccoverage
    col_exuamount = wound_df['EXUAMOUNT'].tolist()
    exuamount = int(random.choice(col_exuamount))
    exuamount = str(exuamount)
    
    # Randomize exutype
    col_exutype = wound_df['EXUTYPE'].tolist()
    exutype = random.choice(col_exutype)
    
    # Randomize edges
    col_edges = wound_df['EDGES'].tolist()
    edges = int(random.choice(col_edges))
    edges = str(edges)
    
    # Randomize periwoundtissue
    col_periwoundtissue = wound_df['PERIWOUNDTISSUE'].tolist()
    periwoundtissue = random.choice(col_periwoundtissue)
    
    # Randomize healingstatus
    col_healingstatus = wound_df['HEALINGSTATUS'].tolist()
    healingstatus = random.choice(col_healingstatus)
    
    # Randomize woundrelatedpain
    col_woundrelatedpain = wound_df['WOUNDRELATEDPAIN'].tolist()
    woundrelatedpain = int(random.choice(col_woundrelatedpain))
    woundrelatedpain = str(woundrelatedpain)

    function_woundprocess.completewoundassessment(
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
        )
    
    
    function_woundprocess.digitalmeasurement()
    
    function_woundprocess.woundanalytics()



from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_human_resources, function_medical_resources
import random, os, pyautogui, sys, ctypes
import time
import pymsgbox
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo, complete_woundprocess
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import random

def userprocess(test_server):
 
    if test_server == "qa":
        servers.qaserver()
        config.driver.get("https://qado.medisource.com/personnels/create")
        time.sleep(2)
        
    elif test_server == "live":
        servers.liveserver()
        config.driver.get("https://app.medisource.com/personnels/create")
        time.sleep(2)
        
    
    # Select discipline and title
    sn = 'Skilled Nurse (SN)'
    sn_rn = 'Registered Nurse (RN)'
    sn_lvn = 'Licensed Vocational Nurse (LVN) / Licensed Practical Nurse (LPN) '
    hha = 'Home Health Aide (HHA)'
    hha_chha = 'Certified Home Health Aide (CHHA)'
    pt = 'Physical Therapist (PT)'
    pt_pt = 'Physical Therapist (PT)'
    pt_pta = 'Physical Therapist Assistant(PTA)'
    ot = 'Occupational Therapist (OT)'
    ot_ot = 'Occupational Therapist (OT)'
    ot_ota = 'Occupational Therapist Assistant (OTA)'
    st = 'Speech Therapist (ST)'
    st_st = 'Speech Therapist Assistant (ST)'
    st_sta = 'Speech-language pathologist (SLP)'
    msw = 'Medical Social Work (MSW)'
    msw_msw = 'Medical Social Worker (MSW)'
    msw_lcsw = 'Licensed Clinical Social Worker (LCSW)'
    
    # Choose final option
    discipline = sn
    title = sn_rn
    
    #randomize options
    language1 = ['English', 'Chinese', 'Filipino', 'French', 'German', 'Hebrew', 'Hungarian', 'Italian', 'Japanese', 'Korean', 'Malaysian', 'Russian', 'Spanish', 'Vietnamese', 'Unknown']
    language = random.choice(language1) 
    level1 = ['Fluent', 'Intermediate', 'Elementary', 'Unable to talk']
    level = random.choice(level1) 
    
    userole = 'Administrator'
    
    # Tabs
    personalinfo = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[1]/a')
    profcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[2]/a')
    healthcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[3]/a')
    
    # Personal Information
    function_human_resources.personalinfo(
        'Automated',
        '02/07/1997',
        'Asian',
        'Single',
        discipline,
        title,
        'Direct Hire',
        'Administrator',
        'Medisource, LLC.',
        '8982 Portage Pointe Dr #B, Streetsboro, OH, 44241',
        language,
        level
        )   
    
    function_human_resources.professionalcreds() # Profressional Credentials
    
    function_human_resources.healthcreds() # Health Credentials
    
    function_human_resources.verificationprocess(userole, test_server) # System Account

def medres_hospitals(test_server):
    
    if test_server == "qa":
        servers.qaserver()
        config.driver.get("https://qado.medisource.com/hospital")
        time.sleep(2)
        
    elif test_server == "live":
        servers.liveserver()
        config.driver.get("https://app.medisource.com/hospital")
        time.sleep(2)
    
    num = pymsgbox.prompt('How many records you want to add?', 'Healthcare Automation')
    num = int(num) 
    # Specify the numbers of hospital to be added
    for x in range(num):
        function_medical_resources.addhospital()
        
    time.sleep(3)

def medres_physicians(test_server, addtype):
    
    if test_server == "qa":
        servers.qaserver()
        config.driver.get("https://qado.medisource.com/physicians")
        time.sleep(2)
        
    elif test_server == "live":
        servers.liveserver()
        config.driver.get("https://app.medisource.com/physicians")
        time.sleep(2)
    
    if addtype == "1":
        function_medical_resources.addphysician_manual()
        
    elif addtype == "2":
        function_medical_resources.addphysician_npi()
        
    time.sleep(3)









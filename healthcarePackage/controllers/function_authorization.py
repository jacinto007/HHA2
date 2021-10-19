from controllers import config, patient_dashboard
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from _ast import Div
from datetime import date
from datetime import datetime, timedelta



def new_auth(
        patientname,
        days_range,
        rn,
        lvn,
        pt, 
        st,
        ot,
        msw,
        hha
        ):
    
    time.sleep(2)
    patientdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/ng-form/fieldset/table/tbody/tr[1]/td[2]//a').click()
    patienttb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/ng-form/fieldset/table/tbody/tr[1]/td[2]/div/div//input').send_keys(patientname, Keys.ENTER)
    
    time.sleep(2)
    startdate = config.driver.find_element_by_xpath('//*[@id="periodstart"]').get_attribute("value") #1. Get the current date of the OASIS and add days for the task date
    print(startdate)
    taskdateconvert = datetime.strptime(startdate, '%m/%d/%Y') #2. Convert to date string
    addeddaystodate = timedelta(days=days_range) #3. Add days to the date
    datetotal = taskdateconvert + addeddaystodate #4. add total
    finaltaskdate = datetime.strftime(datetotal, '%m/%d/%Y') #5. convert again to date string for final date
    
    time.sleep(2)
    #authnum = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/ng-form/fieldset/table/tbody/tr[2]/td[2]/div/input').send_keys()
    enddate = config.driver.find_element_by_xpath('//*[@id="periodend"]').send_keys(finaltaskdate)
    
    time.sleep(2)
    authstatusdd = config.driver.find_element_by_xpath('//*[@id="status_chosen"]/a').click()
    authstatustb = config.driver.find_element_by_xpath('//*[@id="status_chosen"]/div/div/input').send_keys('Approved', Keys.ENTER)
    
    time.sleep(2)
    authremark = config.driver.find_element_by_xpath('//*[@id="content"]//textarea').send_keys('This is created using automated testing.')
    
    time.sleep(2)
    snva = config.driver.find_element_by_name('snva').send_keys(rn)
    lvna = config.driver.find_element_by_name('lvnva').send_keys(lvn)
    ptva = config.driver.find_element_by_name('ptva').send_keys(pt)    
    stva = config.driver.find_element_by_name('stva').send_keys(st)
    otva = config.driver.find_element_by_name('otva').send_keys(ot)
    mswva = config.driver.find_element_by_name('mswva').send_keys(msw)
    hhava = config.driver.find_element_by_name('hhava').send_keys(hha)
    
    time.sleep(3)
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div[1]/button[2]').click()
    
    time.sleep(2)
    schednow = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()
    
    time.sleep(5)  
    cancel = config.driver.find_element_by_css_selector('body > div.modal.fade.ng-isolate-scope.draggable__modal-window.in > div > div > div > div:nth-child(3) > div > button.btn.mhc__btn-neutral.waves-effect.m-r-5').click()   
    
  
    
  
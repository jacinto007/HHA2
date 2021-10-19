from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException
import pymsgbox
from datetime import date
import random

# Useful variables from config.py
todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")



def addhospital():
    
    ssn = config.randomize_ssn()
    name_random = config.randomize_name()
    rn = random.randint(0, 999) #Random number 
    randomhospitalname = "Automated Hospital " + str(rn)

    newhospitalbtn =  config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/a').click()

    time.sleep(2)
    
    addtype = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/button').click()
    
    time.sleep(3)
    typetitle = config.driver.find_element_by_xpath('//*[@id="title"]').send_keys( "Hospital Type " + str(rn))
    time.sleep(3)
    savetypebtn = config.driver.find_element_by_css_selector('body > div.modal.fade.ng-isolate-scope.in > div > div > div > form > div > div:nth-child(3) > div > button.btn.mhc__btn-affirmative.waves-effect').click()
    
    time.sleep(3)
    
    hospitalname = config.driver.find_element_by_name('name').send_keys(randomhospitalname)
    address = config.driver.find_element_by_name('address').send_keys('441 W 6th St, Wyoming, PA, 18644')
    city = config.driver.find_element_by_name('city').send_keys('Wyoming')
    time.sleep(3)
    statedd = config.driver.find_element_by_xpath('//*[@id="state_chosen"]/a').click()
    time.sleep(3)
    statetb = config.driver.find_element_by_xpath('//*[@id="state_chosen"]/div/div/input').send_keys('pennsylvania', Keys.ENTER)
    time.sleep(3)
    zip = config.driver.find_element_by_name('zipCode').send_keys('18644')
    time.sleep(2)
    phone = config.driver.find_element_by_name('addPhone').send_keys(ssn)
    time.sleep(2)
    fax = config.driver.find_element_by_name('fax').send_keys(ssn)
    contactPerson = config.driver.find_element_by_name('contactPerson').send_keys(name_random)
    
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[2]').click()
    
    time.sleep(3)
    goback = config.driver.find_element_by_xpath('//*[@id="content"]/data/ul/li/button').click()
    
    time.sleep(3)
    
def addphysician_manual():
       time.sleep(3)
       today = date.today()
       todaynow = today.strftime("%m/%d/%Y")   
       taskdateconvert = datetime.strptime(todaynow, '%m/%d/%Y') #2. Convert to date string
       addeddaystodate = timedelta(days=2000) #3. Add days to the date
       datetotal = taskdateconvert + addeddaystodate #4. add total
       finaldate = datetime.strftime(datetotal, '%m/%d/%Y') #5. convert again to date string for final date  
       print(finaldate)

       ssn = config.randomize_ssn()
       name_random = config.randomize_name()
       randomspec = config.randomphysician_specialty()
       
       newphysicianbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/a').click()
       time.sleep(2)
       
       skipbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/div/div[1]/button[1]').click()
       
       fn = config.driver.find_element_by_name('firstName').send_keys(name_random)
       Ln = config.driver.find_element_by_name('lastName').send_keys('Automated')
       
       address = config.driver.find_element_by_name('address').send_keys('441 W 6th St, Wyoming, PA, 18644')
       city = config.driver.find_element_by_name('city').send_keys('Wyoming')
       time.sleep(3)
       statedd = config.driver.find_element_by_xpath('//*[@id="state_chosen"]/a').click()
       time.sleep(3)
       statetb = config.driver.find_element_by_xpath('//*[@id="state_chosen"]/div/div/input').send_keys('pennsylvania', Keys.ENTER)
       time.sleep(3)
       zip = config.driver.find_element_by_name('zipCode').send_keys('18644')
       time.sleep(2)
       phone = config.driver.find_element_by_name('addPhone').send_keys(ssn)
       time.sleep(2)
       fax = config.driver.find_element_by_name('fax').send_keys(ssn)
       contactPerson = config.driver.find_element_by_name('contactPerson').send_keys(str(name_random) + ' Automated')
       
       
       physpecialty = config.driver.find_element_by_name('physpecialty').send_keys(randomspec)
       licensed = config.driver.find_element_by_name('licensed').send_keys(ssn)
       expiration = config.driver.find_element_by_xpath('//*[@id="expiration"]').send_keys(finaldate)
       addEmail = config.driver.find_element_by_name('addEmail').send_keys(str(name_random).lower() + '@mailinator.com')
       
       accessportal_yes = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[18]/td[2]/div/label/input').click()
       
       time.sleep(3)
       
       savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[2]').click()
       
       time.sleep(3)
       
       backbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/ul/li/button').click()
       
    
def addphysician_npi():
    time.sleep(2)
    
    newphysicianbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/a').click()
    time.sleep(2)
       
    npirandom = config.randomphysician_npi()
    npi = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/input').send_keys(npirandom)
    time.sleep(5)
    continuebtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/div/div[1]/button[2]').click()
    time.sleep(3)
      
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[2]').click()
       
    time.sleep(3)
    
    backbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/ul/li/button').click()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

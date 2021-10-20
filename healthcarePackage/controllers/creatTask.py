from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
import os
import time
from controllers import config, patient_dashboard
from datetime import datetime
from datetime import timedelta
from datetime import date
  

 

def lvnSV():
    # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=1)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button').click() #clicking the plus icon
    time.sleep(5)
    #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("LVN/LPN - Skilled Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5) 
    
def lvnWV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=2)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("LVN/LPN - Wound Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def prnSV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=3)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("PRN - Skilled Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnEV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=4)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Education Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnIV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=5)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - IV Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnJSHHA():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=6)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Joint Supervisory (CHHA)")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)
    
def rnJSLVN():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=7)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Joint Supervisory (LVN)")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnSV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=9)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Skilled Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnSupV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=10)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Supervisory Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def rnWV():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=11)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Wound Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def ptIE():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=12)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("PT - Initial Eval")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def stIE():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=13)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("ST - Initial Eval")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def otIE():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=14)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("OT - Initial Eval")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)


def mswa():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=15)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("MSW - Assessment")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)

def mswfv():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=16)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("MSW - Follow-up Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(5)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5)


def chha():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=17)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("CHHA - HHA Visit")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(10)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(5) 
    
def transfer():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=20)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - OASIS D1 Transfer (not discharged)")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(10)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    #uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    #visit date
    visitdate = config.driver.find_element_by_xpath('//*[@id="visitdate"]')
    visitdate.send_keys(plustaskdate)
    #Create button
    time.sleep(7)
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(15) 
    #modal for succeeding task
    #proceedbtn = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()
    time.sleep(15) 
    #after mapunta sa trasnfer Order click pabalik nbg task list
    patient_dashboard.gettab("task")
    
def roc():
      
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=21)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - OASIS D1 Resumption of Care")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(10)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5) 
    visitdate = config.driver.find_element_by_xpath('//*[@id="visitdate"]')
    visitdate.send_keys(plustaskdate) 
    #uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(15) 
    patient_dashboard.gettab("task")
    time.sleep(15) 
#Skilled Assessment    
def rnsa():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=55)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() #clicking the plus icon
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - Skilled Assessment")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(10)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)  
    uncheck_mdo = config.driver.find_element_by_xpath('/html/body//label[contains(string(), "Create an MD Order for this task?")]').click()
    #Create button
    time.sleep(7)
    createbtn = config.driver.find_element_by_xpath('/html/body//button[contains(string(), "Create")]').click()
    time.sleep(15) 
    #modal for succeeding task
    #proceedbtn = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()
    
def rec():
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,1000)")
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=55)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    #click yung task details icon
    tdicon = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[21]/td[8]/div/button[1]/i').click()
    #click yung task dropdown at piliin recert
    time.sleep(8)
    tddown = config.driver.find_element_by_xpath('/html/body/div[10]/div/div/div/form/div/div/div[2]/div/fieldset/div/div[1]/div[2]/table/tbody/tr/td/div[2]/div/div/div').click()
    time.sleep(8)
    newTask1A = config.driver.find_element_by_xpath('/html/body/div[10]/div/div/div/form/div/div/div[2]/div/fieldset/div/div[1]/div[2]/table/tbody/tr/td/div[2]/div/div/div/div/ul/li[2]').click()
    #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="visitdate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body/div[10]/div/div/div/form/div/div/div[3]/div/button[2]').click()
    time.sleep(15) 
    patient_dashboard.gettab("task")
    time.sleep(15) 
    
def dc():
     # kunin ang date ngayun
    dateNow = date.today()
    # magdagdag ng araw
    addDate = dateNow + timedelta(days=115)
    #convert natin yung date into string on MM/DD/YYY fromat
    plustaskdate = datetime.strftime(addDate, '%m/%d/%Y')
    #clicking the plus icon
    new1 = config.driver.find_element_by_xpath('//*[@id="save"]/li/button/i[2]').click() 
    time.sleep(5)
     #task date
    taskdate = config.driver.find_element_by_xpath('//*[@id="selecteddate"]')
    taskdate.send_keys(plustaskdate)
    time.sleep(5)
    taskDropdown = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/a').click() 
    time.sleep(5)
    newTask1 = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/div/input').send_keys("RN - OASIS D1 Discharge from Agency")
    newTask1A = config.driver.find_element_by_xpath('//*[@id="tooltip_err7"]/div/div/div/div/ul/li[2]').click()
    time.sleep(10)
    staffdd = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/a').click() 
    time.sleep(5)
    staff = config.driver.find_element_by_xpath('//*[@id="tooltip_err2"]/div/div/div/div/ul/li[2]')
    time.sleep(5)
    staff.click()    
    time.sleep(5)
    #visit date
    visitdate = config.driver.find_element_by_xpath('//*[@id="visitdate"]')
    visitdate.send_keys(plustaskdate) 
    time.sleep(5) 
    #Create button
    createbtn = config.driver.find_element_by_xpath('/html/body/div[10]/div/div/div/div/div[2]/div[2]/div/button[2]').click()
    time.sleep(15) 
    patient_dashboard.gettab("task")
    time.sleep(15)  
    
    

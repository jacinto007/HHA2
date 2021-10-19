from controllers import config, login, servers
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def gettab(pdtab):
    
    tab = ""
    
    if pdtab == "chart":
        tab = config.driver.find_element_by_xpath('//*[@id="togglesidelist"]')
           
    elif pdtab == "task":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[2]/a')
        
    elif pdtab == "mdo":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[3]/a')
    
    elif pdtab == "communication":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[4]/a')
           
    elif pdtab == "spx":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[5]/a')
        
    elif pdtab == "adverse":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[6]/a')

    elif pdtab == "medication":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[7]/a')
        
    elif pdtab == "misc":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[8]/a')
        
    elif pdtab == "woundmanagement":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[8]/a')
         
    elif pdtab == "vsmonitor":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[9]/a')
        
    elif pdtab == "qasis":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[10]/a')   
                 
    elif pdtab == "ptgmanager":
        tab = config.driver.find_element_by_xpath('//*[@id="profile-main-header"]/div/ul/li[11]/a')
        
    tab.click()

def create_mdo(mdotask):
    
    newbtn = config.driver.find_element_by_xpath('//*[@id="data-table-command-header"]/div[3]/button').click()
    listmdo = config.driver.find_element_by_xpath('//*[@id="data-table-command-header"]/div[3]/ul').text
    newmdo = ""
    
    if mdotask == "Physician Order":
        newmdo = config.driver.find_element_by_xpath('//*[@id="data-table-command-header"]/div[3]/ul/li[6]/a')
         
    elif mdotask == "Recertification Order": 
        newmdo = config.driver.find_element_by_xpath('//*[@id="data-table-command-header"]/div[3]/ul/li[2]/a')
       
    elif mdotask == "Discharge Order": 
        newmdo = config.driver.find_element_by_xpath('//*[@id="data-table-command-header"]/div[3]/ul/li[3]/a')
          
    elif mdotask == "Discharge (Death at Home)": 
        newmdo = config.driver.find_element_by_xpath('//*[@id="data-table-command-header"]/div[3]/ul/li[4]/a')
         
    elif mdotask == "Transfer Order": 
        newmdo = config.driver.find_element_by_xpath('//*[@id="data-table-command-header"]/div[3]/ul/li[5]/a')
     
    time.sleep(5)   
    newmdo.click()
    
def newNotes(noteType):
    time.sleep(5)
    new1 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[2]/button')
    new1.click()
    time.sleep(5)
    
    if noteType == "Communication Notes":
        newnote = config.driver.find_element_by_xpath('/html/body/section/section/data/section/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul[1]/li[1]')
         
    elif noteType == "HHA Care Plan": 
        newnote = config.driver.find_element_by_xpath('/html/body/section/section/data/section/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul[1]/li[2]')
       
    elif noteType == "Transfer Summary": 
        newnote = config.driver.find_element_by_xpath('/html/body/section/section/data/section/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul[2]/li[2]')
          
    elif noteType == "Discharge Summary": 
        newnote = config.driver.find_element_by_xpath('/html/body/section/section/data/section/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul[2]/li[3]')
         
    elif noteType == "Discharge Instruction": 
        newnote = config.driver.find_element_by_xpath('/html/body/section/section/data/section/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul[2]/li[4]')
     
    elif noteType == "Case Conference": 
        newnote = config.driver.find_element_by_xpath('/html/body/section/section/data/section/div[2]/div/div/div/div/div/div[1]/div/div[2]/div/ul[2]/li[5]')   
        
     
    time.sleep(5)   
    newnote.click()

        
       

      
      
      
      
      
      
      
      
      
      
      
      
        
        
from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_create_task, function_complete_task
import random, time
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import admission, oasis, create_task, complete_task, create_mdo

def create_task(task, rnskilledass):
    t = task
    s = rnskilledass
    time.sleep(3)
    
    #Scrolldown
    scrolldown = config.driver.execute_script("window.scrollTo(0,0)")
           

    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(5)
    
    print(t)
    print(s)
    for x in t:
        for y in s:
            print(x, y)
        if ((x == "RN - OASIS D1 Discharge Non-visit" or x == "RN - OASIS D1 Other Follow-Up") or ((x == "RN - OASIS D1 Transfer (discharged)" or x == "RN - OASIS D1 Transfer (not discharged)") or (x == "RN - Discharge (Summary Only)" or x == "RN - OASIS D1 Resumption of Care"))):
            function_create_task.oasis(x)
            #complete_task.completetask(x) #enable this to auto-complete the task
        elif x == "RN - Skilled Assessment":
            function_create_task.skilledassessment(x, y)
            complete_task.completetask(x) #enable this to auto-complete the task
        else:
            function_create_task.snv(x)
            #complete_task.completetask(x) #enable this to auto-complete the task
        time.sleep(5)
            
    time.sleep(2)
    
    
  

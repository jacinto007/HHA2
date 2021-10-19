from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo
import ctypes  # An included library with Python install. 
import pymsgbox


rnskilledassesment = str("RN - Skilled Assessment")
rnskilledassesment_dc = str("RN - OASIS D1 Discharge from Agency")
rnskilledassesment_recert = str("RN - OASIS D1 Recertification")

oasisdcaegency = str("RN - OASIS D1 Discharge from Agency")
oasisdcnvisit = str("RN - OASIS D1 Discharge Non-visit")
oasisfollowup = str("RN - OASIS D1 Other Follow-Up")
oasistfrfdc = str("RN - OASIS D1 Transfer (discharged)")
oasistfrnotdc = str("RN - OASIS D1 Transfer (not discharged)")
oasisdcsummary = str("RN - Discharge (Summary Only)")
oasisroc = str("RN - OASIS D1 Resumption of Care")

lvnskilledvisit = str("LVN/LPN - Skilled Visit")
lvnwoundvisit = str("LVN/LPN - Wound Visit")
prnskilledvisit = str("PRN - Skilled Visit")
rneducvisit = str("RN - Education Visit")
rnivvisit = str("RN - IV Visit")
rnjschha = str("RN - Joint Supervisory (CHHA)")
rnjslvn = str("RN - Joint Supervisory (LVN)")
rnskilledvisit = str("RN - Skilled Visit")
rnsupvisit = str("RN - Supervisory Visit")
rnwoundvisit = str("RN - Wound Visit")

ptieval = str("PT - Initial Eval")
ptievalsoc = str("PT - Initial Eval-SOC")
ptvisit = str("PT - PT Visit")
ptavisit = str("PTA - PTA Visit")

otieval = str("OT - Initial Eval")
otievalsoc = str("OT - Initial Eval-SOC")
otvisit = str("OT - OT Visit")
otavisit = str("OTA - OTA Visit")

stieval = str("ST - Initial Eval")
stievalsoc = str("ST - Initial Eval-SOC")
stvisit = str("ST - ST Visit")

mswass = str("MSW - Assessment")
mswfollowup = str("MSW - Follow-up Visit")
chhavisit = str("CHHA - HHA Visit")


def test_unit(testserver, searchpatient):
    
    tasks = [rnivvisit, rnsupvisit, oasistfrnotdc, oasisroc, rnskilledassesment, rnsupvisit, rnskilledassesment, rnskilledassesment] #Enter the task variable you want to create Note: skilledassessment should always the last on the array
    rnskilledass = [rnskilledassesment_recert, rnskilledassesment_dc, rnskilledassesment_recert] # Enter if its recertification or discharge
    
    if testserver == "qa":
        servers.qaserver()
        # Created Patient
        config.driver.get("https://qado.medisource.com/patients/admitted")
        servers.searchpatientrecord(searchpatient)
        time.sleep(2)   
        
    elif testserver == "live":
        servers.liveserver()
        # Created Patient
        config.driver.get("https://app.medisource.com/patients/admitted")
        servers.searchpatientrecord(searchpatient)
        time.sleep(2)   
        
    else:
        pymsgbox.alert('Unable to run test, wrong input.. Please re-run the test.', 'Warning')
         # END TEST
        config.driver.close()
    


    create_task.create_task(tasks, rnskilledass)
    function_mdo.testinfo()
   
    
    
    #currentpage = config.driver.current_url
    
    
    
    
    
    # END TEST
 
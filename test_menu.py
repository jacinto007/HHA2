from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
import create_task, test_unit, test_main
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo
import ctypes  # An included library with Python install. 
import pymsgbox

chooseserver = pymsgbox.prompt('Choose server for the Automated Test, type: \n \n 1. Live (geekers) \n 2. QA (unitest)', 'Healthcare Automation')
testcase = pymsgbox.prompt('Choose Test Case, type: \n \n 1. Basic Testing \n > Patient Admission \n > Complete OASIS Partly \n > Create 2 RN Tasks (IV Visit and Supervisory Visit) \n > Transfer \n > ROC \n > Recert \n > DC \n \n 2. Add New Episode \n \n 3. Pre-admit a MEDICARE patient  \n \n 4. Pre-admit a NON-MEDICARE patient \n \n 5. Woundcare Process \n \n 6. Completing Authorization \n \n 7. Admit a Patient and Add Communication Notes \n \n 8. Other Management Process', 'Healthcare Automation')

####JACCKKK TEST
if chooseserver == "1":
    testserver = "live"

    if testcase == "1": # Option for Basic Testing
        test_main.test_main(testserver)
        
    elif testcase == "2": # Option for exisiting patient
        searchpatient = pymsgbox.prompt('Type EXACT Patient Name: ', 'Healthcare Automation')
        test_unit.test_unit(testserver, searchpatient)
    
    elif testcase == "3": # Option for Pre-admitting a patient medicare
        test_main.preadmitpatient_medicare(testserver)
        
    elif testcase == "4": # Option for Pre-admitting a patient non-medicare
        test_main.preadmitpatient_nonmedicare(testserver)
        
    elif testcase == "5": # Option for Adding wound to OASIS and assess
        searchpatient = pymsgbox.prompt('Type EXACT Patient Name: Please make sure that the OASIS has no wound yet.', 'Healthcare Automation')
        test_main.wound(testserver, searchpatient)
    
    elif testcase == "6": # Option for Adding wound to OASIS and assess
        dayrange = pymsgbox.prompt('Choose Number of Days: ', 'Healthcare Automation')
        test_main.authorization(testserver, dayrange)
    
    elif testcase == "7": # Option for Pre-admitting a patient and complete communication note
        test_main.communiMain(testserver)
        
    elif testcase == "8": # other options for outside patient workflow
        otherman = pymsgbox.prompt('Choose Process: \n \n 1. User Management \n \n 2. Emergency Services  \n \n 3. Hospitals \n \n 4. Physicians \n \n 5. Referral Sources \n \n 6. Insurance Companies  \n \n 7. Healthcare Vendors', 'Healthcare Automation')
        if otherman == "1":
            test_main.usermanagement(testserver)
            
        elif otherman == "2":
            test_main.emergencyservices(testserver)    
            
        elif otherman == "3":
            test_main.hospital(testserver)  
                
        elif otherman == "4":
            addtype = pymsgbox.prompt('1. Manual Add \n \n \n 2. Using NPI', 'Healthcare Automation')
            test_main.physicians(testserver, addtype) 
                 
        elif otherman == "5":
            test_main.referralsources(testserver)      
                    
        elif otherman == "6":
            test_main.insurancecompanies(testserver)    
              
        elif otherman == "7":
            test_main.healthcarevendors(testserver) 
              
            
elif chooseserver == "2":
    
    testserver = "qa"
    
    if testcase == "1": # Option for Basic Testing
        test_main.test_main(testserver)
        
    elif testcase == "2": # Option for exisiting patient
        #taskcode = pymsgbox.prompt('Task Codes: \n \n rnskilledassesment = "RN - Skilled Assessment"  \n rnskilledassesment_dc = "RN - OASIS D1 Discharge from Agency"  \n rnskilledassesment_recert = "RN - OASIS D1 Recertification"   \n  \n  oasisdcaegency = "RN - OASIS D1 Discharge from Agency"   \n oasisdcnvisit = "RN - OASIS D1 Discharge Non-visit"   \n oasisfollowup = "RN - OASIS D1 Other Follow-Up"   \n oasistfrfdc = "RN - OASIS D1 Transfer (discharged)"   \n oasistfrnotdc = "RN - OASIS D1 Transfer (not discharged)"   \n oasisdcsummary = "RN - Discharge (Summary Only)"   \n oasisroc = "RN - OASIS D1 Resumption of Care"   \n \n lvnskilledvisit = "LVN/LPN - Skilled Visit"   \n lvnwoundvisit = "LVN/LPN - Wound Visit"   \n prnskilledvisit = "PRN - Skilled Visit"   \n rneducvisit = "RN - Education Visit"  \n rnivvisit = "RN - IV Visit" \n rnjschha = "RN - Joint Supervisory (CHHA)"   \n rnjslvn = "RN - Joint Supervisory (LVN)"   \n rnskilledvisit = "RN - Skilled Visit"   \n rnsupvisit = "RN - Supervisory Visit"   \n rnwoundvisit = "RN - Wound Visit"   \n  \n ptieval = "PT - Initial Eval"   \n ptievalsoc = "PT - Initial Eval-SOC"  \n ptvisit = "PT - PT Visit"  \n ptavisit = "PTA - PTA Visit"  \n otieval = "OT - Initial Eval"  \n otievalsoc = "OT - Initial Eval-SOC"  \n otvisit = "OT - OT Visit"  \n otavisit = "OTA - OTA Visit"  \n \n stieval = "ST - Initial Eval"  \n stievalsoc = "ST - Initial Eval-SOC"  \n stvisit = "ST - ST Visit" \n \n mswass = "MSW - Assessment"  \n mswfollowup = "MSW - Follow-up Visit"  \n chhavisit = "CHHA - HHA Visit" \n \n Type-in Tasks Code to create, seperated by commas. \n ', 'Select Tasks')
        searchpatient = pymsgbox.prompt('Type EXACT Patient Name: ', 'Healthcare Automation')
        test_unit.test_unit(testserver, searchpatient)
     
    elif testcase == "3":  # Option for Pre-admitting a patient medicare
        test_main.preadmitpatient_medicare(testserver) 
    
    elif testcase == "4": # Option for Pre-admitting a patient non-medicare
        test_main.preadmitpatient_nonmedicare(testserver)
        
    elif testcase == "5": # Option for Adding wound to OASIS and assess
        searchpatient = pymsgbox.prompt('Type EXACT Patient Name: Please make sure that the OASIS has no wound yet.', 'Healthcare Automation')
        test_main.wound(testserver, searchpatient)
        
    elif testcase == "6": # Option for adding authorization to pre-admitted patient
        dayrange = pymsgbox.prompt('Choose Number of Days: ', 'Healthcare Automation')
        test_main.authorization(testserver, dayrange)
    
    elif testcase == "7": # Option for Pre-admitting a patient and complete communication note
        test_main.communiMain(testserver)
        
    elif testcase == "8": # other options for outside patient workflow
        otherman = pymsgbox.prompt('Choose Process: \n \n 1. User Management \n \n 2. Emergency Services  \n \n 3. Hospitals \n \n 4. Physicians \n \n 5. Referral Sources \n \n 6. Insurance Companies  \n \n 7. Healthcare Vendors', 'Healthcare Automation')
        
        if otherman == "1":
            test_main.usermanagement(testserver)
            
        elif otherman == "2":
            test_main.emergencyservices(testserver)    
            
        elif otherman == "3":
            test_main.hospital(testserver)  
                
        elif otherman == "4":
            addtype = pymsgbox.prompt('1. Manual Add \n \n 2. Using NPI', 'Healthcare Automation')
            test_main.physicians(testserver, addtype) 
            
        elif otherman == "5":
            test_main.referralsources(testserver)      
                    
        elif otherman == "6":
            test_main.insurancecompanies(testserver)    
              
        elif otherman == "7":
            test_main.healthcarevendors(testserver)  
        
        
else:
        pymsgbox.alert('Unable to run test, wrong input. Please re-run the test.', 'Warning')
         # END TEST
        config.driver.close()
    









# END TEST
 
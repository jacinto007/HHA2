from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard, function_create_task, function_complete_task, function_mdo,  function_authorization
import random, time
from datetime import date
import admission, oasis, create_task, complete_task, create_mdo, complete_authorization, other_process, commMain, complete_woundprocess
import pymsgbox
import plottingTask



def test_main(servertest):
    
    test_server = servertest # Change the value to qa or live
           
    admission.admission_medicare(test_server) #PATIENT ADMISSION
    #oasis.oasispart() #COMPLETE OASIS SOC
    time.sleep(8)
    plottingTask.plot()  
    function_mdo.testinfo()
    config.driver.close()
    

def preadmitpatient_medicare(servertest):
    
    test_server = servertest 
    admission.preadmission_medicare(test_server) #PATIENT ADMISSION
    
    if servertest == "qa":
        config.driver.get("https://qado.medisource.com/patients/pre-admitted")
    elif servertest == "live": 
        config.driver.get("https://app.medisource.com/patients/pre-admitted")
    
    pymsgbox.alert('Test Success!', 'Success')
    print('Test success!')   
    config.driver.close()

def preadmitpatient_nonmedicare(servertest):
    
    test_server = servertest 
    admission.preadmission_nonmedicare(test_server) #PATIENT ADMISSION
    
    if servertest == "qa":
        config.driver.get("https://qado.medisource.com/patients/pre-admitted")
    elif servertest == "live": 
        config.driver.get("https://app.medisource.com/patients/pre-admitted")
        
    pymsgbox.alert('Test Success!', 'Success')
    print('Test success!')   
    config.driver.close()
 
def communiMain(servertest):
    
    test_server = servertest 
    
    
    if servertest == "qa":
        config.driver.get("https://qado.medisource.com/patients/pre-admitted")
    elif servertest == "live": 
        config.driver.get("https://app.medisource.com/patients/pre-admitted")
    
    admission.preadmission_medicare(test_server) #PATIENT ADMISSION
        
    commMain.communicationmain()

 
    
def wound(servertest, searchpatient):
    test_server = servertest 
    complete_woundprocess.complete_woundprocess(servertest, searchpatient)
    
    print('Test success!')   
    pymsgbox.alert('Test Success!', 'Success')
    config.driver.close()


def authorization(servertest, dayrange):
    test_server = servertest 
    complete_authorization.authorization(test_server, dayrange)
    
    print('Test success!')   
    pymsgbox.alert('Test Success!', 'Success')
    config.driver.close()    
    
def usermanagement(servertest):
    test_server = servertest 
    other_process.userprocess(test_server)
    
    print('Test success!')   
    pymsgbox.alert('Test Success!', 'Success')
    config.driver.close()        
    
    
def hospital(servertest):
    test_server = servertest 
    other_process.medres_hospitals(test_server)
    
    print('Test success!')   
    pymsgbox.alert('Test Success!', 'Success')
    config.driver.close()        

       
       
def physicians(servertest, addtype):
    test_server = servertest 
    add_type = addtype
    print('Physician')    
    other_process.medres_physicians(test_server, add_type)
    
    print('Test success!')   
    pymsgbox.alert('Test Success!', 'Success')
    config.driver.close()   
     
           
def referralsources(servertest):
    test_server = servertest 
    print('referral sources')    
     
            
def insurancecompanies(servertest):
    test_server = servertest 
    print('insurance companies')    
     
             
def healthcarevendors(servertest):
    test_server = servertest 
    print('healthcare vendors')    
     
                 
def emergencyservices(servertest):
    test_server = servertest 
    print('emergency services')    
     
  
    
   
  
  
  
  
  
  
  
  
    


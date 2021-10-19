from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard
import random, time
from datetime import date
from datetime import datetime, timedelta
from re import search

todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
 
ssn = random.randint(0, 9999999999)

# ------------------------------------------------------------------------------------------------
#  search Automated Patient and click the top/first result
# ------------------------------------------------------------------------------------------------
def searchpatient():
    time.sleep(5)
    search_patient = config.driver.find_element_by_xpath("//*[@id='searchbar__wrapper']/div/input")
    search_patient.send_keys("Automated")
    time.sleep(5)
    patientresult = config.driver.find_element_by_xpath("//*[@id='content']/data/div/div[2]/div/table/tbody/tr[2]").click()
    time.sleep(5)

def oasis():
    
    # ------------------------------------------------------------------------------------------------
    #  MAIN OASIS CODE
    # ------------------------------------------------------------------------------------------------
    
    #Open the OASIS 
    clickoasis = config.driver.find_element_by_xpath("//*[@id='parent']/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a").click()
    time.sleep(5)
    
    #click the OASIS edit button
    oasisedit = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div[4]/div[2]/button").click()
    
    # ------------------------------------------------------------------------------------------------
    # FUNCTIONS FOR COMPLETING OASIS PER TAB 
    # ------------------------------------------------------------------------------------------------
    
    time.sleep(5)
    
    # Declare the tabs, save button, and previous next button 
    savebtn = config.driver.find_element_by_css_selector("#titleNoteBar > div.col-sm-12.p-0.title__section.m-b-10.oasis_actionBtnTab > div:nth-child(2) > button.btn__success.m-l-10.waves-effect.ng-scope")
    #previousbtn = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/div/fieldset/div[2]/div/div[4]/button[1]')
    #nextbtn = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/div/fieldset/div[2]/div/div[4]/button[2]')
     
    #OASIS Buttons
    democrecord = config.driver.find_element_by_xpath('//*[@id="clinical"]')
    diagnosesmedhis = config.driver.find_element_by_xpath('//*[@id="diagnosis"]')
    vssensory = config.driver.find_element_by_xpath('//*[@id="sensory"]')
    integendo = config.driver.find_element_by_xpath('//*[@id="integumentary"]')
    cardio = config.driver.find_element_by_xpath('//*[@id="cardio"]')
    nutrielim = config.driver.find_element_by_xpath('//*[@id="elimination"]')
    neurobehav = config.driver.find_element_by_xpath('//*[@id="neuro"]')
    adlmusco = config.driver.find_element_by_xpath('//*[@id="adl"]')
    medication = config.driver.find_element_by_xpath('//*[@id="medication"]')
    careman = config.driver.find_element_by_xpath('//*[@id="careManagement"]')
    
    # ------------------------------------------------------------------------------------------------
    #  TIME IN AND TIME OUT
    # ------------------------------------------------------------------------------------------------
    function_oasis.oasissoc_timeinout(todaytime, plustime)
    
    # ------------------------------------------------------------------------------------------------
    #  DEMOGRAPHICS
    # ------------------------------------------------------------------------------------------------
    function_oasis.oasissoc_demographics(todaydate, "Early", ssn)
    
    # ------------------------------------------------------------------------------------------------
    #  DIAGNOSIS
    # ------------------------------------------------------------------------------------------------
    diagnosesmedhis.click()
    time.sleep(5)
    
    diagnosesmedhis.click()
    #This declares the value for m0s with multiple items
    m1028 = [3] #values 1,2,3
    m0133 = [1,2,3,4,5,6,7,8]
    function_oasis.oasissoc_diagnosesmedhis(
        "U07.1",
        "N39.0",
        "B96.5",
        "N13.9",
        "N13.39",
        "I48.91",
        m1028,
        m0133,
        "59",
        "153"
        )
    
    # ------------------------------------------------------------------------------------------------
    #  VITAL SIGNS / SENSORY
    # ------------------------------------------------------------------------------------------------
    vssensory.click()
    time.sleep(5)
    vssensory.click()
    function_oasis.oasissoc_vssensory(
        "97.4",
        "85",
        "28",
        "117",
        "70",
        "88",
        "92",
        "2",
        "128"
        )
    
    # ------------------------------------------------------------------------------------------------
    #  INTEGUMENTARY / ENDOCRINE
    # ------------------------------------------------------------------------------------------------
    integendo.click()
    time.sleep(5)
    integendo.click()
    function_oasis.oasissoc_integendo()
    
    # ------------------------------------------------------------------------------------------------
    #  CARDIOPULMONARY
    # ------------------------------------------------------------------------------------------------
    cardio.click()
    time.sleep(5)
    cardio.click()
    function_oasis.oasissoc_cardio()
    
    # ------------------------------------------------------------------------------------------------
    #  NUTRITION / ELIMINATION
    # ------------------------------------------------------------------------------------------------
    nutrielim.click()
    time.sleep(5)
    nutrielim.click()
    function_oasis.oasissoc_nutrielim()
    
    # ------------------------------------------------------------------------------------------------
    #  NEUROLOGIC / BEHAVIORAL
    # ------------------------------------------------------------------------------------------------
    neurobehav.click()
    time.sleep(5)
    neurobehav.click()
    function_oasis.oasissoc_neurobehav()
    
    # ------------------------------------------------------------------------------------------------
    #  ADL / IADL / MUSCULOSKELETAL
    # ------------------------------------------------------------------------------------------------
    adlmusco.click()
    time.sleep(5)
    adlmusco.click()
    function_oasis.oasissoc_adlmusco()
    
    # ------------------------------------------------------------------------------------------------
    #  MEDICATION
    # ------------------------------------------------------------------------------------------------
    medication.click()
    time.sleep(5)
    medication.click()
    function_oasis.oasissoc_medication()
    
    # ------------------------------------------------------------------------------------------------
    #  CARE MANAGEMENT
    # ------------------------------------------------------------------------------------------------
    careman.click()
    time.sleep(5)
    careman.click()
    function_oasis.oasissoc_careman()
    
    
    # ------------------------------------------------------------------------------------------------
    #  SAVE 
    # ------------------------------------------------------------------------------------------------
    time.sleep(5)
    savebtn.click()
    
    time.sleep(3)
    savebtn.click()
 
 
def oasispart():
    
    # ------------------------------------------------------------------------------------------------
    #  MAIN OASIS CODE
    # ------------------------------------------------------------------------------------------------
    
    #Open the OASIS 
    clickoasis = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[1]/div/div[5]/div[1]/table/tbody/tr[2]/td[2]/a').click()
    time.sleep(8)
    
    #click the OASIS edit button
    oasisedit = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div[4]/div[2]/button").click()
    
    # ------------------------------------------------------------------------------------------------
    # FUNCTIONS FOR COMPLETING OASIS PER TAB 
    # ------------------------------------------------------------------------------------------------
    
    time.sleep(5)
    
  
    # Declare the tabs, save button, and previous next button 
    #previousbtn = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/div/fieldset/div[2]/div/div[4]/button[1]')
    #nextbtn = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div/div/fieldset/div[2]/div/div[4]/button[2]')
    
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]//button[contains(string(), "Save")]')
   
    #OASIS Buttons
    democrecord = config.driver.find_element_by_xpath('//*[@id="clinical"]')
    diagnosesmedhis = config.driver.find_element_by_xpath('//*[@id="diagnosis"]')
    vssensory = config.driver.find_element_by_xpath('//*[@id="sensory"]')
    integendo = config.driver.find_element_by_xpath('//*[@id="integumentary"]')
    cardio = config.driver.find_element_by_xpath('//*[@id="cardio"]')
    nutrielim = config.driver.find_element_by_xpath('//*[@id="elimination"]')
    neurobehav = config.driver.find_element_by_xpath('//*[@id="neuro"]')
    adlmusco = config.driver.find_element_by_xpath('//*[@id="adl"]')
    medication = config.driver.find_element_by_xpath('//*[@id="medication"]')
    careman = config.driver.find_element_by_xpath('//*[@id="careManagement"]')
    
    # ------------------------------------------------------------------------------------------------
    #  TIME IN AND TIME OUT
    # ------------------------------------------------------------------------------------------------
    function_oasis.oasissoc_timeinout(todaytime, plustime)
    
    # ------------------------------------------------------------------------------------------------
    #  DEMOGRAPHICS
    # ------------------------------------------------------------------------------------------------
    function_oasis.oasissoc_demographics(todaydate, "Early", ssn)
    
    # ------------------------------------------------------------------------------------------------
    #  SAVE 
    # ------------------------------------------------------------------------------------------------
    time.sleep(5)
    savebtn.click()
    time.sleep(5)
    config.driver.refresh()
    
    #time.sleep(3)
    #savebtn.click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,0)")
    
    time.sleep(3)
    #go back to task
    patient_dashboard.gettab("task")
    time.sleep(3)
       
    
    
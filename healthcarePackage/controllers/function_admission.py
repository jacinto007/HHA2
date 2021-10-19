from controllers import config, login, servers
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

def admission(
        refdate,
        reftime,
        plannedsoc,
        lname,
        fname,
        mi,
        bdate,
        sex,
        mstatus,
        ethn,
        langspoken,
        ssnumber,
        streetaddress,
        adddirection,
        majorcstreet,
        city,
        stateadd,
        zipcodeadd,
        phoneone,
        phonetwo,
        emaila,
        cgname, 
        cgphone,
        ecname,
        ecrel,
        ecp1,
        ecp2,
        hadmit,
        hdc,
        dsur,
        dallergies,
        moeigthy
        ):
    
    time.sleep(5)
    
    skip_eligibility = config.driver.find_element_by_link_text("Skip").click() #skip button
    time.sleep(2)
# ------------------------------------------------------------------------------------------------
#  MAIN PATIENT ADMISSION CODE
# ------------------------------------------------------------------------------------------------

    #Patient Information
    referral_date = config.driver.find_element_by_id("refDate").send_keys(refdate)
    time.sleep(2)
    referral_time = config.driver.find_element_by_xpath('//*[@id="referral_time"]/input').send_keys(reftime)
    mrn = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/label/input").click()
    preadmission_date = config.driver.find_element_by_id("pre_admission_date").send_keys(plannedsoc)
    last_name = config.driver.find_element_by_id("last_name").send_keys(lname)
    first_name = config.driver.find_element_by_id("first_name").send_keys(fname)
    middle_initial = config.driver.find_element_by_id("mi").send_keys(mi)
    birthdate = config.driver.find_element_by_id("birthdate").send_keys(bdate)
    
    #conditional formatting
    gender = ""
    if sex == "Male":
        gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[1]/input")
    elif sex == "Female":
        gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[2]/input")
    time.sleep(1)
    gender.click()
    
    #code for choosing select
    option = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/a").click() #click the select
    mstext = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/div/div/input").send_keys(mstatus, Keys.ENTER) #search the value
    option = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").click()
    ethnicity = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").send_keys(ethn, Keys.ENTER)
    
    #Language Spoken
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").click()
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(langspoken)
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(Keys.ENTER)

    ssn = config.driver.find_element_by_id("ssNumber").send_keys(ssnumber)
    
    #Patient Address
    strtadd = config.driver.find_element_by_id("main_line1").send_keys(streetaddress)
    addd = config.driver.find_element_by_id("main_line2").send_keys(adddirection)
    mcs = config.driver.find_element_by_id("main_street").send_keys(majorcstreet)
    cityadd = config.driver.find_element_by_id("main_city").send_keys(city)
    
    #State Code
    config.driver.find_element(By.XPATH, "//tr[20]/td[2]/div/div/div/a").click()
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").click()
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").send_keys(stateadd, Keys.ENTER)

    zipcode = config.driver.find_element_by_id("main_zipcode").send_keys(zipcodeadd)
    phone1 = config.driver.find_element_by_name("phone").send_keys(phoneone)
    phone2 = config.driver.find_element_by_name("other_phone").send_keys(phonetwo)
    email = config.driver.find_element_by_name("main_email").send_keys(emaila)
    
    #same as patient address button
    sameaspatientaddress = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[25]/td[2]/button").click()

    #Living Situation
    livings = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[35]/td[2]/div/label[2]/input").click() #Lives Alone
    assistance = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[36]/td[2]/div/label[4]/input").click() #Occasional short-term
    ls_caregiver = config.driver.find_element_by_id("ls_caregiver").send_keys(cgname)
    ls_caregiver_phone = config.driver.find_element_by_id("ls_caregiver_phone").send_keys(cgphone)
    
    #Emergency Contact
    ec_name = config.driver.find_element_by_id("ec_name").send_keys(ecname)
    ec_relationship = config.driver.find_element_by_id("ec_relationship").send_keys(ecrel)
    ec_phone = config.driver.find_element_by_id("ec_phone").send_keys(ecp1)
    ec_other_phone = config.driver.find_element_by_id("ec_other_phone").send_keys(ecp2)
    
# ------------------------------------------------------------------------------------------------
#  beyond this part, the automation will automatically select the first entry of each dropdown
# ------------------------------------------------------------------------------------------------
    time.sleep(3)
    
    #Physician Information
    attending_physician = config.driver.find_element_by_css_selector("#physician_attending_chosen > .chosen-single").click()
    at_result = config.driver.find_element_by_css_selector(".active-result:nth-child(2)").click()
    
    time.sleep(3)
    scrolldown = config.driver.execute_script("window.scrollTo(0,1000)")
    
    time.sleep(2)
    #Primary Insurance Information
    primary_insurance = config.driver.find_element_by_css_selector("#primary_insurance_chosen > .chosen-single").click()
    time.sleep(2)
    pi_result = config.driver.find_element_by_css_selector("#primary_insurance_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    #Scrolldown
    scrolldown = config.driver.execute_script("window.scrollTo(0,6500)")
    
    #Admission type
    admission_type = config.driver.find_element_by_css_selector("#admissiontype_chosen > .chosen-single").click()
    at_result = config.driver.find_element_by_css_selector("#admissiontype_chosen .active-result:nth-child(1)").click()
    
    pointoforigin = config.driver.find_element_by_css_selector("#point_of_origin_chosen > .chosen-single").click()
    poo_result = config.driver.find_element_by_css_selector("#point_of_origin_chosen .active-result:nth-child(1)").click()
    
    time.sleep(2)
    referral_type = config.driver.find_element_by_css_selector("#referral_type_chosen > .chosen-single").click()
    time.sleep(2)
    rt_result = config.driver.find_element_by_css_selector("#referral_type_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    referral_source = config.driver.find_element_by_css_selector("#referral_source_id_chosen > .chosen-single").click()
    time.sleep(2)
    rs_result = config.driver.find_element_by_css_selector("#referral_source_id_chosen .active-result:nth-child(2)").click()
    
    #Hospitalization Information
    hospital = config.driver.find_element_by_css_selector("#hospital_id_chosen > .chosen-single").click()
    time.sleep(1)
    h_result = config.driver.find_element_by_css_selector("#hospital_id_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    h_admitdate = config.driver.find_element_by_id("admit_date").send_keys(hadmit)
    h_discharge = config.driver.find_element_by_id("discharge_date").send_keys(hdc)
    
    #Diagnosis / Pre-admission Orders
    dsurgery = config.driver.find_element_by_id("diagnosis_surgery").send_keys(dsur)
    option = config.driver.find_element_by_xpath("//*[@id='diagnosis_allergies']/div/div/input").click()
    dallergies = config.driver.find_element_by_xpath("//*[@id='diagnosis_allergies']/div/div/input").send_keys(dallergies, Keys.ENTER)

    #M0080
    mo = ""
    
    if moeigthy == "RN":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[1]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_rn_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_rn_chosen .active-result:nth-child(1)").click()
        
    elif moeigthy == "PT":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[2]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_pt_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_pt_chosen .active-result:nth-child(1)").click()
        
    elif moeigthy == "SLP":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[3]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_st_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_st_chosen .active-result").click()
        
    elif moeigthy == "OT":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[4]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_ot_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_ot_chosen .active-result:nth-child(1)").click()
    
    mo.click()
   
    #choose the first CM
    case_manager = config.driver.find_element_by_css_selector("#cs_cm_chosen > .chosen-single").click()
    cm_result = config.driver.find_element_by_css_selector("#cs_cm_chosen .active-result:nth-child(1)").click()
    
    # SAVE button
    save = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div/div/div/div/div[1]/button[2]").click()
       
    time.sleep(5)
    
   
    #config.driver.close()

    
def preadmission_med(
        refdate,
        reftime,
        lname,
        fname,
        mi,
        bdate,
        sex,
        mstatus,
        ethn,
        langspoken,
        ssnumber,
        streetaddress,
        adddirection,
        majorcstreet,
        city,
        stateadd,
        zipcodeadd,
        phoneone,
        phonetwo,
        emaila,
        cgname, 
        cgphone,
        ecname,
        ecrel,
        ecp1,
        ecp2,
        hadmit,
        hdc,
        dsur,
        dallergies,
        moeigthy
        ):
    
    time.sleep(5)
    
    skip_eligibility = config.driver.find_element_by_link_text("Skip").click() #skip button

# ------------------------------------------------------------------------------------------------
#  MAIN PATIENT ADMISSION CODE
# ------------------------------------------------------------------------------------------------
    time.sleep(5)
    #Patient Information
    referral_date = config.driver.find_element_by_id("refDate").send_keys(refdate)
    time.sleep(2)
    referral_time = config.driver.find_element_by_xpath('//*[@id="referral_time"]/input').send_keys(reftime)
    mrn = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/label/input").click()
    last_name = config.driver.find_element_by_id("last_name").send_keys(lname)
    first_name = config.driver.find_element_by_id("first_name").send_keys(fname)
    middle_initial = config.driver.find_element_by_id("mi").send_keys(mi)
    birthdate = config.driver.find_element_by_id("birthdate").send_keys(bdate)
    
    #conditional formatting
    gender = ""
    if sex == "Male":
        gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[1]/input")
    elif sex == "Female":
        gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[2]/input")
    time.sleep(1)
    gender.click()
    
    #code for choosing select
    option = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/a").click() #click the select
    mstext = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/div/div/input").send_keys(mstatus, Keys.ENTER) #search the value
    option = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").click()
    ethnicity = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").send_keys(ethn, Keys.ENTER)
    
    #Language Spoken
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").click()
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(langspoken)
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(Keys.ENTER)

    ssn = config.driver.find_element_by_id("ssNumber").send_keys(ssnumber)
    
    #Patient Address
    strtadd = config.driver.find_element_by_id("main_line1").send_keys(streetaddress)
    addd = config.driver.find_element_by_id("main_line2").send_keys(adddirection)
    mcs = config.driver.find_element_by_id("main_street").send_keys(majorcstreet)
    cityadd = config.driver.find_element_by_id("main_city").send_keys(city)
    
    #State Code
    config.driver.find_element(By.XPATH, "//tr[20]/td[2]/div/div/div/a").click()
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").click()
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").send_keys(stateadd, Keys.ENTER)

    zipcode = config.driver.find_element_by_id("main_zipcode").send_keys(zipcodeadd)
    phone1 = config.driver.find_element_by_name("phone").send_keys(phoneone)
    phone2 = config.driver.find_element_by_name("other_phone").send_keys(phonetwo)
    email = config.driver.find_element_by_name("main_email").send_keys(emaila)
    
    #same as patient address button
    sameaspatientaddress = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[25]/td[2]/button").click()

    #Living Situation
    livings = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[35]/td[2]/div/label[2]/input").click() #Lives Alone
    assistance = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[36]/td[2]/div/label[4]/input").click() #Occasional short-term
    ls_caregiver = config.driver.find_element_by_id("ls_caregiver").send_keys(cgname)
    ls_caregiver_phone = config.driver.find_element_by_id("ls_caregiver_phone").send_keys(cgphone)
    
    #Emergency Contact
    ec_name = config.driver.find_element_by_id("ec_name").send_keys(ecname)
    ec_relationship = config.driver.find_element_by_id("ec_relationship").send_keys(ecrel)
    ec_phone = config.driver.find_element_by_id("ec_phone").send_keys(ecp1)
    ec_other_phone = config.driver.find_element_by_id("ec_other_phone").send_keys(ecp2)
    
# ------------------------------------------------------------------------------------------------
#  beyond this part, the automation will automatically select the first entry of each dropdown
# ------------------------------------------------------------------------------------------------
    time.sleep(2)
    
    #Physician Information
    attending_physician = config.driver.find_element_by_css_selector("#physician_attending_chosen > .chosen-single").click()
    at_result = config.driver.find_element_by_css_selector(".active-result:nth-child(2)").click()
    
    time.sleep(5)
    scrolldown = config.driver.execute_script("window.scrollTo(0,1000)")
    #Primary Insurance Information
    primary_insurance = config.driver.find_element_by_css_selector("#primary_insurance_chosen > .chosen-single").click()
    time.sleep(2)
    pi_result = config.driver.find_element_by_css_selector("#primary_insurance_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    #Scrolldown
    scrolldown = config.driver.execute_script("window.scrollTo(0,6500)")
    
    #Admission type
    admission_type = config.driver.find_element_by_css_selector("#admissiontype_chosen > .chosen-single").click()
    at_result = config.driver.find_element_by_css_selector("#admissiontype_chosen .active-result:nth-child(1)").click()
    
    pointoforigin = config.driver.find_element_by_css_selector("#point_of_origin_chosen > .chosen-single").click()
    poo_result = config.driver.find_element_by_css_selector("#point_of_origin_chosen .active-result:nth-child(1)").click()
    
    time.sleep(2)
    referral_type = config.driver.find_element_by_css_selector("#referral_type_chosen > .chosen-single").click()
    time.sleep(2)
    rt_result = config.driver.find_element_by_css_selector("#referral_type_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    referral_source = config.driver.find_element_by_css_selector("#referral_source_id_chosen > .chosen-single").click()
    time.sleep(2)
    rs_result = config.driver.find_element_by_css_selector("#referral_source_id_chosen .active-result:nth-child(2)").click()
    
    #Hospitalization Information
    hospital = config.driver.find_element_by_css_selector("#hospital_id_chosen > .chosen-single").click()
    time.sleep(5)
    h_result = config.driver.find_element_by_css_selector("#hospital_id_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    h_admitdate = config.driver.find_element_by_id("admit_date").send_keys(hadmit)
    h_discharge = config.driver.find_element_by_id("discharge_date").send_keys(hdc)
    
    #Diagnosis / Pre-admission Orders
    dsurgery = config.driver.find_element_by_id("diagnosis_surgery").send_keys(dsur)
    option = config.driver.find_element_by_xpath("//*[@id='diagnosis_allergies']/div/div/input").click()
    dallergies = config.driver.find_element_by_xpath("//*[@id='diagnosis_allergies']/div/div/input").send_keys(dallergies, Keys.ENTER)

    #M0080
    mo = ""
    
    if moeigthy == "RN":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[1]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_rn_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_rn_chosen .active-result:nth-child(1)").click()
        
    elif moeigthy == "PT":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[2]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_pt_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_pt_chosen .active-result:nth-child(1)").click()
        
    elif moeigthy == "SLP":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[3]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_st_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_st_chosen .active-result").click()
        
    elif moeigthy == "OT":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[4]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_ot_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_ot_chosen .active-result:nth-child(1)").click()
    
    mo.click()
   
    #choose the first CM
    case_manager = config.driver.find_element_by_css_selector("#cs_cm_chosen > .chosen-single").click()
    cm_result = config.driver.find_element_by_css_selector("#cs_cm_chosen .active-result:nth-child(1)").click()
    
    # SAVE button
    save = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div/div/div/div/div[1]/button[2]").click()
       
    time.sleep(5)
    
   
    #config.driver.close()


def preadmission_nonmed(
        refdate,
        reftime,
        lname,
        fname,
        mi,
        bdate,
        sex,
        mstatus,
        ethn,
        langspoken,
        ssnumber,
        streetaddress,
        adddirection,
        majorcstreet,
        city,
        stateadd,
        zipcodeadd,
        phoneone,
        phonetwo,
        emaila,
        cgname, 
        cgphone,
        ecname,
        ecrel,
        ecp1,
        ecp2,
        hadmit,
        hdc,
        dsur,
        dallergies,
        moeigthy
        ):
    
    time.sleep(5)
    
    skip_eligibility = config.driver.find_element_by_link_text("Skip").click() #skip button

# ------------------------------------------------------------------------------------------------
#  MAIN PATIENT ADMISSION CODE
# ------------------------------------------------------------------------------------------------

    #Patient Information
    referral_date = config.driver.find_element_by_id("refDate").send_keys(refdate)
    time.sleep(2)
    referral_time = config.driver.find_element_by_xpath('//*[@id="referral_time"]/input').send_keys(reftime)
    mrn = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/label/input").click()
    last_name = config.driver.find_element_by_id("last_name").send_keys(lname)
    first_name = config.driver.find_element_by_id("first_name").send_keys(fname)
    middle_initial = config.driver.find_element_by_id("mi").send_keys(mi)
    birthdate = config.driver.find_element_by_id("birthdate").send_keys(bdate)
    
    #conditional formatting
    gender = ""
    if sex == "Male":
        gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[1]/input")
    elif sex == "Female":
        gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[2]/input")
    time.sleep(1)
    gender.click()
    
    #code for choosing select
    option = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/a").click() #click the select
    mstext = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/div/div/input").send_keys(mstatus, Keys.ENTER) #search the value
    option = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").click()
    ethnicity = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").send_keys(ethn, Keys.ENTER)
    
    #Language Spoken
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").click()
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(langspoken)
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(Keys.ENTER)

    ssn = config.driver.find_element_by_id("ssNumber").send_keys(ssnumber)
    
    #Patient Address
    strtadd = config.driver.find_element_by_id("main_line1").send_keys(streetaddress)
    addd = config.driver.find_element_by_id("main_line2").send_keys(adddirection)
    mcs = config.driver.find_element_by_id("main_street").send_keys(majorcstreet)
    cityadd = config.driver.find_element_by_id("main_city").send_keys(city)
    
    #State Code
    config.driver.find_element(By.XPATH, "//tr[20]/td[2]/div/div/div/a").click()
    time.sleep(2)
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").click()
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").send_keys(stateadd, Keys.ENTER)

    zipcode = config.driver.find_element_by_id("main_zipcode").send_keys(zipcodeadd)
    phone1 = config.driver.find_element_by_name("phone").send_keys(phoneone)
    phone2 = config.driver.find_element_by_name("other_phone").send_keys(phonetwo)
    email = config.driver.find_element_by_name("main_email").send_keys(emaila)
    
    #same as patient address button
    sameaspatientaddress = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[25]/td[2]/button").click()

    #Living Situation
    livings = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[35]/td[2]/div/label[2]/input").click() #Lives Alone
    assistance = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[36]/td[2]/div/label[4]/input").click() #Occasional short-term
    ls_caregiver = config.driver.find_element_by_id("ls_caregiver").send_keys(cgname)
    ls_caregiver_phone = config.driver.find_element_by_id("ls_caregiver_phone").send_keys(cgphone)
    
    #Emergency Contact
    ec_name = config.driver.find_element_by_id("ec_name").send_keys(ecname)
    ec_relationship = config.driver.find_element_by_id("ec_relationship").send_keys(ecrel)
    ec_phone = config.driver.find_element_by_id("ec_phone").send_keys(ecp1)
    ec_other_phone = config.driver.find_element_by_id("ec_other_phone").send_keys(ecp2)
    
# ------------------------------------------------------------------------------------------------
#  beyond this part, the automation will automatically select the first entry of each dropdown
# ------------------------------------------------------------------------------------------------
    time.sleep(2)
    
    #Physician Information
    attending_physician = config.driver.find_element_by_css_selector("#physician_attending_chosen > .chosen-single").click()
    at_result = config.driver.find_element_by_css_selector(".active-result:nth-child(2)").click()
    
    time.sleep(5)
    scrolldown = config.driver.execute_script("window.scrollTo(0,1000)")
    
    time.sleep(5)
    # Primary Insurance
    primary_insurance = config.driver.find_element_by_css_selector("#primary_insurance_chosen > .chosen-single")
    time.sleep(5)
    primary_insurance.click()
    time.sleep(2)
    primary_insurancedd = config.driver.find_element_by_xpath('//*[@id="primary_insurance_chosen"]/div/div/input')
    primary_insurancedd.send_keys('other', Keys.ENTER)
    
    time.sleep(2)
    
    #authorization number
    authorization_num = config.driver.find_element_by_xpath('//*[@id="primary_insurance_authorization"]').send_keys(ssnumber)
    
    time.sleep(2)
    #Scrolldown
    scrolldown = config.driver.execute_script("window.scrollTo(0,6500)")
    
    #Admission type
    admission_type = config.driver.find_element_by_css_selector("#admissiontype_chosen > .chosen-single").click()
    at_result = config.driver.find_element_by_css_selector("#admissiontype_chosen .active-result:nth-child(1)").click()
    
    pointoforigin = config.driver.find_element_by_css_selector("#point_of_origin_chosen > .chosen-single").click()
    poo_result = config.driver.find_element_by_css_selector("#point_of_origin_chosen .active-result:nth-child(1)").click()
    
    time.sleep(2)
    referral_type = config.driver.find_element_by_css_selector("#referral_type_chosen > .chosen-single").click()
    time.sleep(2)
    rt_result = config.driver.find_element_by_css_selector("#referral_type_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    referral_source = config.driver.find_element_by_css_selector("#referral_source_id_chosen > .chosen-single").click()
    time.sleep(2)
    rs_result = config.driver.find_element_by_css_selector("#referral_source_id_chosen .active-result:nth-child(2)").click()
    
    #Hospitalization Information
    hospital = config.driver.find_element_by_css_selector("#hospital_id_chosen > .chosen-single").click()
    time.sleep(5)
    h_result = config.driver.find_element_by_css_selector("#hospital_id_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    h_admitdate = config.driver.find_element_by_id("admit_date").send_keys(hadmit)
    h_discharge = config.driver.find_element_by_id("discharge_date").send_keys(hdc)
    
    #Diagnosis / Pre-admission Orders
    dsurgery = config.driver.find_element_by_id("diagnosis_surgery").send_keys(dsur)
    option = config.driver.find_element_by_xpath("//*[@id='diagnosis_allergies']/div/div/input").click()
    dallergies = config.driver.find_element_by_xpath("//*[@id='diagnosis_allergies']/div/div/input").send_keys(dallergies, Keys.ENTER)

    #M0080
    mo = ""
    
    if moeigthy == "RN":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[1]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_rn_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_rn_chosen .active-result:nth-child(1)").click()
        
    elif moeigthy == "PT":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[2]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_pt_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_pt_chosen .active-result:nth-child(1)").click()
        
    elif moeigthy == "SLP":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[3]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_st_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_st_chosen .active-result").click()
        
    elif moeigthy == "OT":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[4]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_ot_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_ot_chosen .active-result:nth-child(1)").click()
    
    mo.click()
   
    #choose the first CM
    case_manager = config.driver.find_element_by_css_selector("#cs_cm_chosen > .chosen-single").click()
    cm_result = config.driver.find_element_by_css_selector("#cs_cm_chosen .active-result:nth-child(1)").click()
    
    # SAVE button
    save = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div/div/div/div/div[1]/button[2]").click()
       
    time.sleep(5)
    
   
    #config.driver.close()




def preadmission_nonmed_auth(
        refdate,
        reftime,
        plannedsoc,
        lname,
        fname,
        mi,
        bdate,
        sex,
        mstatus,
        ethn,
        langspoken,
        ssnumber,
        streetaddress,
        adddirection,
        majorcstreet,
        city,
        stateadd,
        zipcodeadd,
        phoneone,
        phonetwo,
        emaila,
        cgname, 
        cgphone,
        ecname,
        ecrel,
        ecp1,
        ecp2,
        hadmit,
        hdc,
        dsur,
        dallergies,
        moeigthy
        ):
    
    time.sleep(5)
    
    skip_eligibility = config.driver.find_element_by_link_text("Skip").click() #skip button

# ------------------------------------------------------------------------------------------------
#  MAIN PATIENT ADMISSION CODE
# ------------------------------------------------------------------------------------------------

    #Patient Information
    referral_date = config.driver.find_element_by_id("refDate").send_keys(refdate)
    time.sleep(2)
    referral_time = config.driver.find_element_by_xpath('//*[@id="referral_time"]/input').send_keys(reftime)
    mrn = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/div/label/input").click()
    preadmission_date = config.driver.find_element_by_id("pre_admission_date").send_keys(plannedsoc)
    last_name = config.driver.find_element_by_id("last_name").send_keys(lname)
    first_name = config.driver.find_element_by_id("first_name").send_keys(fname)
    middle_initial = config.driver.find_element_by_id("mi").send_keys(mi)
    birthdate = config.driver.find_element_by_id("birthdate").send_keys(bdate)
    
    #conditional formatting
    gender = ""
    if sex == "Male":
        gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[1]/input")
    elif sex == "Female":
        gender = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[10]/td[2]/div/label[2]/input")
    time.sleep(1)
    gender.click()
    
    #code for choosing select
    option = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/a").click() #click the select
    mstext = config.driver.find_element_by_xpath("//*[@id='marital_status_chosen']/div/div/input").send_keys(mstatus, Keys.ENTER) #search the value
    option = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").click()
    ethnicity = config.driver.find_element_by_xpath("//*[@id='ethnicities_chosen']/ul/li/input").send_keys(ethn, Keys.ENTER)
    
    #Language Spoken
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").click()
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(langspoken)
    config.driver.find_element(By.CSS_SELECTOR, ".ui-select-search").send_keys(Keys.ENTER)

    ssn = config.driver.find_element_by_id("ssNumber").send_keys(ssnumber)
    
    #Patient Address
    strtadd = config.driver.find_element_by_id("main_line1").send_keys(streetaddress)
    addd = config.driver.find_element_by_id("main_line2").send_keys(adddirection)
    mcs = config.driver.find_element_by_id("main_street").send_keys(majorcstreet)
    cityadd = config.driver.find_element_by_id("main_city").send_keys(city)
    
    #State Code
    config.driver.find_element(By.XPATH, "//tr[20]/td[2]/div/div/div/a").click()
    time.sleep(2)
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").click()
    config.driver.find_element(By.CSS_SELECTOR, "#main_state_chosen input").send_keys(stateadd, Keys.ENTER)

    zipcode = config.driver.find_element_by_id("main_zipcode").send_keys(zipcodeadd)
    phone1 = config.driver.find_element_by_name("phone").send_keys(phoneone)
    phone2 = config.driver.find_element_by_name("other_phone").send_keys(phonetwo)
    email = config.driver.find_element_by_name("main_email").send_keys(emaila)
    
    #same as patient address button
    sameaspatientaddress = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[25]/td[2]/button").click()

    #Living Situation
    livings = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[35]/td[2]/div/label[2]/input").click() #Lives Alone
    assistance = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[36]/td[2]/div/label[4]/input").click() #Occasional short-term
    ls_caregiver = config.driver.find_element_by_id("ls_caregiver").send_keys(cgname)
    ls_caregiver_phone = config.driver.find_element_by_id("ls_caregiver_phone").send_keys(cgphone)
    
    #Emergency Contact
    ec_name = config.driver.find_element_by_id("ec_name").send_keys(ecname)
    ec_relationship = config.driver.find_element_by_id("ec_relationship").send_keys(ecrel)
    ec_phone = config.driver.find_element_by_id("ec_phone").send_keys(ecp1)
    ec_other_phone = config.driver.find_element_by_id("ec_other_phone").send_keys(ecp2)
    
# ------------------------------------------------------------------------------------------------
#  beyond this part, the automation will automatically select the first entry of each dropdown
# ------------------------------------------------------------------------------------------------
    time.sleep(2)
    
    #Physician Information
    attending_physician = config.driver.find_element_by_css_selector("#physician_attending_chosen > .chosen-single").click()
    at_result = config.driver.find_element_by_css_selector(".active-result:nth-child(2)").click()
    
    time.sleep(5)
    scrolldown = config.driver.execute_script("window.scrollTo(0,1000)")
    
    time.sleep(5)
    # Primary Insurance
    primary_insurance = config.driver.find_element_by_css_selector("#primary_insurance_chosen > .chosen-single")
    time.sleep(5)
    primary_insurance.click()
    time.sleep(2)
    primary_insurancedd = config.driver.find_element_by_xpath('//*[@id="primary_insurance_chosen"]/div/div/input')
    primary_insurancedd.send_keys('other', Keys.ENTER)
    
    time.sleep(2)
    
    #authorization number
    authorization_num = config.driver.find_element_by_xpath('//*[@id="primary_insurance_authorization"]').send_keys(ssnumber)
    
    time.sleep(2)
    #Scrolldown
    scrolldown = config.driver.execute_script("window.scrollTo(0,6500)")
    
    #Admission type
    admission_type = config.driver.find_element_by_css_selector("#admissiontype_chosen > .chosen-single").click()
    at_result = config.driver.find_element_by_css_selector("#admissiontype_chosen .active-result:nth-child(1)").click()
    
    pointoforigin = config.driver.find_element_by_css_selector("#point_of_origin_chosen > .chosen-single").click()
    poo_result = config.driver.find_element_by_css_selector("#point_of_origin_chosen .active-result:nth-child(1)").click()
    
    time.sleep(2)
    referral_type = config.driver.find_element_by_css_selector("#referral_type_chosen > .chosen-single").click()
    time.sleep(2)
    rt_result = config.driver.find_element_by_css_selector("#referral_type_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    referral_source = config.driver.find_element_by_css_selector("#referral_source_id_chosen > .chosen-single").click()
    time.sleep(2)
    rs_result = config.driver.find_element_by_css_selector("#referral_source_id_chosen .active-result:nth-child(2)").click()
    
    #Hospitalization Information
    hospital = config.driver.find_element_by_css_selector("#hospital_id_chosen > .chosen-single").click()
    time.sleep(5)
    h_result = config.driver.find_element_by_css_selector("#hospital_id_chosen .active-result:nth-child(2)").click()
    
    time.sleep(2)
    h_admitdate = config.driver.find_element_by_id("admit_date").send_keys(hadmit)
    h_discharge = config.driver.find_element_by_id("discharge_date").send_keys(hdc)
    
    #Diagnosis / Pre-admission Orders
    dsurgery = config.driver.find_element_by_id("diagnosis_surgery").send_keys(dsur)
    option = config.driver.find_element_by_xpath("//*[@id='diagnosis_allergies']/div/div/input").click()
    dallergies = config.driver.find_element_by_xpath("//*[@id='diagnosis_allergies']/div/div/input").send_keys(dallergies, Keys.ENTER)

    #M0080
    mo = ""
    
    if moeigthy == "RN":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[1]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_rn_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_rn_chosen .active-result:nth-child(1)").click()
        
    elif moeigthy == "PT":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[2]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_pt_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_pt_chosen .active-result:nth-child(1)").click()
        
    elif moeigthy == "SLP":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[3]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_st_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_st_chosen .active-result").click()
        
    elif moeigthy == "OT":
        mo = config.driver.find_element_by_xpath("//*[@id='content']/data/div[2]/div/ng-form/fieldset/table/tbody/tr[68]/td/div/label[4]/input")
        config.driver.find_element(By.CSS_SELECTOR, "#cs_ot_chosen > .chosen-single").click()
        config.driver.find_element(By.CSS_SELECTOR, "#cs_ot_chosen .active-result:nth-child(1)").click()
    
    mo.click()
   
    #choose the first CM
    case_manager = config.driver.find_element_by_css_selector("#cs_cm_chosen > .chosen-single").click()
    cm_result = config.driver.find_element_by_css_selector("#cs_cm_chosen .active-result:nth-child(1)").click()
    
    # SAVE button
    save = config.driver.find_element_by_xpath("//*[@id='titleNoteBar']/div/div/div/div/div[1]/button[2]").click()
       
    time.sleep(5)
    
   
    #config.driver.close()





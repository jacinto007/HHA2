from controllers import config, login, function_admission, function_oasis, servers, patient_dashboard
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException
import pymsgbox
from datetime import date

# Useful variables from config.py
todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")
name_random = config.randomize_name()
ssn = config.randomize_ssn()
today = date.today()
todaynow = today.strftime("%m/%d/%Y")   

taskdateconvert = datetime.strptime(todaynow, '%m/%d/%Y') #2. Convert to date string
addeddaystodate = timedelta(days=1000) #3. Add days to the date
datetotal = taskdateconvert + addeddaystodate #4. add total
finaltaskdate = datetime.strftime(datetotal, '%m/%d/%Y') #5. convert again to date string for final date  
print(finaltaskdate)


def personalinfo(
        lastname,
        birthdate,
        ethnicity,
        marstat,
        discipline,
        title,
        hirecateg,
        posi,
        comp,
        addr,
        lang,
        lvl
        ):
    time.sleep(2)

    # ----------------------------------------------------------
    # Personal Information 
    # ----------------------------------------------------------
    fname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//tr[1]/td[2]/div/input').send_keys(name_random)
    lname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//tr[2]/td[2]/div/input').send_keys(lastname)
    gender_m = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]//label[1]/input').click()
    bdate = config.driver.find_element_by_xpath('//*[@id="birthdate"]').send_keys(birthdate)
    
    ethdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/a').click()
    ethtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/div/div/input').send_keys(ethnicity, Keys.ENTER)
    
    maritalstatdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[8]/td[2]/div/div/div/a').click()
    maritalstattb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[8]/td[2]/div/div/div/div/div/input').send_keys(marstat, Keys.ENTER)
    
    
    disciplinedd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[9]/td[2]/div/div/div/a').click()
    disciplinetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[9]/td[2]/div/div/div/div/div/input').send_keys(discipline, Keys.ENTER)
    
    titledd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[10]/td[2]/div/div/div/a').click()
    titletb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[10]/td[2]/div/div/div/div/div/input').send_keys(title, Keys.ENTER)
    
    hirecategdd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[11]/td[2]/div/div/div/a').click()
    hirecategtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[11]/td[2]/div/div/div/div/div/input').send_keys(hirecateg, Keys.ENTER)
    
    positiondd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[12]/td[2]/div/div/div/a').click()
    positiontb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[12]/td[2]/div/div/div/div/div/input').send_keys(posi, Keys.ENTER)
    
    ssntb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[13]/td[2]/div/input').send_keys(ssn)
    clinicianid = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[14]/td[2]/div/input').send_keys(ssn)
    company = config.driver.find_element_by_name('company').send_keys(comp)
    address = config.driver.find_element_by_name('address1').send_keys(addr)
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,5000)")
    time.sleep(3)
    phone = config.driver.find_element_by_name('phone').send_keys(ssn)
    emailtb = config.driver.find_element_by_name('email').send_keys(name_random + '@mailinator.com')
    hireddate = config.driver.find_element_by_id('hireddate').send_keys(todaynow)
    
    terminationdate = config.driver.find_element_by_id('terminationdate').send_keys(finaltaskdate)
    
    for x in range(1,5):
        for y in range(2,4):
            langdd1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr[1]/td['+ str(y) +']/div/div/div/a').click()
            langtb1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr[1]/td['+ str(y) +']/div/div/div/div/div/input').send_keys(lang, Keys.ENTER)
            dd1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr['+ str(x) +']/td['+ str(y) +']/div/div/div/a').click()
            tb1 = config.driver.find_element_by_xpath('//*[@id="content"]//tbody/tr['+ str(x) +']/td['+ str(y) +']/div/div/div/div/div/input').send_keys(lvl, Keys.ENTER)
            
    scrollup= config.driver.execute_script("window.scrollTo(0,0)")
        
def professionalcreds():
    time.sleep(3)

    # ----------------------------------------------------------
    # Professional Credentials
    # ----------------------------------------------------------
    profcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[2]/a').click()
    time.sleep(3)
    
    profid = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr[1]/td[3]/div/input').send_keys(ssn)
    proeffdate = config.driver.find_element_by_xpath('//*[@id="efdateu0"]').send_keys(todaynow)
    proexpdate = config.driver.find_element_by_xpath('//*[@id="exdate0"]').send_keys(finaltaskdate)
    prodatever = config.driver.find_element_by_xpath('//*[@id="verdate0"]').send_keys(todaynow)
    proverby = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr[1]/td[7]/div/input').send_keys('Khenard Figuracion')
    
    for x in range(2,11):
        l = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/a').click()
        l21 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/a').click()
        no = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[3]/fieldset/table/tbody/tr['+ str(x) +']/td[2]/div/div/div/div/ul/li[2]').click()
    
def healthcreds():
    time.sleep(3)
    
    # ----------------------------------------------------------
    # Health Credentials
    # ----------------------------------------------------------
    
    # Other buttons
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div/button[2]')
    systemuser_yes = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]')
    systemuser_no = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[2]')
    
    time.sleep(3)
    healthcreds = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div/div[2]/ul/li[3]/a').click()
   
    hc1 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[1]/td[2]/div/div/div/a').click()
    hc2 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[1]/td[2]/div/div/div/a').click()
    hcno = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[1]/td[2]/div/div/div/div/ul/li[2]').click()
    hc3 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[3]/td[2]/div/div/div/a').click()
    hc3 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[3]/td[2]/div/div/div/a').click()
    hcno1 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[4]/fieldset/table/tbody/tr[3]/td[2]/div/div/div/div/ul/li[2]').click()

    # ----------------------------------------------------------
    # Saving
    # ----------------------------------------------------------
    time.sleep(3)
    savebtn.click()
    time.sleep(3)
    systemuser_yes.click()
    time.sleep(5)
    discardyes = config.driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/button[1]').click()
    
    
def verificationprocess(userole, test_server):
    
    p = config.driver.current_window_handle # Get the current window
    parent = config.driver.window_handles[0]

    time.sleep(2)

    # ----------------------------------------------------------
    # create user system account and mailinator
    # ----------------------------------------------------------
    time.sleep(5)
    
    
    useremail = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[3]/td[2]/div/input').get_attribute('value')
    username = useremail.replace('@mailinator.com', '')
    
    usernametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[2]/td[2]/div/input').send_keys(username)
    activeuser = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[5]/td[2]/div/ng-form/label[1]/input').click()
    
    # Choose User role
    userroledd = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[7]/td[2]/div/div/div/a').click()
    useroletb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table/tbody/tr[7]/td[2]/div/div/div/div/div/input').send_keys(userole, Keys.ENTER)
    
    time.sleep(2)     
    scroll= config.driver.execute_script("window.scrollTo(0,5000)")
    
    commenttb = config.driver.find_element_by_name('remarks').send_keys('This user is added through automated testing')
    
    time.sleep(2)
    saveaccountbtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div/button[2]').click()
    
    time.sleep(5)
    
    servers.logout() # Logout
    
    time.sleep(5)
    # Go to mailinator.com
    config.driver.get("https://www.mailinator.com/")
    print(useremail)
    mail = config.driver.find_element_by_xpath('//*[@id="addOverlay"]').send_keys(useremail, Keys.ENTER)
    time.sleep(3)
    inbox1 = config.driver.find_element_by_xpath('/html/body/div/main/div[2]/div[3]/div/div[4]/div/div/table/tbody/tr/td[2]').click()
    time.sleep(5)
    
    # Get the valus of Username and auto-generated password 
    config.driver.switch_to.frame(config.driver.find_element_by_id('html_msg_body'))
    username = config.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/span[2]').text
    print(username)
    userpass =config.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/span[4]').text
    print(userpass)
    time.sleep(5)
    
    config.driver.execute_script("window.open('about:blank','secondtab');")
    config.driver.switch_to.window("secondtab")
    
    if test_server == "qa":
        config.driver.get("https://qado.medisource.com/login")
        time.sleep(2)
        
    elif test_server == "live": 
        config.driver.get("https://app.medisource.com/login")
        time.sleep(2)
        
    
    chld = config.driver.window_handles[1]
    time.sleep(3)
        
    login.login(username, userpass)
    time.sleep(3)
    
    
    config.driver.switch_to.window(parent) # Switch to first tab
         
    backtoinbox = config.driver.find_element_by_xpath('//*[@id="email_pane"]/div/div[1]/div[2]/a').click()
    time.sleep(3)
    
    inbox1 = config.driver.find_element_by_xpath('/html/body/div/main/div[2]/div[3]/div/div[4]/div/div/table/tbody/tr/td[2]').click()
    time.sleep(3)
    
    config.driver.switch_to.frame(config.driver.find_element_by_id('html_msg_body'))
    
    verificationcode = config.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td/table[2]/tbody/tr[2]/td').text
    print(verificationcode)
    time.sleep(3)
        
    config.driver.switch_to.window(chld) # Switch back to the 2nd tab
         
    time.sleep(3)
    verifycode = config.driver.find_element_by_xpath('//*[@id="token"]').send_keys(verificationcode)
    verifybtn = config.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/section/div/div/form/div[4]/button').click()
        

    defaultans = 'testtest',
    newuserpass = 'Tester2021!'
    
    userpassmail = userpass
    
    time.sleep(20)
    
    # Security Questions
    q1 = config.driver.find_element_by_xpath('//*[@id="q1"]/div/a').click()
    qa1 = config.driver.find_element_by_xpath('//*[@id="q1"]/div/div/ul/li[1]').click()
    a1 = config.driver.find_element_by_xpath('//*[@id="answer1"]').send_keys(defaultans)
    time.sleep(2)
    q2 = config.driver.find_element_by_xpath('//*[@id="q2"]/div/a').click()
    qa2 = config.driver.find_element_by_xpath('//*[@id="q2"]/div/div/ul/li[1]').click()
    a2 = config.driver.find_element_by_xpath('//*[@id="answer2"]').send_keys(defaultans)
    time.sleep(2)
    
    nextbtn = config.driver.find_element_by_xpath('//*[@id="securityquestions"]/form/div[5]/button').click()
    
    # Change Password
    currentpass = config.driver.find_element_by_xpath('//*[@id="temppass"]').send_keys(userpassmail)
    newpass = config.driver.find_element_by_xpath('//*[@id="newpass"]').send_keys(newuserpass)
    confirmpass = config.driver.find_element_by_xpath('//*[@id="confirmpass"]').send_keys(newuserpass)
    time.sleep(2)
    
    finishbtn = config.driver.find_element_by_xpath('//*[@id="passwordupdate"]/form/div[4]/div[2]/button').click()
    
    time.sleep(3)
    
    okbtn = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
from controllers import config
import pyautogui, sys
import random, time
from datetime import date
from datetime import datetime, timedelta


todaytime = config.timenow()
todaydate = config.datenow()
plustime = (datetime.now() + timedelta(hours=5)).strftime("%H:%M")


def ThirtyDaySummary():
    
    time.sleep(2)
    openTb = config.driver.find_element_by_xpath('//*[@id="parent"]/div/div[3]/div/table/tbody/tr/td[2]')
    openTb.click()
    time.sleep(2)
    editBtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div[2]/div/button')
    editBtn.click()
    time.sleep(2)
    LoadBtn = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/button')
    LoadBtn.click()
    time.sleep(2)
    confirmBtn = config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]')
    confirmBtn.click()
    time.sleep(2)
    #other Diagnoses
    inputText = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[1]/tbody/tr[7]/td/div[2]/tags-input/div/div/input')
    inputText.send_keys("Diagnosed with Severe Marupokness.")
    time.sleep(2)
    #SCIC/Change in Diagnosis/Events/Physician Orders
    check1 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[2]/tbody/tr[2]/td/span[1]/label/input')
    check1.click()
    time.sleep(2)
    check2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[2]/tbody/tr[2]/td/span[2]/label/input')
    check2.click()
    time.sleep(2)
    inputText2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[2]/tbody/tr[2]/td/div/div/div/input')
    inputText2.send_keys("Kailangan ng Biogesic.")
    time.sleep(2)
    comment = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[2]/tbody/tr[4]/td/div[2]/input')
    comment.send_keys("Gusto ko ng wantawsan syetemel.")
    time.sleep(2)
    #VS Monitor
    Pt = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[3]/tbody/tr[4]/td[8]/div/div/div/input')
    Pt.send_keys("Lorem Ipsum 1")
    time.sleep(2)
    INR = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[3]/tbody/tr[4]/td[9]/div/div/div/input')
    INR.send_keys("Lorem Ipsum 2")
    time.sleep(2)
    comment2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[3]/tbody/tr[5]/td/div[2]/textarea')
    comment2.send_keys("Click Click Click hello.")
    time.sleep(2)
    #Medication Management
    check3 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[4]/tbody/tr[5]/td[2]/label[1]/input')
    check3.click()
    time.sleep(2)
    check4 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[4]/tbody/tr[5]/td[2]/label[3]/input')
    check4.click()
    time.sleep(2)
    comment3 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[4]/tbody/tr[6]/td[2]/textarea')
    comment3.send_keys("What if we all living because we are batteries.")
    time.sleep(2)
    #Laboratory/Diagnostic Tests
    comment4 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[5]/tbody/tr[3]/td[2]/textarea')
    comment4.send_keys("Am I mister meeseeks, cos for me existence is pain.")
    time.sleep(2)
    #Procedures
    comment5 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/div/table/tbody/tr/td/table[6]/tbody/tr[2]/td/div[2]/textarea')
    comment5.send_keys("Sit Down, be humble, be humble..")
    time.sleep(2)
    
    #save button
    save = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[3]')
    save.click()
    time.sleep(2)
    
    scrollup = config.driver.execute_script("window.scrollTo(1000,0)")
    #upload file here
    time.sleep(2)

    
def CommunicationNotesInput():
    CCNdate = config.driver.find_element_by_id("date")
    CCNdate.send_keys(todaydate)
    time.sleep(2)
    title = config.driver.find_element_by_name('subject')
    title.click()
    time.sleep(2)
    ChooseTitle = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/div[2]/ul/li[1]')
    ChooseTitle.click()
    time.sleep(2)
    CCNtime = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/table/tbody/tr/td/table/tbody/tr[2]/td[3]/div/input')
    CCNtime.send_keys("23:30")
    time.sleep(2)
    CommNotes = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/table/tbody/tr/td/table/tbody/tr[4]/td/div/textarea')
    CommNotes.send_keys("Here we are don't turn away now, we are the warriors that built this town.")
    time.sleep(2)
    chckbx = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr[3]/td[1]/div/label/input')
    chckbx.click()
    time.sleep(2)
    select = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr[3]/td[2]/div/div/div/a')
    select.click()
    time.sleep(2)
    choose = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr[3]/td[2]/div/div/div/div/ul/li')
    choose.click()
    time.sleep(2)
    chckbx2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/div/fieldset/table/tbody/tr/td/table/tbody/tr[7]/td[2]/div[1]/label/input')
    chckbx2.click()
    time.sleep(2)
    
    save = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[2]')
    save.click()
    time.sleep(2)
    
    
def HHAplanInput():
    
    HHAdate = config.driver.find_element_by_id("visitDate")
    HHAdate.send_keys(todaydate)
    time.sleep(2)
    timeIn = config.driver.find_element_by_id("timeIn")
    timeIn.send_keys("12:30")
    time.sleep(2)
    timeOut = config.driver.find_element_by_id("timeOut")
    timeOut.send_keys("01:30")
    time.sleep(2)
    #functional limitatios
    Input = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/fieldset/div/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/div[2]/div/input')
    Input.send_keys("Mga may alias na iisa, inisa-isa.")
    time.sleep(2)
    #activities permitted
    Input1 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/div[2]/div/input')
    Input1.send_keys("This crown is killing lives, playing with lies.")
    time.sleep(2)
    #Safety Measures
    Input2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/fieldset/div/table[4]/tbody/tr[2]/td/table/tbody/tr[5]/td[3]/div[2]/div/input')
    Input2.send_keys("At ngayon ay magbabalik sayo, yan ang panalangin ko.")
    time.sleep(2)
    #fluid intake
    choose1 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/fieldset/div/table[5]/tbody/tr[18]/td[4]/table/tbody/tr[1]/td/label/input')
    choose1.click()
    time.sleep(2)
    Input3 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/fieldset/div/table[5]/tbody/tr[18]/td[4]/table/tbody/tr[2]/td/div/input')
    Input3.send_keys("Kumain ng gulay na makulay, para masigla ang buhay.")
    time.sleep(2)
    #additional observation
    Input4 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/fieldset/div/table[7]/tbody/tr[2]/td/textarea')
    Input4.send_keys("Paint my love, would you paint my love it's the picture of thousand sunsets, it's the freedom of a thousand dove.")
    time.sleep(2)
    choose2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/fieldset/div/table[8]/tbody/tr/td[1]/label/input')
    choose2.click()
    time.sleep(2)
    Observationdate = config.driver.find_element_by_xpath('//*[@id="aor0003"]')
    Observationdate.send_keys("08/01/2021")
    time.sleep(2)
    Input5 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div[1]/fieldset/div/table[8]/tbody/tr/td[4]/input')
    Input5.send_keys("Lorem Ipsum123")
    time.sleep(2)
    
    
    save = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[2]')
    save.click()
    time.sleep(2)


def transferSummaryInput():
    
    transferdate = config.driver.find_element_by_xpath('//*[@id="transfer_date"]')
    transferdate.send_keys(todaydate)
    time.sleep(2)
    choosePhysician = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/div/div/a')
    choosePhysician.click()
    time.sleep(2)
    selectPhysician =config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/div/div/div/ul/li')
    selectPhysician.click()
    time.sleep(2)
    
    #other reason
    #inputReason1 = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td/table/tbody/tr[7]/td/div[2]/div/textarea')
    #inputReason1.send_keys("Gusto ko kumain ng Jollibee sweet and spicy chicken. Ugh dang, craving is me super")
    #time.sleep(2)
    
     # sa part na ito hinanap ko na lahat ng checkbox sa form at iclick, hindi na siya sa per section 
    items = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td').text
    subjectmatter = items.split('\n')
    removeitem = {"Other reasons:"}
    subjectmatter = [ele for ele in subjectmatter if ele not in removeitem]
    print(subjectmatter)
    for x in subjectmatter:
        finditem = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td//label[contains(string(), "'+ x +'")]')
        finditem.click()
    
    
    #transfer to
    inputReason2 = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/table[4]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/input')
    inputReason2.send_keys("Go Go power rangers")
    time.sleep(2)
    #reason for transfer
    inputReason3 = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/table[5]/tbody/tr[2]/td/table/tbody/tr[3]/td/input')
    inputReason3.send_keys("Go Go zaido parating na ang mga zaido, Blue, Red, Green.")
    time.sleep(2)
    #current physical 
    inputReason4 = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[2]/div/input')
    inputReason4.send_keys("Bata pa lang ko mam ganito na tinatrabaho ko.")
    time.sleep(2)
    #current functional status
    adlCheckbox = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/div[3]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/div[1]/label/input')
    adlCheckbox.click()
    time.sleep(2)
    mobCheckbox = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/div[3]/table[1]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/div/div[1]/label/input')
    mobCheckbox.click()
    time.sleep(2)
    #assistive device
    inputReason5 = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/div[3]/table[2]/tbody/tr/td[2]/div/input')
    inputReason5.send_keys("I'm a cat person haha SKL")
    time.sleep(2)
    #summary of care
    inputReason6 = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/table[6]/tbody/tr[2]/td/div/div/textarea')
    inputReason6.send_keys("How could we know a greater nightmare was hanging in the air?")
    time.sleep(2)
    #discipline
    inputReason7 = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/table[7]/tbody/tr/td[2]/div/input')
    inputReason7.send_keys("Sana all binibisita.")
    time.sleep(2)
    #physician date
    PhysicianDate = config.driver.find_element_by_xpath('//*[@id="notification_date_physician"]')
    PhysicianDate.send_keys("06/05/2021")
    time.sleep(2)
    #Patient date
    PatientDate = config.driver.find_element_by_xpath('//*[@id="notification_date_patient"]')
    PatientDate.send_keys("06/10/2021")
    time.sleep(2)
    #send via
    sendviaCheckbox = config.driver.find_element_by_xpath('//*[@id="CommTransferSummary"]/div/div[1]/fieldset/table/tbody/tr/td/table[8]/tbody/tr[2]/td[4]/div/label[1]/input')
    sendviaCheckbox.click()
    time.sleep(2)
    #save
    saveTransfersum= config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[2]')
    saveTransfersum.click()
    time.sleep(7)
    
    
def dischargeSummaryInput():
    
    dischargedate = config.driver.find_element_by_xpath('//*[@id="dischargeDate"]')
    dischargedate.send_keys(todaydate)
    time.sleep(2)
    #diagnoses
    #primary
    inputReason1 = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[2]/td/div[1]/textarea')
    inputReason1.send_keys("Diagnose with marupokness.")
    time.sleep(2)
    #secondary
    inputReason2 = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[2]/td/div[2]/textarea')
    inputReason2.send_keys("Diagnose with mahal ko pa siya eh syndrome when lasing.")
    time.sleep(2)
    #reason for home admission
    inputReason3 = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[1]/tbody/tr[2]/td/table/tbody/tr[7]/td/div[2]/div/textarea')
    inputReason3.send_keys("Go Go zaido parating na ang mga zaido, Blue, Red, Green.")
    time.sleep(2)
    #reason for discharge
    inputReason4 = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[2]/tbody/tr[2]/td/table/tbody/tr[2]/td/div/div/div[2]/input')
    inputReason4.send_keys("Bata pa lang ko mam ganito na tinatrabaho ko.")
    time.sleep(2)
    #current physical status
    inputReason5 = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div[2]/div/input')
    inputReason5.send_keys("Hindi pa po siya baliw sabi niya.")
    time.sleep(2)
    #current functional status
    adlCheckbox = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[4]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/div/div[1]/label/input')
    adlCheckbox.click()
    time.sleep(2)
    mobCheckbox = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[4]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td/div/div[1]/label/input')
    mobCheckbox.click()
    time.sleep(2)
    #assistive device
    inputAssist = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[5]/tbody/tr/td[2]/div/input')
    inputAssist.send_keys("Ferrari 458")
    time.sleep(2)
    #summary of care
    inputReason6 = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[7]/tbody/tr[2]/td/div/div/textarea')
    inputReason6.send_keys("Handa akong magtiis kahit na, away away away na ito.")
    time.sleep(2)
    #discipline
    inputReason7 = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[8]/tbody/tr/td[2]/div/input')
    inputReason7.send_keys("Martyr nyebera")
    time.sleep(2)
    #treatment goals
    goals = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[9]/tbody/tr/td[2]/div/label[1]/input')
    goals.click()
    time.sleep(2)
    #physician date
    PhysicianDate = config.driver.find_element_by_xpath('//*[@id="physicianDischargeDate"]')
    PhysicianDate.send_keys("06/05/2021")
    time.sleep(2)
    #Patient date
    PatientDate = config.driver.find_element_by_xpath('//*[@id="patFamCare"]')
    PatientDate.send_keys("06/10/2021")
    time.sleep(2)
    #send via
    sendviaCheckbox = config.driver.find_element_by_xpath('//*[@id="dischargeSummaryForm"]/div/div[1]/fieldset/table/tbody/tr/td/div/div[1]/table[10]/tbody/tr[2]/td[4]/div/label[1]/input')
    sendviaCheckbox.click()
    time.sleep(2)
    #save
    saveDischargesum= config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[2]')
    saveDischargesum.click()
    time.sleep(7)
    
    
    #refresh the page, kasi may times na lumalabas yung DISCARD button parin kahit wala naman ng entry
    #config.driver.refresh();
    #time.sleep(10)     

def DischargeInstructionsInput():
    
    dischargedate = config.driver.find_element_by_xpath('//*[@id="dischargeDate"]')
    dischargedate.send_keys(todaydate)
    time.sleep(2)
    #appointment Dr.
    selectDr = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[2]/td/span[2]/div/div/div/a')
    selectDr.click()
    time.sleep(2)
    chooseDr = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[2]/td/span[2]/div/div/div/div/ul/li[2]')
    chooseDr.click()
    time.sleep(2)
    
    #checkbox
    check1 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[6]/td/div/label[1]/input')
    check1.click()
    time.sleep(2)
    #additional Medication
    input1 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[7]/td/div/div[2]/textarea')
    input1.send_keys("Can somebody to get things back the it used to be.")
    time.sleep(2)
    #diet
    input2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[9]/td/div/div[2]/div/input')
    input2.send_keys("Pasensya ka na sa mga kathang isip kong ito.")
    time.sleep(2)
    #add intructions
    input3 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[11]/td/div/div[2]/textarea')
    input3.send_keys("Magpakulo ng bayabas tsaka ito inumin at kainin.")
    time.sleep(2)
    #wound care instructions
    input4 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[13]/td/div/div[2]/textarea')
    input4.send_keys("Mag gisa ng bawang at sibuyas at isunod luya.")
    time.sleep(2)
    #follow through
    input5 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[15]/td/div/div/input')
    input5.send_keys("I know you're somewhere out there.")
    time.sleep(2)
    #other instructions
    input6 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset/table/tbody/tr/td/table[2]/tbody/tr[17]/td/div/textarea')
    input6.send_keys("Talking to the moon, trynna get to you.")
    time.sleep(2)
    
    save = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[2]')
    save.click()
    time.sleep(7)
     
    
    
def CaseConferenceInput():
    
    caseDate = config.driver.find_element_by_id("order_date")
    caseDate.send_keys(todaydate)
    time.sleep(2)
    #Health Reason
    inputHealthReason = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[1]/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/fieldset/textarea')
    inputHealthReason.send_keys("Siomai rice, Siomai rice, ako ay nagugutom gusto ko siomai rice.")
    time.sleep(2)
    #purpose of care
    inputPurpose = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[1]/table/tbody/tr/td/table[2]/tbody/tr[6]/td/fieldset/textarea')
    inputPurpose.send_keys("Dami pang gustong sabihin, ngunit wag na lang muna.")
    time.sleep(2)
    #assesment of patient
    checkAssesment = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[1]/table/tbody/tr/td/table[2]/tbody/tr[7]/td/div[1]/label/input')
    checkAssesment.click()
    time.sleep(2)
    inputBy = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[1]/table/tbody/tr/td/table[2]/tbody/tr[7]/td/div[2]/input')
    inputBy.send_keys("Pag nilahad ang damdamin, sana di magbago ang pagtingin.")
    time.sleep(2)
    inputBy2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[1]/table/tbody/tr/td/table[2]/tbody/tr[8]/td/fieldset/textarea')
    inputBy2.send_keys("Baka bukas ika'y akin, sana di magbago'ng pagtingin.")
    time.sleep(2)
    #plan of action
    checkPlan = config.driver.find_element_by_name("plan_of_action_check")
    checkPlan.click()
    time.sleep(2)
    inputplan1 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[1]/table/tbody/tr/td/table[2]/tbody/tr[10]/td/table/tbody/tr[2]/td[1]/div/input')
    inputplan1.send_keys("Lorem Ipsum 1.")
    time.sleep(2)
    inputplan2 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[1]/table/tbody/tr/td/table[2]/tbody/tr[10]/td/table/tbody/tr[2]/td[2]/div/input')
    inputplan2.send_keys("Lorem Ipsum 2.")
    time.sleep(2)
    inputplan3 = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[1]/table/tbody/tr/td/table[2]/tbody/tr[10]/td/table/tbody/tr[2]/td[3]/div/input')
    inputplan3.send_keys("Lorem Ipsum 3.")
    time.sleep(2)
    #Case conference
    checkFtF = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[2]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/div[1]/label/input')
    checkFtF.click()
    time.sleep(2)
    checkPhone = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[2]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/div[2]/label/input')
    checkPhone.click()
    time.sleep(2)
    checkOnline = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[2]/table/tbody/tr/td/table/tbody/tr[1]/td[2]/div[3]/label/input')
    checkOnline.click()
    time.sleep(2)
    #Agency Comment
    inputComment = config.driver.find_element_by_xpath('//*[@id="parent"]/div/form/div/div[1]/fieldset[2]/table/tbody/tr/td/table/tbody/tr[3]/td/fieldset/table/tbody/tr/td[3]/div/textarea')
    inputComment.send_keys("Maligo araw-araw, ugalihin gumamit ng sabon.")
    time.sleep(2)
       
   # save the case con
    saveCase2 = config.driver.find_element_by_xpath('//*[@id="tdTitleAction"]/button[2]')
    saveCase2.click()
    time.sleep(2)
    
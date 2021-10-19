from controllers import config, login, function_admission, function_oasis, servers, function_complete_task, function_create_task, patient_dashboard, function_mdo, function_human_resources, function_medical_resources
import random, os, pyautogui, sys, ctypes
import time
import pymsgbox
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
import admission, oasis, create_task, complete_task, create_mdo, complete_woundprocess
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import random
from selenium.webdriver.common.action_chains import ActionChains



# Hospital
servers.liveserver()
config.driver.get("https://app.medisource.com/hospital")
time.sleep(3)

config.driver.find_element_by_xpath('/html/body/section/section/data/div/div[1]/div/div[3]/div[1]/div/div/div/div/input').send_keys('automated')
time.sleep(3)

        
def deleteh():
    config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[2]/td[1]/div[1]/div[2]').click()
    config.driver.find_element_by_xpath('//*[@id="Delete"]/li/button/i[2]').click()
    config.driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()

num = 5
for x in range(num):
        deleteh()






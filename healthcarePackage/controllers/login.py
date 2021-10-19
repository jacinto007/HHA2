from controllers import config
import time

def login(un, up):
    #Get element and applied set variables
    usern = config.driver.find_element_by_id("loginemail").send_keys(un)
    userpass = config.driver.find_element_by_id("loginpassword").send_keys(up)
    time.sleep(1)
    submitbtn = config.driver.find_element_by_xpath("//*[@id='mhLP-ln']/div[2]/form/div[6]/button").click()
    time.sleep(1)
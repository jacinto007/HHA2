from controllers import config, login
import time

# ------------------------------------------------------------------------------------------------
#  QA SERVER
# ------------------------------------------------------------------------------------------------
def qaserver():
    config.driver.maximize_window()
    config.driver.get("https://qado.medisource.com/login")
    
    login.login("superagent@abk", "Tester2021!")
    time.sleep(5)
    
# ------------------------------------------------------------------------------------------------
#  LIVE SERVER
# ------------------------------------------------------------------------------------------------
def liveserver():
    config.driver.maximize_window()
    config.driver.get("https://app.medisource.com/login")
    
    login.login("superagent@geekers", "Tester2021@")
    time.sleep(5)
    
def webpagetest():
    # Use Navigation Timing  API to calculate the timings that matter the most
    # https://www.lambdatest.com/blog/how-to-measure-page-load-times-with-selenium/
    navigationStart = config.driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = config.driver.execute_script("return window.performance.timing.responseStart")
    domComplete = config.driver.execute_script("return window.performance.timing.domComplete")
    
    # Calculate the performance 
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart
     
    print("Back End: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)    

def searchpatientrecord(searchpatient):
    time.sleep(5)
    print(searchpatient)
    time.sleep(2)
    searchbar = config.driver.find_element_by_xpath('//*[@id="searchbar__wrapper"]/div/input').send_keys(searchpatient)
    time.sleep(5)
    searchresult = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[2]').click()
    
    
def logout(): 
    # Logout
    time.sleep(3)
    profileuser = config.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div/ul/li[6]/a').click()
    signout = config.driver.find_element_by_xpath('//*[@id="header"]/div/div/div/div/ul/li[6]/div/div[2]/div/button[2]').click()
     
        
    
    
    
    
    
    
    
    
    
    

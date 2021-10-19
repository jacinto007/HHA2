from controllers import config, patient_dashboard
import time, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from _ast import Div

# ------------------------------------------------------------------------------------------------
#  TIME IN AND TIME OUT
# ------------------------------------------------------------------------------------------------
def oasissoc_timeinout(ti, to):
    timein = config.driver.find_element_by_name("timeIn").send_keys(ti)
    timeout = config.driver.find_element_by_name("timeOut").send_keys(to)

# ------------------------------------------------------------------------------------------------
#  DEMOGRAPHICS
# ------------------------------------------------------------------------------------------------
def oasissoc_demographics(todaynow, episodetiming, ssn):
    time.sleep(3)
    m0063 = config.driver.find_element_by_name('M0063_MEDICARE_NUM').send_keys(ssn)
    m0090 = config.driver.find_element_by_id("m0090_info_completed_dt").send_keys(todaynow)
    time.sleep(3)
    m0102_checkbox = config.driver.find_element_by_name("M0102_PHYSN_ORDRD_SOCROC_DT_NA").click()
    time.sleep(3)
    m0104 = config.driver.find_element_by_id("m0104_physn_rfrl_dt").send_keys(todaynow)
    
    #For Episode Timing
    etiming = ""
    
    if episodetiming == "Early":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[1]/div[1]/label/input")
    elif episodetiming == "Later":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[1]/div[2]/label/input")
    elif episodetiming == "Unknown":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[2]/div[1]/label/input")
    elif episodetiming == "NA":
        etiming = config.driver.find_element_by_xpath("//*[@id='oasisForm']/fieldset/table[1]/tbody/tr[28]/td[2]/table/tbody/tr/td/div/div/div[2]/div[2]/label/input")
    
    time.sleep(3)
    etiming.click()
    
    m0140_asian = config.driver.find_element_by_xpath("//*[@id='M0140_ETHNIC_ASIAN']/input").click()
    m0150_medicare_trad = config.driver.find_element_by_xpath("//*[@id='M0150_CPAY_MCARE_FFS']/input").click()
    m1000_skilled_nursing_facility = config.driver.find_element_by_name("M1000_DC_SNF_14_DA").click()
    m1005_unknown = config.driver.find_element_by_name("M1005_INP_DSCHG_UNKNOWN").click()
    
    time.sleep(5)

# ------------------------------------------------------------------------------------------------
#  DIAGNOSIS
# ------------------------------------------------------------------------------------------------
def oasissoc_diagnosesmedhis(
        pdx,
        sdx1,
        sdx2,
        sdx3,
        sdx4,
        sdx5,
        m1028_items,
        m0133_items,
        mheight,
        mweight
        ):
    
    time.sleep(5)
    
    #Primary Diagnosis
    pd = config.driver.find_element_by_xpath("//*[@id='tooltip_a']/table/tbody/tr/td[2]/icd-opt/div/div[1]/input")
    pd.send_keys(pdx)
    time.sleep(2)
    config.driver.switch_to_active_element()
    pd.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    pd.send_keys(Keys.ENTER)
    pdr = config.driver.find_element_by_xpath("//*[@id='icdSeverityIdCode$index']/label[4]/input").click()
    
    time.sleep(2)
    
    #Secondary Diagnosis
    #1st Secondary Diagnosis
    sd1 = config.driver.find_element_by_xpath("//*[@id='tooltip_b']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd1.send_keys(sdx1)
    time.sleep(2)
    config.driver.switch_to_active_element()
    sd1.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    sd1.send_keys(Keys.ENTER)
    sd1r = config.driver.find_element_by_xpath("//*[@id='tooltip_b']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3
      
    time.sleep(2)
    
    #2nd Secondary Diagnosis
    sd2 = config.driver.find_element_by_xpath("//*[@id='tooltip_c']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd2.send_keys(sdx2)
    time.sleep(2)
    config.driver.switch_to_active_element()
    sd2.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    sd2.send_keys(Keys.ENTER)
    sd2r = config.driver.find_element_by_xpath("//*[@id='tooltip_c']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3
  
    time.sleep(2)
    
    #3rd Secondary Diagnosis
    sd3 = config.driver.find_element_by_xpath("//*[@id='tooltip_d']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd3.send_keys(sdx3)
    time.sleep(2)
    config.driver.switch_to_active_element()
    sd3.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    sd3.send_keys(Keys.ENTER)
    sd3r = config.driver.find_element_by_xpath("//*[@id='tooltip_d']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3
  
    time.sleep(2)
    
    #4th Secondary Diagnosis
    sd4 = config.driver.find_element_by_xpath("//*[@id='tooltip_e']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd4.send_keys(sdx4)
    time.sleep(2)
    config.driver.switch_to_active_element()
    sd4.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    sd4.send_keys(Keys.ENTER)
    sd4r = config.driver.find_element_by_xpath("//*[@id='tooltip_e']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3
  
    time.sleep(2)
    
    #5th Secondary Diagnosis
    sd5 = config.driver.find_element_by_xpath("//*[@id='tooltip_f']/table/tbody/tr[1]/td[2]/icd-opt/div/div[1]/input")
    sd5.send_keys(sdx5)
    time.sleep(2)
    config.driver.switch_to_active_element()
    sd5.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    sd5.send_keys(Keys.ENTER)
    sd5r = config.driver.find_element_by_xpath("//*[@id='tooltip_f']/table/tbody/tr/td[3]/fieldset/div/label[3]/input").click() #Value is 3
  
    time.sleep(2)
    
    #m0128_items
    m1028_items_selected = ""
    for x in m1028_items:
        print(x)
        m1028_items_selected = config.driver.find_element_by_xpath("//*[@class='m-0']/label["+str(x)+"]/input")
        m1028_items_selected.click()
    time.sleep(2)

    m1030 = config.driver.find_element_by_xpath("//*[@id='M1030_THH_NONE_ABOVE']/input").click() #Value is None of the above
    
    #m0133_items
    m0133_items_selected = ""
    for x in m0133_items:
        print(x)
        m0133_items_selected = config.driver.find_element_by_xpath("//*[@id='M1033_HOSP_RISK_HSTRY_FALLS']/label["+ str(x) +"]/input")
        m0133_items_selected.click()
    time.sleep(2)
    m1060_height = config.driver.find_element_by_name("M1060_HEIGHT_A").send_keys(mheight)
    m1060_weight = config.driver.find_element_by_name("M1060_WEIGHT_B").send_keys(mweight)
    time.sleep(2)
    
    #Past Medical History   Select all No History
    pmh_s_nh = config.driver.find_element_by_name("SOOMEDICAL0135").click()
    pmh_i_nh = config.driver.find_element_by_name("SOOMEDICAL0121").click()
    pmh_e_nh = config.driver.find_element_by_name("SOOMEDICAL0137").click()
    pmh_r_nh = config.driver.find_element_by_name("SOOMEDICAL0138").click()
    pmh_c_nh = config.driver.find_element_by_name("SOOMEDICAL0139").click()
    pmh_g_nh = config.driver.find_element_by_name("SOOMEDICAL0141").click()
    pmh_n_nh = config.driver.find_element_by_name("SOOMEDICAL0142").click()
    pmh_m_nh = config.driver.find_element_by_name("SOOMEDICAL0143").click()
    pmh_cl_nh = config.driver.find_element_by_name("SOOMEDICAL0145").click()
    pmh_oh_nh = config.driver.find_element_by_name("SOOMEDICAL0146").click()
    pmh_s_nh = config.driver.find_element_by_name("SOOMEDICAL0147").click()

# ------------------------------------------------------------------------------------------------
#  VITAL SIGNS / SENSORY
# ------------------------------------------------------------------------------------------------
def oasissoc_vssensory(
        vstemp,
        vspulse,
        vsres,
        vslasys,
        vsladyl,
        vso2room,
        vso2o2,
        vso2lpm,
        vsbs
        ):
    time.sleep(5)
    
    vs_temp = config.driver.find_element_by_name("SOOVS0001").send_keys(vstemp)
    vs_temp_scan = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[2]/td/table/tbody/tr/td[3]/div/label[2]/input").click() #scan
    
    vs_pulse = config.driver.find_element_by_name("SOOVS0003").send_keys(vspulse)
    vs_pulse_radial = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[3]/td/table/tbody/tr/td[3]/div/label[1]/input").click()
    vs_res = config.driver.find_element_by_name("SOOVS0006").send_keys(vsres)
    
    vs_lefta_sys = config.driver.find_element_by_name("SOOVS0009").send_keys(vslasys)
    vs_lefta_dyl = config.driver.find_element_by_name("SOOVS0059").send_keys(vsladyl)
    vs_lefta_sitting = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[5]/td/table/tbody/tr/td[3]/div/label[1]/input").click()
    
    vs_o2room = config.driver.find_element_by_name("SOOVS0021").send_keys(vso2room)
    vs_o2o2 = config.driver.find_element_by_name("SOOVS0022").send_keys(vso2o2)
    vs_o2lpm = config.driver.find_element_by_name("SOOVS0023").send_keys(vso2lpm)
    
    vs_bs = config.driver.find_element_by_name("SOOVS0024").send_keys(vsbs)
    vs_bs_rbs = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[11]/td/table/tbody/tr/td[3]/div/label[2]/input").click()
    
    vs_weight_actual = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[12]/td/table/tbody/tr/td[3]/div/label[2]/input").click()
    vs_height_actual = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/div[1]/table[1]/tbody/tr[13]/td/table/tbody/tr/td[3]/div/label[1]/input").click()
    
    m1242_nopain = config.driver.find_element_by_xpath("//*[@id='M1242_PAIN_FREQ_ACTVTY_MVMT']/div/div[1]/label/input").click()
    m1200_normalvision = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/div/label/input").click()
    
    #All sensory status will be WNL
    ss_eyes_wnl = config.driver.find_element_by_xpath("//*[@id='sensoryForm']/div/div/fieldset/table[4]/tbody/tr[2]/td/table/tbody/tr/td[2]/label/input").click()
    ss_ear_wnl = config.driver.find_element_by_name("SOOSENSORY0039").click()
    ss_mouth_wnl = config.driver.find_element_by_name("SOOSENSORY0059").click() 
    ss_nose_wnl = config.driver.find_element_by_name("SOOSENSORY0055").click() 
    ss_throat_wnl = config.driver.find_element_by_name("SOOSENSORY0063").click() 
    ss_speech_wnl = config.driver.find_element_by_name("SOOSENSORY0067").click() 
    ss_touch_wnl = config.driver.find_element_by_name("SOOSENSORY0070").click() 

# ------------------------------------------------------------------------------------------------
#  INTEGUMENTARY / ENDOCRINE
# ------------------------------------------------------------------------------------------------
def oasissoc_integendo():
    time.sleep(5)
    is_wnl = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input").click()
    bsppsr_noimpairement = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_rarelymoist = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[3]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_walksf = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[4]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_nolimit = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[5]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_excellent = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[6]/td[1]/table/tbody/tr[5]/td[1]/label/input").click()
    bsppsr_noprob = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[2]/tbody/tr[7]/td[1]/table/tbody/tr[4]/td[1]/label/input").click()
    
    m1306_0 = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/label[1]/input").click()
    m1322_0 = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[5]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div/div[1]/label/input").click()
    m1324_na = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[6]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div/div[5]/label/input").click()
    m1330_0 = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[7]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input").click()
    m1340_0 = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[1]/table[10]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input").click()
    
    endosys_wnl = config.driver.find_element_by_xpath("//*[@id='integForm']/fieldset/div[3]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input").click()

# ------------------------------------------------------------------------------------------------
#  CARDIOPULMONARY
# ------------------------------------------------------------------------------------------------
def oasissoc_cardio():
    time.sleep(5)
    m1400_0 = config.driver.find_element_by_xpath('//*[@id="M1400_WHEN_DYSPNEIC"]/div[1]/label/input').click()
    resps_wnl = config.driver.find_element_by_xpath('//*[@id="cardioForm"]/div/fieldset/div[1]/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    cardio_wnl = config.driver.find_element_by_xpath('//*[@id="cardioForm"]/div/fieldset/div[1]/table[10]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    
# ------------------------------------------------------------------------------------------------
#  NUTRITION / ELIMINATION
# ------------------------------------------------------------------------------------------------
def oasissoc_nutrielim():
    time.sleep(5)
    uppergistat_wnl = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    genitostat_wnl = config.driver.find_element_by_xpath('//*[@id="SOOELIMINATION0011"]/td/table/tbody/tr/td[2]/div/label/input').click()
    abnelim_no = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[10]/tbody/tr[5]/td[2]/label[1]/input').click()
    spx_no = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[10]/tbody/tr[7]/td[2]/label[1]/input').click()
    m1600_0 = config.driver.find_element_by_xpath('//*[@id="M1600_UTI"]/div[1]/label/input').click()
    m1610_0 = config.driver.find_element_by_xpath('//*[@id="M1610_UR_INCONT"]/div[1]/label/input').click()
    time.sleep(5)
    lowergistat_wnl = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[21]/tbody/tr[1]/td[2]/label[1]/input').click()
    m1620_na = config.driver.find_element_by_xpath('//*[@id="code"]').send_keys('NA')
    m1630_0 = config.driver.find_element_by_xpath('//*[@id="elimForm"]/fieldset/div[1]/table[24]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div/label[1]/input').click()

# ------------------------------------------------------------------------------------------------
#  NEUROLOGIC / BEHAVIORAL
# ------------------------------------------------------------------------------------------------
def oasissoc_neurobehav():
    time.sleep(5)
    neurostat_wnl = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    m1700_0 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[2]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1710_0 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr[1]/td/div/label/input').click()
    m1720_0 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[4]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1730_0 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[5]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1740_7 = config.driver.find_element_by_id('M1740_BD_NONE').click()
    m1745_1 = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[7]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[2]/label/input').click()
    thought_wnl = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[9]/tbody/tr[1]/td/table/tbody/tr/td[2]/div/label/input').click()
    languageb_no = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[10]/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/label/input').click()
    learningb_no = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[10]/tbody/tr[4]/td[2]/table/tbody/tr/td/label/input').click()
    soabuse = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[10]/tbody/tr[6]/td[2]/table/tbody/tr/td/label/input').click()
    spiritual_no = config.driver.find_element_by_xpath('//*[@id="neuroForm"]/div/fieldset/div[1]/table[10]/tbody/tr[8]/td[2]/table/tbody/tr/td/label/input').click()
    
# ------------------------------------------------------------------------------------------------
#  ADL / IADL / MUSCULOSKELETAL
# ------------------------------------------------------------------------------------------------
def oasissoc_adlmusco():
    
    gg0100_3 = "3"
    gg_6 = "6"
    
    time.sleep(5)
    musstat_wnl = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td/div[2]/label/input').click()
    m1800_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[6]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1810_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[7]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1820_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[8]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1830_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[9]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1840_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[10]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1845_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[11]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1850_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[12]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1860_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[13]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1870_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[14]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m1910_0 = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[15]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
 
    time.sleep(2)
        
    scrolldown = config.driver.execute_script("window.scrollTo(0,3500)")
        
    GG0100A = config.driver.find_element_by_xpath('//*[@id="GG0100A_chosen"]').click()
    GG0100A3 = config.driver.find_element_by_xpath('//*[@id="GG0100A_chosen"]/div/ul/li[1]').click()
    GG0100B = config.driver.find_element_by_xpath('//*[@id="GG0100B_chosen"]').click()
    GG0100B3 = config.driver.find_element_by_xpath('//*[@id="GG0100B_chosen"]/div/ul/li[1]').click()
    GG0100C = config.driver.find_element_by_xpath('//*[@id="GG0100C_chosen"]').click()
    GG0100C3 = config.driver.find_element_by_xpath('//*[@id="GG0100C_chosen"]/div/ul/li[1]').click()
    GG0100D = config.driver.find_element_by_xpath('//*[@id="GG0100D_chosen"]').click()
    GG0100D3 = config.driver.find_element_by_xpath('//*[@id="GG0100D_chosen"]/div/ul/li[1]').click()
    gg0110_z = config.driver.find_element_by_xpath('//*[@id="adlForm"]/fieldset/div[1]/table[18]/tbody/tr[2]/td/table/tbody/tr[4]/td[3]/label/input').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,4000)")
    
    GG0130A1 = config.driver.find_element_by_xpath('//*[@id="GG0130A1"]/div/mhc-gg0130').click()
    GG0130A16 = config.driver.find_element_by_xpath('//*[@id="GG0130A1"]//div/ul/li[1]').click()
    GG0130A2 = config.driver.find_element_by_xpath('//*[@id="GG0130A2"]/div/mhc-gg0130').click()
    GG0130A26 = config.driver.find_element_by_xpath('//*[@id="GG0130A2"]//div/ul/li[1]').click()
    
    GG0130B1 = config.driver.find_element_by_xpath('//*[@id="GG0130B1"]/div/mhc-gg0130').click()
    GG0130B16 = config.driver.find_element_by_xpath('//*[@id="GG0130B1"]//div/ul/li[3]').click()
    GG0130B2 = config.driver.find_element_by_xpath('//*[@id="GG0130B2"]/div/mhc-gg0130').click()
    GG0130B26 = config.driver.find_element_by_xpath('//*[@id="GG0130B2"]//div/ul/li[3]').click()
    
    GG0130C1 = config.driver.find_element_by_xpath('//*[@id="GG0130C1"]/div/mhc-gg0130').click()
    GG0130C16 = config.driver.find_element_by_xpath('//*[@id="GG0130C1"]//div/ul/li[1]').click()
    GG0130C2 = config.driver.find_element_by_xpath('//*[@id="GG0130C2"]/div/mhc-gg0130').click()
    GG0130C26 = config.driver.find_element_by_xpath('//*[@id="GG0130C2"]//div/ul/li[1]').click()
    
    GG0130E1 = config.driver.find_element_by_xpath('//*[@id="GG0130E1"]/div/mhc-gg0130').click()
    GG0130E16 = config.driver.find_element_by_xpath('//*[@id="GG0130E1"]//div/ul/li[1]').click()
    GG0130E2 = config.driver.find_element_by_xpath('//*[@id="GG0130E2"]/div/mhc-gg0130').click()
    GG0130E26 = config.driver.find_element_by_xpath('//*[@id="GG0130E2"]//div/ul/li[1]').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,4300)")
    
    GG0130F1 = config.driver.find_element_by_xpath('//*[@id="GG0130F1"]/div/mhc-gg0130').click()
    GG0130F16 = config.driver.find_element_by_xpath('//*[@id="GG0130F1"]//div/ul/li[1]').click()
    GG0130F2 = config.driver.find_element_by_xpath('//*[@id="GG0130F2"]/div/mhc-gg0130').click()
    GG0130F26 = config.driver.find_element_by_xpath('//*[@id="GG0130F2"]//div/ul/li[1]').click()
    
    GG0130G1 = config.driver.find_element_by_xpath('//*[@id="GG0130G1"]/div/mhc-gg0130').click()
    GG0130G16 = config.driver.find_element_by_xpath('//*[@id="GG0130G1"]//div/ul/li[1]').click()
    GG0130G2 = config.driver.find_element_by_xpath('//*[@id="GG0130G2"]/div/mhc-gg0130').click()
    GG0130G26 = config.driver.find_element_by_xpath('//*[@id="GG0130G2"]//div/ul/li[1]').click()
    
    GG0130H1 = config.driver.find_element_by_xpath('//*[@id="GG0130H1"]/div/mhc-gg0130').click()
    GG0130H16 = config.driver.find_element_by_xpath('//*[@id="GG0130H1"]//div/ul/li[1]').click()
    GG0130H2 = config.driver.find_element_by_xpath('//*[@id="GG0130H2"]/div/mhc-gg0130').click()
    GG0130H26 = config.driver.find_element_by_xpath('//*[@id="GG0130H2"]//div/ul/li[1]').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,5200)")
    
    GG0170A1 = config.driver.find_element_by_xpath('//*[@id="GG0170A1"]').click()
    GG0170A16 = config.driver.find_element_by_xpath('//*[@id="GG0170A1"]//div/ul/li[1]').click()
    GG0170A2 = config.driver.find_element_by_xpath('//*[@id="GG0170A2"]').click()
    GG0170A26 = config.driver.find_element_by_xpath('//*[@id="GG0170A2"]//div/ul/li[1]').click()
    
    GG0170B1 = config.driver.find_element_by_xpath('//*[@id="GG0170B1"]').click()
    GG0170B16 = config.driver.find_element_by_xpath('//*[@id="GG0170B1"]//div/ul/li[1]').click()
    GG0170B2 = config.driver.find_element_by_xpath('//*[@id="GG0170B2"]').click()
    GG0170B26 = config.driver.find_element_by_xpath('//*[@id="GG0170B2"]//div/ul/li[1]').click()
    
    GG0170C1 = config.driver.find_element_by_xpath('//*[@id="GG0170C_MOBILITY_SOCROC_PERF"]/div/mhc-gg0170c/div').click()
    GG0170C16 = config.driver.find_element_by_xpath('//*[@id="GG0170C_MOBILITY_SOCROC_PERF"]//div/ul/li[1]').click()
    GG0170C2 = config.driver.find_element_by_xpath('//*[@id="GG0170C_MOBILITY_DSCHG_GOAL"]/div/mhc-gg0170c/div').click()
    GG0170C26 = config.driver.find_element_by_xpath('//*[@id="GG0170C_MOBILITY_DSCHG_GOAL"]//div/ul/li[1]').click()
    
    GG0170D1 = config.driver.find_element_by_xpath('//*[@id="GG0170D1"]/div/mhc-gg0170c/div').click()
    GG0170D16 = config.driver.find_element_by_xpath('//*[@id="GG0170D1"]//div/ul/li[1]').click()
    GG0170D2 = config.driver.find_element_by_xpath('//*[@id="GG0170D2"]/div/mhc-gg0170c/div').click()
    GG0170D26 = config.driver.find_element_by_xpath('//*[@id="GG0170D2"]//div/ul/li[1]').click()
    
    GG0170E1 = config.driver.find_element_by_xpath('//*[@id="GG0170E1"]').click()
    GG0170E16 = config.driver.find_element_by_xpath('//*[@id="GG0170E1"]//div/ul/li[1]').click()
    GG0170E2 = config.driver.find_element_by_xpath('//*[@id="GG0170E2"]').click()
    GG0170E26 = config.driver.find_element_by_xpath('//*[@id="GG0170E2"]//div/ul/li[1]').click()
    
    GG0170F1 = config.driver.find_element_by_xpath('//*[@id="GG0170F1"]').click()
    GG0170F16 = config.driver.find_element_by_xpath('//*[@id="GG0170F1"]//div/ul/li[1]').click()
    GG0170F2 = config.driver.find_element_by_xpath('//*[@id="GG0170F2"]').click()
    GG0170F26 = config.driver.find_element_by_xpath('//*[@id="GG0170F2"]//div/ul/li[1]').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,5500)")
    
    GG0170G1 = config.driver.find_element_by_xpath('//*[@id="GG0170G1"]').click()
    GG0170G16 = config.driver.find_element_by_xpath('//*[@id="GG0170G1"]//div/ul/li[1]').click()
    GG0170G2 = config.driver.find_element_by_xpath('//*[@id="GG0170G2"]').click()
    GG0170G26 = config.driver.find_element_by_xpath('//*[@id="GG0170G2"]//div/ul/li[1]').click()
    
    GG0170I1 = config.driver.find_element_by_xpath('//*[@id="GG0170I1"]').click()
    GG0170I16 = config.driver.find_element_by_xpath('//*[@id="GG0170I1"]//div/ul/li[1]').click()
    GG0170I2 = config.driver.find_element_by_xpath('//*[@id="GG0170I2"]').click()
    GG0170I26 = config.driver.find_element_by_xpath('//*[@id="GG0170I2"]//div/ul/li[1]').click()
    
    GG0170J1 = config.driver.find_element_by_xpath('//*[@id="GG0170J1"]').click()
    GG0170J16 = config.driver.find_element_by_xpath('//*[@id="GG0170J1"]//div/ul/li[1]').click()
    GG0170J2 = config.driver.find_element_by_xpath('//*[@id="GG0170J2"]').click()
    GG0170J26 = config.driver.find_element_by_xpath('//*[@id="GG0170J2"]//div/ul/li[1]').click()
    
    GG0170K1 = config.driver.find_element_by_xpath('//*[@id="GG0170K1"]').click()
    GG0170K16 = config.driver.find_element_by_xpath('//*[@id="GG0170K1"]//div/ul/li[1]').click()
    GG0170K2 = config.driver.find_element_by_xpath('//*[@id="GG0170K2"]').click()
    GG0170K26 = config.driver.find_element_by_xpath('//*[@id="GG0170K2"]//div/ul/li[1]').click()
    
    GG0170L1 = config.driver.find_element_by_xpath('//*[@id="GG0170L1"]').click()
    GG0170L16 = config.driver.find_element_by_xpath('//*[@id="GG0170L1"]//div/ul/li[1]').click()
    GG0170L2 = config.driver.find_element_by_xpath('//*[@id="GG0170L2"]').click()
    GG0170L26 = config.driver.find_element_by_xpath('//*[@id="GG0170L2"]//div/ul/li[1]').click()
    
    scrolldown = config.driver.execute_script("window.scrollTo(0,6000)")
    
    GG0170M1 = config.driver.find_element_by_xpath('//*[@id="GG0170M1"]').click()
    GG0170M16 = config.driver.find_element_by_xpath('//*[@id="GG0170M1"]//div/ul/li[1]').click()
    GG0170M2 = config.driver.find_element_by_xpath('//*[@id="GG0170M2"]').click()
    GG0170M26 = config.driver.find_element_by_xpath('//*[@id="GG0170M2"]//div/ul/li[1]').click()
    
    GG0170N1 = config.driver.find_element_by_xpath('//*[@id="GG0170N1"]').click()
    GG0170N16 = config.driver.find_element_by_xpath('//*[@id="GG0170N1"]//div/ul/li[1]').click()
    GG0170N2 = config.driver.find_element_by_xpath('//*[@id="GG0170N2"]').click()
    GG0170N26 = config.driver.find_element_by_xpath('//*[@id="GG0170N2"]//div/ul/li[1]').click()
    
    GG0170O1 = config.driver.find_element_by_xpath('//*[@id="GG0170O1"]').click()
    GG0170O16 = config.driver.find_element_by_xpath('//*[@id="GG0170O1"]//div/ul/li[1]').click()
    GG0170O2 = config.driver.find_element_by_xpath('//*[@id="GG0170O2"]').click()
    GG0170O26 = config.driver.find_element_by_xpath('//*[@id="GG0170O2"]//div/ul/li[1]').click()
    
    GG0170P1 = config.driver.find_element_by_xpath('//*[@id="GG0170P1"]').click()
    GG0170P16 = config.driver.find_element_by_xpath('//*[@id="GG0170P1"]//div/ul/li[1]').click()
    GG0170P2 = config.driver.find_element_by_xpath('//*[@id="GG0170P2"]').click()
    GG0170P26 = config.driver.find_element_by_xpath('//*[@id="GG0170P2"]//div/ul/li[1]').click()
    
    GG0170Q1 = config.driver.find_element_by_xpath('//*[@id="GG0170Q1_chosen"]').click()
    GG0170Q11 = config.driver.find_element_by_xpath('//*[@id="GG0170Q1_chosen"]/div/ul/li[1]').click()


    scrolldown = config.driver.execute_script("window.scrollTo(0,6500)")
    
    
   

# ------------------------------------------------------------------------------------------------
#  MEDICATION
# ------------------------------------------------------------------------------------------------
def oasissoc_medication():
    time.sleep(5)
    highrisk_none = config.driver.find_element_by_xpath('//*[@id="medicationForm"]/fieldset/div[1]/table[1]/tbody/tr[1]/td/label/input').click()
    m2001_0 = config.driver.find_element_by_xpath('//*[@id="medicationForm"]/fieldset/div[1]/table[3]/tbody/tr[2]/td[2]/table[2]/tbody/tr/td/div[1]/label/input').click()
    m2010_na = config.driver.find_element_by_xpath('//*[@id="medicationForm"]/fieldset/div[1]/table[5]/tbody/tr[2]/td[2]/fieldset/table/tbody/tr/td/div[3]/label/input').click()
    m2020_1 = config.driver.find_element_by_xpath('//*[@id="medicationForm"]/fieldset/div[1]/table[6]/tbody/tr[2]/td[2]/fieldset/table/tbody/tr/td/div[2]/label/input').click()
    m2030_0 = config.driver.find_element_by_xpath('//*[@id="medicationForm"]/fieldset/div[1]/table[7]/tbody/tr[2]/td[2]/fieldset/table/tbody/tr/td/div[1]/label/input').click()
    
# ------------------------------------------------------------------------------------------------
#  CARE MANAGEMENT
# ------------------------------------------------------------------------------------------------
def oasissoc_careman():
    time.sleep(5)
    m1100_7 = config.driver.find_element_by_xpath('//*[@id="careForm"]/fieldset/div[1]/table[2]/tbody/tr[2]/td/table/tbody/tr[4]/td[4]/div/label/input').click()
    m2102_1 = config.driver.find_element_by_xpath('//*[@id="M2102_CARE_TYPE_SRC_SPRVSN"]').click()
    m2200_000 = config.driver.find_element_by_xpath('//*[@id="careForm"]/fieldset/div[1]/table[4]/tbody/tr[2]/td[2]/table/tbody/tr/td/label/input').send_keys("000")
    dme_none = config.driver.find_element_by_xpath('//*[@id="tooltip_wr8"]/div[2]/div/label/input').click()
   
  
    
  
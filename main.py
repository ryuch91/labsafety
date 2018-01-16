#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configure import ID, PW

import subprocess

# Change this path to your own IE driver path
DRIVER_PATH = 'C:\Users\iDB_ADB\Documents\GitHub\labsafety\drivers\IEDriverServer.exe'
MAIN_ADDRESS = 'http://safety.kaist.ac.kr/Default.aspx'

browser = webdriver.Ie(DRIVER_PATH)
browser.implicitly_wait(5)

browser.get(MAIN_ADDRESS)
# assert "안전팀" in (driver.title).decode('cp949').encode('utf-8')

# Click to enter the login page
LoginXpath='//img[contains(@src, "/images/LoginMsg.gif")]'
elem = browser.find_element_by_xpath(LoginXpath)
elem.click()

# Enter ID and PW to login
IDXpath='//input[contains(@name,"id")]'
PWXpath='//input[contains(@name,"password")]'
LoginBtnXpath='//input[contains(@src, "/iamps/images/iampsv2/p8_19.gif")]'
elem = browser.find_element_by_xpath(IDXpath)
elem.send_keys(ID)
elem= browser.find_element_by_xpath(PWXpath)
elem.send_keys(PW)
elem = browser.find_element_by_xpath(LoginBtnXpath)
elem.click()

# Enter lab safety system
SafetySystemXpath='//img[contains(@src,"/images/main/QuickMenu_01.png")]'
elem = browser.find_element_by_xpath(SafetySystemXpath)
elem.click()

SystemLinkXpath = '//img[contains(@src,"/images/Inspection/LabSafetyMgrSystem_Shortcuts.gif")]'
elem = browser.find_element_by_xpath(SystemLinkXpath)
elem.click()

browser.implicitly_wait(5)

# Run Sikuli script to click MS Silverlight app
def runSikuliScript(path):
    filepath = path
    p = subprocess.Popen(filepath, shell=True, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print "Done running Sikuli"

p = "C:\Users\iDB_ADB\Documents\GitHub\labsafety\sikuli.bat"
runSikuliScript(p)
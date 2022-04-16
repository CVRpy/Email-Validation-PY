
from ast import Global
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import csv
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import chromedriver_autoinstaller
from os import system
import datetime
import time
import os

#IF YOU HAVE VPN TO CHANGE IP ADDRESS EVERY 5 MINTUES 
def vpn_changer():
    if datetime.datetime.now().minute % 5 == 0:
        print(
            f"###########  {datetime.datetime.now()} is to change VPN IP Adress ##############")
        print("#" * 50)

        try:
            print("++++++++++++++++ Trying to Kill VPN APP +++++++++++++++++++++")
            system("TASKKILL /F /IM Freedome.exe")
        except:
            pass
        time.sleep(5)

        os.startfile(
            r"C:\Program Files (x86)\F-Secure\Freedome\Freedome\1\Freedome.exe")
        print("#################  VPN Reloaded   #############################")
        time.sleep(10)
    else:
        print("#####++++ VPN NOT CHANGED YET ++++#####")
        pass

#ADD YOUR FILE LOCATION TO READ IT
with open('EMAILADDRESS.csv', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)
email_list = []
for email in data:
    email_list.append(*email)


email_input = ""
ls = []


def validate(email_input):
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.ChromeOptions(executable_path='/webdriver/chromedriver.exe')
    # change ip if required every 5 mins
    vpn_changer()
    # change user agent

    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    print(options)
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()

    # Navigate to url
    driver.get("https://validateemailaddress.org")
    # Store 'SearchInput' element
    # accept terms
    try:
        ses = driver.find_element_by_id("accept")
        ses.click()
        time.sleep(5)
    except:
        pass

    SearchInput = driver.find_element(By.CSS_SELECTOR, "input")
    # print(len(SearchInput))
    #email_input = ""
    SearchInput.send_keys(f"{email_input}")
    time.sleep(5)
    SearchInput.send_keys(u'\ue007')

    time.sleep(5)
    global result1
    global result2
    result1 = f"{email_input} " + "seems not to be valid"
    # print(result1)

    try:
        result2 = driver.find_element(By.CLASS_NAME, 'success').text
        print(result2)
        try:
            result2 = driver.find_element(By.CLASS_NAME, 'failure').text
            print(result2)
        except:
            print("Found Success element, Failed to find failure element")
    except:
        print("Found Failure element, Failed to find success element")
    #assert result2.text == 'seems not to be valid'

    global valid

    def valid():
        if result1 == result2:
            return False
        else:
            return True
    valid()
    print("#" * 50)
    print("#" * 50)
    print("#" * 50)
    print(f"Email {email_input} is: ", valid())
    ls = []
    if valid() == True:
        ls.append(f"{email_input.strip()}")
        print(
            "############## Email has been added successfully ############################\n")
        with open("/Users/Matrix10/Downloads/Projects/1files/valid_emails.csv", "a", newline='', encoding='utf-8-sig') as file:
            wr = csv.writer(file)
    # delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL
    #wr.writerow(["EMAIL GMAIL", "PASSWORD"])
            wr.writerow(ls)

    # Clears the entered text
    # SearchInput.clear()
    driver.quit()


for i in email_list[1148:]:
    email_input = i
    print("#" * 50)
    print("#" * 50)
    print("#" * 50)
    print(f"checking: {i}")
    print("#" * 50)
    print("#" * 50)
    print("#" * 50)
    validate(i)

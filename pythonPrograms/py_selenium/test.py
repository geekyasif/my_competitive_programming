from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://ilizone2020.iul.ac.in/2020/login/index.php")
# #

with open('username','r') as f:
    set_username = f.read()

with open('password', 'r') as f:
    set_password = f.read()

# getting the id of the login input and setting the username
username = driver.find_element_by_id("username")
username.send_keys(set_username)

# getting the id of the password field and setting the password
password = driver.find_element_by_id("password")
password.send_keys(set_password)

# getting the login button and setting click event to login
login = driver.find_element_by_id("loginbtn")
login.click()

print("login sucessfully")

time.sleep(5)

# driver.find_element_by_xpath("//button[@aria-expanded='false']").click()
#subject microprocessor
driver.find_element_by_xpath("//*[@id='page-container-0']/div/ul/li[1]/div/div[1]/div/a").click()
time.sleep(2)

# attendance link by subject
driver.find_element_by_xpath("//*[@id='module-312271']/div/div/div[2]/div/a").click()

time.sleep(2)
#submit attendace link
driver.find_element_by_xpath("//*[@id='region-main']/div[1]/table[1]/tbody/tr[9]/td[3]/a").click()


# present radio button
driver.find_element_by_xpath("//*[@id='id_status_32450']").click()

driver.find_element_by_id("id_submitbutton").click()





# driver.find_element_by_link_text("JAVA Programming").click()

# l = driver.find_element_by_link_text("Log out")
# l.click()

# try:
#     coursename = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "Data Compression")))
#     coursename.click()
#
# except:
#     driver.quit()





print("successfully ended")
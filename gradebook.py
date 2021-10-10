from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from utils import exportToExcel
import pandas as pd
import os
import time

load_dotenv()

URL = ""

# Opciones webdriver
# --------------------------------------------------------------------------------------------------------------------------------#
options = Options()
options.add_argument("log-level=3")
options.add_argument('window-size=1920x1080')
driver = Chrome(executable_path=os.getenv("DRIVER_PATH"), options=options)
# --------------------------------------------------------------------------------------------------------------------------------#

wait = WebDriverWait(driver, 5)
driver.get(URL)

time.sleep(1)

# Enfocar el widget de login
driver.switch_to.frame("netlify-identity-widget")

# Hacer click en sign in con google
driver.find_element_by_class_name("providerGoogle").click()

# Correo
driver.find_element_by_tag_name("input").send_keys(os.getenv("MAIL"))
driver.find_elements_by_tag_name("button")[-2].click()

time.sleep(1)

# Password
driver.find_element_by_xpath("//input[@type='password']").send_keys(os.getenv("PASSWORD"))
driver.find_elements_by_tag_name("button")[-2].click()

time.sleep(15)

rows = driver.find_elements_by_tag_name("clr-dg-row")

table = []

for row in rows:
    columns = row.find_elements_by_tag_name("clr-dg-cell")
    temp = [column.text for column in columns]
    temp[0] = temp[0].split("\n")[0]
    table.append(temp)

df = pd.DataFrame(table, columns=["Name", "Submissions", "Most Recent Score", "Top Score", "First Score", "Average Score", "Actions"])
df.drop("Actions", axis=1, inplace=True)

fileName = driver.find_element_by_tag_name("h3").text

exportToExcel(df, fileName)
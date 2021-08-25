import pandas as pd
from selenium import webdriver
import time
from datetime import datetime
import ctypes


driver = webdriver.Chrome("chromedriver.exe")
now = datetime.now()
sheet_name_var = ""


if datetime.today().weekday() == 0:
    sheet_name_var = "Sheet1"
elif datetime.today().weekday() == 1:
    sheet_name_var = "Sheet2"
elif datetime.today().weekday() == 2:
    sheet_name_var = "Sheet3"
elif datetime.today().weekday() == 3:
    sheet_name_var = "Sheet4"
elif datetime.today().weekday() == 4:
    sheet_name_var = "Sheet5"
else:
    sheet_name_var = "Sheet1"


exc = pd.read_excel("horario.xlsx", sheet_name_var)



hr_comparacion = now.strftime("%H") + ":00" + ":00"
hr_actual = int()
print(hr_comparacion)



for i in exc.index:
    
    if exc["Hora"][i].strftime("%H:%M:%S") == hr_comparacion:
        hr_actual = i



for i in exc.index:
    i = i + hr_actual
    ctypes.windll.user32.MessageBoxW(0, ("Tienes otra clase a las:  " + now.strftime("%H") + ":00" + ":00"), "Tienes otra clase", 1)
    url = exc["Liga"][i]
    driver.get(url)
    time.sleep(2700)
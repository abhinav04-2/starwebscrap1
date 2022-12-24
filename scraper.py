from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(START_URL)
soup=BeautifulSoup(page.text,"html.parser")
startable=soup.find("table")
temp=[]
tablerows=startable.find_all("tr")
for tr in tablerows:
    cells=tr.find_all("td")
    row=[i.text.rstrip( ) for i in cells]
    temp.append(row)
name=[]
distance=[]
mass=[]
radius=[]
lu=[]
for i in range (1,len(temp)):
    name.append(temp[i][1])
    distance.append(temp[i][3])
    mass.append(temp[i][5])
    radius.append(temp[i][6])
    lu.append(temp[i][7])
headers= ['nameofstar',"distance","mass","radius","lu"]
stars = pd.DataFrame(list(zip(name, distance, mass, radius, lu)), columns = headers)
stars.to_csv("stars.csv") 




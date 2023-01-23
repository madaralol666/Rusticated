from selenium import webdriver
from bs4 import BeautifulSoup
import playsound
import datetime
import time
import os
import re


options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#Starting Driver
driver = webdriver.Edge(options=options)
driver.get('https://rusticated.com/')

time.sleep(0.2)
# DateTime(int)
def EventTime(TimeOfEvent):
    DropTime = re.sub("[h|m]",",",TimeOfEvent[:-3])
    DropTime = re.sub("[s| ]","",DropTime).split(',')
    DropTime_int = [int(x) for x in DropTime]
    DropTime_ = datetime.time(DropTime_int[0],DropTime_int[1],DropTime_int[2])
    return DropTime_
        
# Log Info
while True:
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    AirDrop = soup.findAll('span', class_="sc-cZFQFd cEnZuv")[56].text
    CargoShip = soup.findAll('span', class_="sc-cZFQFd cEnZuv")[57].text
    Heli = soup.findAll('span', class_="sc-cZFQFd cEnZuv")[58].text
    Chinook = soup.findAll('span', class_="sc-cZFQFd cEnZuv")[59].text

    # Sound Check
    if EventTime(AirDrop) == datetime.time(0, 0, 0):
        playsound.playsound('Sounds/Airdrop.mp3')
    if EventTime(CargoShip) == datetime.time(0, 0, 0):
        playsound.playsound('Sounds/Cargoship.mp3')
    if EventTime(Heli) == datetime.time(0, 0, 0):
        playsound.playsound('Sounds/Helli.mp3')
    if EventTime(Chinook) == datetime.time(0, 0, 0):
        playsound.playsound('Sounds/Chinook.mp3')

    time.sleep(1)
    os.system("cls")
    print(
        f"-------------------------------------\n"
        f"AirDrop:     {EventTime(AirDrop)}\n"
        f"CargoShip:   {EventTime(CargoShip)}\n"
        f"Heli:        {EventTime(Heli)}\n"
        f"ChinookInfo: {EventTime(Chinook)}\n"
        f"-------------------------------------",
    )
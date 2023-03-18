from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from Server_name import Server_names
from playsound import playsound
import time
import os
import threading


pars_link_account = "https://rusticated.com/"
options = EdgeOptions()
options.add_argument('headless')
options.add_argument('disable-logging')
options.add_argument('log-level=3')
options.add_argument('--enable-javascript')
driver = Edge(options=options)
driver.get(pars_link_account)
wait = WebDriverWait(driver, 10)

input_server_name = input("Input server name: ")

def sound_Air():
    playsound('Sounds/Airdrop.mp3')
def sound_Cargo():
    playsound('Sounds/Cargoship.mp3')
def sound_Helli():
    playsound('Sounds/Helli.mp3')
def sound_Chinook():
    playsound('Sounds/Chinook.mp3')

if input_server_name in Server_names:
    while True:

        element = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{input_server_name}')]")))
        event = element.find_elements(By.CSS_SELECTOR, "li.sc-jRwbcX.ksMOFF")
        time.sleep(0.5)
        os.system('cls')
        print("Airdrop    ", event[0].text.split('\n')[1])
        print("Cargoship  ", event[1].text.split('\n')[1])
        print("Helli      ", event[2].text.split('\n')[1])
        print("Chinook    ",event[3].text.split('\n')[1])

        if event[0].text.split('\n')[1] == "0h 0m 0s ago":
            thd_sound_air = threading.Thread(target=sound_Air)
            thd_sound_air.start()

        if event[1].text.split('\n')[1] == "0h 0m 0s ago":
            thd_sound_cargo = threading.Thread(target=sound_Cargo)
            thd_sound_cargo.start()

        if event[2].text.split('\n')[1] == "0h 0m 0s ago":
            thd_sound_Helli = threading.Thread(target=sound_Helli)
            thd_sound_Helli.start()

        if event[3].text.split('\n')[1] == "0h 0m 0s ago":
            thd_sound_Chinook = threading.Thread(target=sound_Chinook)
            thd_sound_Helli.start()
else:
    print('Error: not found server name')

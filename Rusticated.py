from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from Server_name import Server_names
import playsound
import time
import os


pars_link_account = "https://rusticated.com/"
options = EdgeOptions()
options.add_argument('headless')
options.add_argument('disable-logging')
options.add_argument('log-level=3')
options.add_argument('--enable-javascript')
driver = Edge(options=options)
driver.get(pars_link_account)
wait = WebDriverWait(driver, 10)

input_server_name = input()

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
            playsound.playsound('Sounds/Airdrop.mp3')

        if event[1].text.split('\n')[1] == "0h 0m 0s ago":
            playsound.playsound('Sounds/Cargoship.mp3')

        if event[2].text.split('\n')[1] == "0h 0m 0s ago":
            playsound.playsound('Sounds/Helli.mp3')
            
        if event[3].text.split('\n')[1] == "0h 0m 0s ago":
            playsound.playsound('Sounds/Chinook.mp3')
else:
    print('Error: not found server name')

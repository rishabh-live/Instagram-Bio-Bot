#Definition 
PostId = "<Your POST ID Here>"
USERNAME = "<Your User Name>"
PASSWORD = "<Your Account Password>"






print("Starting Import\r")

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import json

print("Starting Chrome\r")

driver = webdriver.Chrome('./chromedriver')



def checkLikes():
    #driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.instagram.com/p/"+PostId)
    noButton = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d     _8A5w5    ']")
    totalNo = noButton.find_element_by_css_selector('span').text

    #Read File and Get DATA
    with open('./records.json') as f:
        data = json.load(f)

    #Check Values
    if data['likes'] < totalNo:
        data['updated'] = "TRUE"
        data['likes'] = totalNo
    else:
       data['updated'] = "FALSE" 

    

    #Upadte record with new values
    with open('./records.json', 'w+') as json_file:
        json.dump(data, json_file)


def perform():
     
    driver.get("https://www.instagram.com")

    sleep(random.randint(6,11))
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    buttonSubmit = driver.find_element_by_xpath("//button[@type='submit']")

    username.send_keys(USERNAME)
    sleep(random.randint(0,4))
    password.send_keys(PASSWORD)
    sleep(random.randint(0,2))
    buttonSubmit.send_keys(Keys.RETURN)

    



    print("Logging Completed")

    sleep(4)

    notNow = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    notNow.send_keys(Keys.RETURN)
    sleep(random.randint(0,2))

    driver.get("https://www.instagram.com/accounts/edit/")

    sleep(random.randint(0,5))

    typewriter = driver.find_element_by_xpath("//textarea[@class='p7vTm']")
    typewriter.send_keys(Keys.CONTROL + "a")
    typewriter.send_keys(Keys.BACKSPACE)

    sleep(random.randint(0,2))

    bioTextLine1 = '#IBTA'

    for element in range(0, len(bioTextLine1)):
        sleep(random.randint(0,1))
        typewriter.send_keys(bioTextLine1[element])

    typewriter.send_keys(Keys.RETURN)

    bioTextLine1 = 'Project Aim : Get the no. of likes on the latest post( @rishabh.live )and update the bio here'

    for element in range(0, len(bioTextLine1)):
        sleep(random.randint(0,1))
        typewriter.send_keys(bioTextLine1[element])
    
    typewriter.send_keys(Keys.RETURN)
    
    with open('./records.json') as f:
        data = json.load(f)

    bioTextLine1 = 'Likes : ' + data['likes']

    for element in range(0, len(bioTextLine1)):
        sleep(random.randint(0,1))
        typewriter.send_keys(bioTextLine1[element])

    sleep(random.randint(0,2))
    submitUpdate = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
    submitUpdate.send_keys(Keys.RETURN)



    
checkLikes()

with open('./records.json') as f:
    data = json.load(f)


if data['updated'] == "TRUE":
    perform()
else:
    print("Bio Already Up-to-date")
    

driver.close()

#sqdOP yWX7d     _8A5w5    

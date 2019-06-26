import os
import re
from selenium import webdriver
from selenium.webdriver.common import keys
from lib2to3.tests.support import driver
from re import search
from nltk.data import clear_cache
from findertools import select
from selenium.webdriver.support.ui import Select
from aetypes import Boolean
import time
from nltk.sem.chat80 import contains
from cgitb import text
from macerrors import noSuchIconErr

#To setup chrome driver path and launch & open the github website in the chrome browser
driver = webdriver.Chrome("/Users/mackbookpankaj/eclipse-workspace/ChromeWebDriver/chromedriver")
driver.maximize_window()
driver.get("https://github.com")
text_found = driver.find_element_by_xpath("/html/body/div[4]/main/div[1]/div/div/div[1]/h1")
if text_found.text=="Built for developers" :
    print "Url entered and website displayed"
else:
    print "Entered a wrong Url"

#To click Sign in button
sign_in_button = driver.find_element_by_link_text("Sign in")
if sign_in_button.is_enabled():
    sign_in_button.click()
    print ("The wegpage is redirect to login page")
else :
    print ("The webpage is not redirect to login page")

#Enter username, password and click sign in button
mandatory_field = driver.find_element_by_name("login")
mandatory_field.send_keys("testingpython")
mandatory_field = driver.find_element_by_id("password")
mandatory_field.send_keys("test1234")
sign_in_button = driver.find_element_by_name("commit")
sign_in_button.click()
text_found = driver.find_element_by_id("js-flash-container")
if text_found.text=="Incorrect username or password." :
    print("Displaying message when entered username & password is wrong: Incorrect username or password.")
else:
    print("Nothing found")
mandatory_field = driver.find_element_by_name("login").clear()


#To click forgot link and inserting email id as m.ie
forgot_password = driver.find_element_by_link_text("Forgot password?")
forgot_password.click()
mandatory_field_email = driver.find_element_by_id("email_field")
mandatory_field_email.send_keys("m.ie")
reset_password = driver.find_element_by_name("commit")
reset_password.click()
text_message = driver.find_element_by_id("js-flash-container")
if text_message.text=="Can't find that email, sorry." :
    print "Message displayed in the webpage when the value entered in the mandatory email field is invalid : Can't find that email, sorry."
else:
    print "Nothing found"
    
  
#To click send password reset email without input
mandatory_field = driver.find_element_by_name("email")
mandatory_field.send_keys("")
reset_password = driver.find_element_by_name("commit")
reset_password.click()
text_message = driver.find_element_by_id("js-flash-container")
if text_message.text=="Can't find that email, sorry." :
    print "Message displayed in the webpage when the value entered in the mandatory email field is empty: Can't find that email, sorry."
else:
    print "Nothing found"
    


#To search the First word of the message- Can't
text_found = driver.find_element_by_id("js-flash-container")
#print(text_found.text)
first = text_found.text.partition(' ')[0]
if first=="Can't" :
    print("Found the first word of the message is: Can't ")
else:
    print("Nothing found")

driver.back()
driver.back()
driver.back()
driver.back()
driver.back()


#To click Sign Up button and redirect to join github page
search_field = driver.find_element_by_link_text("Sign up")
if search_field.is_enabled():
    search_field.click()
    print ("The webpage is redirect to join github page")
else :
    print ("The webpage is not redirecting to join github page")


#To search the text "Create your personal account" in join github page
text_contain = driver.find_element_by_xpath("//h2[contains(.,'Create your personal account')]")
#print(text_contain.text)
if text_contain.text=='Create your personal account': 
    print("join github page contains the text: Create your personal account")
else:
    print("join github page does not contain the text: Create your personal account")
        
   
#To check the entered email id is existing    
exiting_email = driver.find_element_by_id("user_email")
exiting_email.send_keys("sheepankaj@gmail.com")
time.sleep(2)
exiting_email1 = driver.find_element_by_xpath("//p[contains(.,'Email is invalid or already taken')]")
if exiting_email1.text=="Email is invalid or already taken" :
    print ("Create an account button is grayed when an existing email address is inserted in join github page")
else:
    print ("The inserted email id is not existing earlier")


driver.quit()

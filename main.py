from PyP100 import PyL530 # PyP100 is a Python library for controlling many of the TP-Link Tapo devices including the P100, P105, P110 plugs and the L530 and L510E bulbs.

import speech_recognition # Speech Recognition module
import pyttsx3 as tts # Text-to-Speech module

import requests
import time
import sys

# FUTURE PLANS
# I will put this code into an arduino and make it work 24/7

# Making sure that we have internet connection
def check_internet_connection():
    url = "http://www.google.com"
    timeout = 5
    while True:
        try:
            request = requests.get(url, timeout=timeout)
            print("Connected to the Internet")
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")

# Connecting to TAPO servers
def connect_bulb():
    # Fetching your TAPO username and password 
    with open(r"D:\Programming\Github\voice-control-lights\credits.txt", "r") as f:
        lines = f.readlines()
        mail = lines[0].strip()
        password = lines[1].strip()

    # In the tapo app:
    # Click your device
    # Click the settings icon
    # Click the device info
    ip_address = "192.168.1.2"

    l530 = PyL530.L530(ip_address, mail, password) #Creating a PL530 light bulb object

    # Sometimes connecting doesn't work properly
    # So we are trying again if there is a error
    for i in range(5):
        try:
            l530.handshake() #Creates the cookies required for further methods
            l530.login() #Sends credentials to the plug and creates AES Key and IV for further methods
            return l530 # Returns the bulb object if everything is fine
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
    
    return False # Returns false is it couldn't connect

def turnOff(l530):
    l530.turnOff() # Sends the turn off request

def turnOn(l530):
    l530.turnOn() # Sends the turn off request

def speech_recognizer(l530):
    # Creating recognizer object
    recognizer = speech_recognition.Recognizer()

    while True:
        try:
            # Starting to listen
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic) # Setting the ambient noise so it can understand us properly
                print("I'm listening...")
                audio = recognizer.listen(mic, phrase_time_limit=5) # We're setting phrase time limit as 5 because this module can stuck in listening sometimes

                text = recognizer.recognize_google(audio) # Speech-to-text with Google

                text = text.lower()

                print(f"you said {text}")

                if "turn off" == text:
                    turnOff(l530)
                    talk(text) 
                if "turn on" == text:
                    turnOn(l530)
                    talk(text)
                if "stop" == text:
                    talk(text)
                    sys.exit()

        except Exception as e:
            # If there is a error about recognizer object we should create it again
            recognizer = speech_recognition.Recognizer()
            print(e)
            continue


engine = tts.init()

def talk(phrase):
    # Talking stuffs
    if phrase == "turn off":
        engine.say("I'm turning the lights off.")
    elif phrase == "turn on":
        engine.say("I'm turning the lights on.")
    elif phrase == "stop":
        engine.say("Goodbye!")
        
    engine.runAndWait()

def main():
    check_internet_connection()

    l530 = connect_bulb()

    if l530 != False:
        # Building up text to speech module
        rate = engine.getProperty('rate')
        # Getting details of current speaking rate
        engine.setProperty('rate', 140) # The speed of talk
        
        voices = engine.getProperty('voices')
        # 1 for male 0 for female
        engine.setProperty('voice', voices[1].id)

        volume = engine.getProperty('volume')
        # Getting to know current volume level (min=0 and max=1)
        engine.setProperty('volume', 0.5)

        # Starting to listen
        speech_recognizer(l530)
    else:
        print("There is a problem about connecting to servers.")

main()


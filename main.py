from win10toast import ToastNotifier # Notification module

import speech_recognition # Speech Recognition module

import requests # API Call

def send_message(message):
    toast = ToastNotifier()

    toast.show_toast(
        "Light State",
        message,
        duration = 5,
        icon_path = "icon.ico",
        threaded = True,
)


def check_internet_connection():
    url = "http://www.google.com"
    try:
        r = requests.get(url)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

def api_call(key, state):
    send_message(f"Turning the lights {state}.")
    requests.get(f"https://maker.ifttt.com/trigger/bulb_{state}/json/with/key/{key}")
        
def speech_recognizer(key):
    # Creating recognizer object
    recognizer = speech_recognition.Recognizer()
    while True: 
        try:
            # Starting to listen
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic) # Setting the ambient noise so it can understand us properly
                
                print("I'm listening...")

                audio = recognizer.listen(mic, phrase_time_limit=5) # We're setting phrase time limit as 5 because this module can stuck in listening time to time

                text = recognizer.recognize_google(audio) # Speech-to-text with Google

                text = text.lower()

                print(f"you said {text}")

                if "turn off" in text or "turn on" in text: 
                    if check_internet_connection():
                        api_call(key, "on") if "turn on" in text else api_call(key, "off")
                        # if "turn on" in text -> api_call(key, "on")
                        # if "turn off" in text -> api_call(key, "off")
                        
        except Exception as e:
            print(e)
            # If there is a error about recognizer object we should create it again
            recognizer = speech_recognition.Recognizer()

def main():
    with open(r"C:\Users\Serkan\Programming\Python\voice-control-lights\key.txt", "r") as f:
        IFTTT_KEY = f.readline()

    speech_recognizer(IFTTT_KEY)

main()

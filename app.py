import os
import webbrowser
import pyautogui
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Dictionary of applications to open
dictapp = {
    "command prompt": "cmd",
    "paint": "paint",
    "wps": "wps",
    "camera": "Camera",
    "chrome": "chrome",
    "vs code": "code",
    "power bi": r'"C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe"',
    "whatsapp": r'"D:\WhatsApp.lnk"',
    "notepad": "notepad"
}

def openappweb(query):
    if ".com" in query or ".co.in" in query or ".org" in query:
        speak("Launching..")
        print("Launching..")
        query = query.replace("open", "")
        query = query.replace(" ", "")
        query = query.replace("launch", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak(f"Opening {app}..")
                print(f"Opening {app}..")
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("Closing..")
    print("Closing..")
    if "one tab" in query or "tab" in query:
        pyautogui.hotkey("ctrl", "w")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak(f"Closing {app}..")
                print(f"Closing {app}..")
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

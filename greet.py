import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
# print(voices[0])
engine.setProperty("rate",190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning.")
    elif 12 <= hour < 18:
        speak("Good Afternoon.")
    else:
        speak("Good Evening.")
    speak("Please tell me, How can I help you?")

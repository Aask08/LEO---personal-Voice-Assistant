import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from winerror import HRESULT_SEVERITY


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,3)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said: {query}\n")
    except Exception :
        print("Say that again.")
        return "None"
    return query

query= takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Setting the voice ID
engine.setProperty("rate", 180)  # Speed of speech

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchgoogle(query):
    if "google" in query:
        import wikipedia as googlescrap
        query = query.replace("Ava","")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        print("This is what i found on google...")
        speak("This is what i found on google...")

        try:
            pywhatkit.search(query)
            result=googlescrap.summary(query,1)
            speak(result)

        except:
            speak("No speackable output avaliable...")

def searchyoutube(query):
    if "youtube" in query:
        query = query.replace("Ava", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        print("This is what i found for your Search...")
        speak("This is what i found for your Search...")
        web ="https://www.youtube.com/results?search_query=" +query
        webbrowser.open(web)
        print("Done sir...")
        speak("Done sir...")
def searchyoutubeplay(query):
    if "youtube play" in query:
        query = query.replace("Ava", "")
        query = query.replace("youtube play search", "")
        query = query.replace("youtube play", "")
        speak("This is what i found for your Search...")
        print("This is what i found for your Search...")
        web ="https://www.youtube.com/results?search_query=" +query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        print("Done sir...")
        speak("Done sir...")

def searchwikipedia(query):
    if "wikipedia" in query:
        print("searching from wikipedia...")
        speak("searching from wikipedia...")
        query = query.replace("Ava", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        results=wikipedia.summary(query,sentences=2)
        print("according to wikipedia...")
        speak("according to wikipedia...")
        print(results)
        speak(results)
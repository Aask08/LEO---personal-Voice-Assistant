import datetime
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 190)  # Speed of speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.dynamic_energy_threshold = True
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=4)
        except sr.WaitTimeoutError:
            print("Listening timed out. Try again.")
            speak("Listening timed out. Please try again.")
            return "None"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said: {query}\n")
        speak(f"You said: {query}")
    except sr.UnknownValueError:
        print("I didn't catch that. Can you say it again?")
        speak("I didn't catch that. Can you say it again?")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        speak("Something went wrong. Please try again.")
        return "None"

    return query


def display_menu():
    # Full menu
    menu = """
    I am awake now! Here are some things you can ask me:
    1. Say 'Google' to search the web.
    2. Say 'YouTube play [song or video name]' to play something on YouTube.
    3. Say 'Wikipedia [topic]' to search for information on Wikipedia.
    4. Ask for the 'temperature' to get the current temperature.
    5. Ask for the 'time' to know the current time.
    6. Say 'open [application name]' to launch an app or tab.
    7. Say 'close [application name]' to close an app or tab.
    8. Say 'sleep' to make me sleep.
    """
    print(menu)


    spoken_menu = (
        "I am awake. You can ask me to search Google, play a video on YouTube, "
        "look up something on Wikipedia, check the temperature or the time. "
        "You can also ask me to open or close apps, or say sleep to make me sleep."
    )
    speak(spoken_menu)
    speak("What would you like to do next?")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "wake up" in query:
            from greet import greetme

            greetme()
            display_menu()

            while True:
                query = takeCommand().lower()

                if "sleep" in query:
                    speak("OK, You can call me anytime. Going to sleep.")
                    print("OK, You can call me anytime. Going to sleep.")
                    exit()

                # Conversations
                elif "hello" in query:
                    speak("Hello ma'am, how are you?")
                elif "i am fine" in query:
                    speak("That's great to hear!")
                elif "how are you" in query:
                    speak("I'm doing great, thanks for asking!")

                #open/close app
                elif "open" in query:
                    from app import openappweb
                    openappweb(query)
                elif "close" in query:
                    from app import closeappweb
                    closeappweb(query)

                # Web search functionalities
                elif "google" in query:
                    from search import searchgoogle

                    searchgoogle(query)
                elif "youtube play" in query:
                    from search import searchyoutubeplay

                    searchyoutubeplay(query)
                elif "youtube" in query:
                    from search import searchyoutube

                    searchyoutube(query)
                elif "wikipedia" in query:
                    from search import searchwikipedia

                    searchwikipedia(query)

                # Temperature
                elif "temperature" in query:
                    search = "temperature in Bhubaneswar"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"Current {search} is {temp}")
                    print(f"Current {search} is {temp}")

                # Time
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {strTime}.")
                    print(f"The time is {strTime}.")


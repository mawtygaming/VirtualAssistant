import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import time

BOSS = "Boss Maw"
# AI = "alexa"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# This Function will pronounce the string passed to it.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This Function will get the current military time.
def greetings():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Magandang Umaga!" + BOSS)
    elif hour >= 12 and hour <= 18:
        speak("Magandang Hapon!" + BOSS)
    elif hour > 18 and hour <= 23:
        speak("Magandang Gabi!" + BOSS)
    else:
        pass
    speak("I am Kalbo, what can I do for you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-us') # speechRecognition class on Google
        # download .whl file here https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
        # print(BOSS + f" said: {query}\n")

    except Exception as e:
        # print("I'm Sorry I didn't hear what you said.")
        query = None

    return query

# Main Program starts here.
speak("Initializing Kalbo...")
time.sleep(4)
speak("Initializing Complete!")
greetings()

def main():
    query = takeCommand()
    yt = "open youtube"

    # Logic on executing basic task.
    try:
        if 'wikipedia' in query.lower():
            speak("Searching Wikipedia...")
            query = query.replace("wikipedea", "")
            results = wikipedia.summary(query, sentences = 1)
            speak(results)

        elif 'open python tutorials' in query.lower():
            speak("Opening Python Tutorials.")
            url = "https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif yt in query.lower():
            speak("Opening Youtube.")
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query.lower():
            speak("Opening Google.")
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open facebook' in query.lower():
            speak("Opening Facebook.")
            url = "facebook.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open messenger' in query.lower():
            speak("Opening Messenger.")
            url = "messenger.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open my manga' in query.lower():
            speak("Opening Manga reader.")
            url = "mangareader.net"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open github' in query.lower():
            speak("Opening Git Hub.")
            url = "github.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query.lower():
            speak("Opening your music.")
            songs_dir = 'C:/Users/markb/Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"{BOSS}, the time is {strTime}")

        elif 'open steam' in query.lower():
            speak("Opening Steam.")
            steamPath = 'C:\\Program Files (x86)\\Steam\\Steam.exe'
            os.startfile(steamPath)

        elif 'open garena' in query.lower():
            speak("Opening Garena.")
            garenaPath = 'C:\\Program Files (x86)\\Garena\\Garena\\Garena.exe'
            os.startfile(garenaPath)

        elif 'open remote' in query.lower():
            speak("Opening Putty")
            puttyPath = 'C:\\Program Files\\PuTTY\\putty.exe'
            os.startfile(puttyPath)

        elif 'open word' in query.lower():
            speak("Opening Microsoft Word")
            wordPath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(wordPath)

        elif 'open powerpoint' in query.lower():
            speak("Opening Microsoft Power Point")
            pptPath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(pptPath)

        elif 'open excel' in query.lower():
            speak("Opening Microsoft Excel")
            excelPath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
            os.startfile(excelPath)

        elif 'open thunder bird' in query.lower():
            speak("Opening Mozilla Thunderbird")
            birdPath = 'C:\\Program Files (x86)\\Mozilla Thunderbird\\thunderbird.exe'

        else:
            # speak("I can't understand you!")
            main()

    except Exception as ex:
        query = None

while True:
    main()

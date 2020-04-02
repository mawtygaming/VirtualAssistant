import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image
import pyttsx3 
import speech_recognition as sr 
import datetime

global ti

ti = StringVar()

# This function is the object of the main window
class mainWindow:
    def __init__(self, ui):
        self.logoImg = logoImg = ImageTk.PhotoImage(Image.open("logo.png"))
        self.logoPlace = logoPlace = Label(image=logoImg).grid(row=0, column=0)
        # This is the frame 
        self.frameUI = frameUI = LabelFrame(ui,text = "Setup Virtual Assistant", font='Helvetica 14 bold', padx=20, pady=20)
        frameUI.grid(row=0, column=1)

        # Object for Play image
        self.imgPlay = imgPlay=PhotoImage(file="play.png")
        self.imgStop = imgStop=PhotoImage(file="stop.png")

        # These are buttons
        self.btnPlay = btnPlay = Button(frameUI, start())
        btnPlay.config(image=imgPlay)
        btnPlay.grid(row=0, column=1)
        self.btnStop = btnStop = Button(frameUI)
        btnStop.config(image=imgStop)
        btnStop.grid(row=0, column=2)
        btnMas = Button(frameUI, text = "Master", padx=25,pady=4).grid(row=0, column=3)
        btnWeb = Button(frameUI, text = "Add Website", padx=25,pady=4).grid(row=0, column=4)
        btnAdd = Button(frameUI, text = "Add Program", padx=25,pady=4).grid(row=0, column=5)
        btnMusic = Button(frameUI, text = "Play Music", padx=25,pady=4).grid(row=0, column=6)

    # This function must open a new window
    def addWindowbtn(self):
        pass   

# class addWindow:
#     def __init__(self, ui):
#         pass

def mainWin():
    ui = tk.Tk()
    window = mainWindow(ui)
    ui.title("Virtual Assistant")
    ui.iconbitmap("C:/Users/markb/OneDrive/Desktop/Virtual Assistant/logo.ico")
    ui.resizable(0,0)

    # Make center position
    ws = ui.winfo_screenwidth() # This is to get your windows screen width
    hs = ui.winfo_screenheight() # This is to get your windows screen height
    w = 765 # Define your application width
    h = 200 # Define your application height
    # calculate position x, y
    x = (ws/2) - (w/2) # This is to center the app based on width
    y = (hs/2) - (h/2) # This is to center the app based on height
    ui.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    ui.mainloop()

def speakEngine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        r.pause_threshold = 1
        r.energy_threshold = 400
    try:
        query = r.recognize_google(audio, language = 'en-us')
    except Exception as e:
        return None

def start():
    speak("Hi Boss")
    while True:
        query = takeCommand()

        if 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak("the time is {strTime}")
        else:
            speak("Didn't hear what you said.")

if __name__ == "__main__":
    mainWin()
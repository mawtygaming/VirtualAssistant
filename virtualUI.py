from tkinter import *
from PIL import ImageTk, Image

# Setting up Tkinter
ui = Tk()
ui.title("Virtual Assistant")
ui.iconbitmap("C:/Users/markb/OneDrive/Desktop/Virtual Assistant/logo.ico")
ui.resizable(0,0)

# Function to make the dialog box in center position
def center_window(w=690, h=200):
    # get screen width and height
    ws = ui.winfo_screenwidth()
    hs = ui.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    ui.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Dialog box height
center_window(720,200)

logoImg = ImageTk.PhotoImage(Image.open("logo.png"))
logoPlace = Label(image=logoImg).grid(row=0, column=0)

frameUI = LabelFrame(ui,text = "Setup Virtual Assistant", font='Helvetica 14 bold', padx=20, pady=20)
frameUI.grid(row=0, column=1)

btnTest = Button(frameUI, text = "Master", padx=25).grid(row=0, column=1)
btnTest2 = Button(frameUI, text = "Add Website", padx=25).grid(row=0, column=2)
btnTest3 = Button(frameUI, text = "Add Program", padx=25).grid(row=0, column=3)
btnTest4 = Button(frameUI, text = "Play Music", padx=25).grid(row=0, column=4)

ui.mainloop()
from tkinter import *
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import os

color1 = "#CCC5B9"
color2 = "#FFFCF2"
color3 = "#403D39"
color4 = "#252422"
color5 = "#EB5E28"

root = Tk()
root.geometry("760x480")
root.title("Luísa")
root.config(bg=color2)

audio = sr.Recognizer()
luisa = pyttsx3.init()
for voice in luisa.getProperty('voices'):
    if voice.name == "Microsoft Zira Desktop - English (United States)":
        luisa.setProperty('voice', voice.id)
        break

luisa.say('Hey, my name is Luísa')
luisa.say('How can i help you?')
luisa.runAndWait()


def comand_execute():
    titletext.configure(text="I'm listening!")
    titletext.place(x=180, y=120)
    try:
        with sr.Microphone() as source:
            voice = audio.listen(source)
            comand = audio.recognize_google(voice, language="en-US")
            comand = comand.lower()
            if "luisa" in comand:
                comand = comand.replace("luisa", "")
                luisa.say(comand)
                luisa.runAndWait()

    except:
        luisa.say("I'm sorry, i couldn't understand you")

    return comand


def user_voice():
    comand = comand_execute()
    if "time" in comand:
        time = datetime.datetime.now().strftime("%H:%M")
        luisa.say("It's" + time)
        luisa.runAndWait()

    elif "play" in comand:
        music = comand.replace("play", "")
        musicresult = pywhatkit.playonyt(music)
        luisa.say("Playing" + music)
        luisa.runAndWait()

    elif "search for" in comand:
        search = comand.replace("search for", "")
        wikipedia.set_lang("en")
        result = wikipedia.summary(search, 2)
        luisa.say(result)
        luisa.runAndWait()

    elif "open" in comand:
        open = comand.replace("open", "")
        os.system(f"start {open}.exe")
        luisa.say(f"Opening {open}")
        luisa.runAndWait()

    elif "alexa" in comand:
        luisa.say(" I love alexa!, hahahahahahaha")
        luisa.runAndWait()


titletext = Label(root, text="Luísa", font=("COMIC SANS MS", 48, "bold"), fg=color5, bg=color2)
titletext.place(x=300, y=120)

b1 = Button(root, text="Speak", font=("COMIC SANS MS", 16, "bold"), bg=color1, command=comand_execute and user_voice)
b1.place(width=200, height=50, x=280, y=350)

root.mainloop()

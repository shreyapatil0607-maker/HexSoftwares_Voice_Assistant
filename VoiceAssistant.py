import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import threading


myName = "Siri"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)   # female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hey Shreya, Good Morning....!! I am siri...., How may I help you?")
        #speak("I am siri, How may I help you?")

    elif 12 <= hour < 18:
        speak("Hey Shreya, Good Afternoon...!! I am siri...., How may I help you?")
        #speak("I am siri, How may I help you?")

    else:
        speak("Hey Shreya, Good Evening....!!I am siri...., How may I help you?")
        

def takeCommand():   # Voice Input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"You said: {query}")
        return query

    except:
        print("Say that again please...")
        return "None"
    
def take_screenshot():
    folder="screenshots"
    if not os.path.exists(folder):
        os.mkdir(folder)

    time_stamp=datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    path=f"{folder}/Screenshot_{time_stamp}.png"
    img=pyautogui.screenshot()
    img.save(path)

    speak(f"Screenshot saved in {path}")


# ========== MAIN ==========
if __name__ =="__main__":
    wishme()
    while True:
        command = takeCommand().lower()
        speak(f"You said {command}")


        if 'open google' in command or 'google' in command:
            webbrowser.open('www.google.com')

        elif 'open firefox' in command or 'firefox' in command:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            speak("Opening Firefox")

        # -------- OPEN VS CODE --------
        elif 'open vs code' in command or 'vs code' in command:
            os.startfile("C:\\Users\\YOURUSER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            speak("Opening Visual Studio Code")

        # -------- OPEN NOTEPAD --------
        elif 'open notepad' in command or 'notepad' in command:
            os.startfile("notepad.exe")
            speak("Opening Notepad")

        # -------- OPEN YOUTUBE --------
        elif 'open youtube' in command or 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        # -------- OPEN WHATSAPP --------
        elif 'open whatsapp' in command or 'whatsapp' in command:
            webbrowser.open("https://web.whatsapp.com")
            speak("Opening WhatsApp")

        # -------- OPEN MS WORD --------
        elif 'open word'  in command or 'word' in command:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            speak("Opening Microsoft Word")

        # -------- OPEN EXCEL --------
        elif 'open excel' in command or 'excel'in command:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
            speak("Opening Excel")

        # -------- OPEN POWERPOINT --------
        elif 'open powerpoint' in command or 'power' in command:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            speak("Opening PowerPoint")
        
        elif 'take screenshot' in command or 'screenshot' in command:
            take_screenshot()

        elif 'shutdown' in command :
            speak("shutting down your computer")
            os.system("shutdown /s /t 5")

        
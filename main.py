import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Initialize Speech Recognition
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='en-in')
            print(command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None

def run_jarvis():
    speak("Hello, I'm Jarvis. How can I assist you today?")
    while True:
        command = take_command()
        if command is None:
            continue
        elif "what's your name" in command:
            speak("My name is Jarvis.")
        elif "what time is it" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + time)
        elif "search" in command:
            query = command.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        elif "play" in command:
            song = command.replace("play", "")
            pywhatkit.playonyt(song)
        elif "joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "exit" in command:
            speak("Goodbye!")
            break
        elif "open facebook" in command:
            url = "https://www.facebook.com"
            webbrowser.open(url)
        elif "open twitter" in command:
            url = "https://www.twitter.com"
            webbrowser.open(url)
        elif "open instagram" in command:
            url = "https://www.instagram.com"
            webbrowser.open(url)
        elif "open gmail" in command:
            url = "https://mail.google.com"
            webbrowser.open(url)
        elif "open wikipedia" in command:
            url = "https://www.wikipedia.org"
            webbrowser.open(url)
        elif "open notepad" in command:
            os.system("notepad.exe")
        elif "open calculator" in command:
            os.system("calc.exe")
        elif "open task manager" in command:
            os.system("taskmgr.exe")
        elif "open youtube" in command:
            url = "https://www.youtube.com"
            webbrowser.open(url)
        elif "open google" in command:
            url = "https://www.google.com"
            webbrowser.open(url)
        elif "open linkedin" in command:
            url = "https://www.linkedin.com"
            webbrowser.open(url)
        else:
            speak("Command not recognized!")

run_jarvis()

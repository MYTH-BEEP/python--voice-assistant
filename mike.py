import speech_recognition as sr
import pyttsx3
import datetime
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import smtplib
import random

MASTER ='sir'

print('intializing mike')

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices','voices[0].id')
#print(voices[0].id)
engine.setProperty('rate',150)

def speak(text):
  engine.say(text)
  engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("Good morning" + MASTER)

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good evening" + MASTER)

    speak("yo i am mike whatsup how may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print("Try again please.")
        speak("I couldn't understand what you were trying to say. Say that again please")
        query = None
    return query
    
print("Ready!")
speak("Ready...")
wishMe()
query = takeCommand()


#commands

if 'wikipedia' in query.lower():
    print("searching wikipedia...")
    speak('searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    speak("Opening youtube...")
    webbrowser.open("https://www.youtube.com")

elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")


elif 'open google' in query.lower():
    print("Opening google...")
    speak("Opening google...")
    webbrowser.open("https://www.google.com")

elif 'who created you' in query.lower():
    print("MR.MYTH created me")
    speak("Austrin created be") 

elif 'how are you?' in query.lower():
    print("i am fine")
    speak("i am finee")        








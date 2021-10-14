import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyaudio
import pyjokes
import requests
from bs4 import BeautifulSoup

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def any_more():
    print("Any other question ? Otherwise Say \"exit\"")
    talk("Any other question ? Otherwise Say \"exit\"")


def query(user_query):

    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='Z0LcW XcVN5d').get_text()
    return result


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk("listening...")
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        talk("No response from you")
        print("Exiting")
        talk("i am exiting the session")
    return command


def run_alexa():
    command = take_command()
    print(command)
    try:
        if 'play song' in command:
            song = command.replace('play song', '')
            talk('playing ' + song)
            print('playing ' + song)
            pywhatkit.playonyt(song)
            e = 0
            any_more()

            return e
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is ' + time)
            talk('Current time is ' + time)
            e = 0
            any_more()
            return e
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
            e = 0
            any_more()
            return e

        elif 'wikipedia of' in command:
            search = command.replace('wikipedia of', '')
            info = wikipedia.summary(search, 3)
            print(info)
            talk(info)
            any_more()
            e = 0
            return e
        elif 'exit' in command:
            talk("you exited")
            e = 1
            return e
        else:
            result = query(command)
            print(result)
            talk(result)
            e = 0
            any_more()
            return e

    except:
        talk('Pardon Please , we dont have information about given topic')
        e = 0
        any_more()
        return e
    

def initialize():
    try:
        with sr.Microphone() as source:
            print(".")
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alice' in command:
                talk("hii , i am glad to see you again !!!")
                talk("Tell me what can do for you ?")
                e = 0
                while True:
                    if e == 0:
                        e = run_alexa()

                    else:
                        break

    except:
        pass

    
while True:
    initialize()


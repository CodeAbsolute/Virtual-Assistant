import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def run_alexa():
    command = take_command()
    print(command)
    if 'wikipedia' in command:  # if wikipedia found in the query then this block will be executed
        talk('Searching Wikipedia...')
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        talk("According to Wikipedia")
        print(results)
        talk(results)

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in command:
        webbrowser.open("stackoverflow.com")
    elif 'play music' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'who are you' in command:
        talk('I am Alexa your Assistant')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open code' in command:
        code_path = '"C:\\Users\\mahes\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
        os.startfile(code_path)
    elif 'quit' in command:
        exit()
    else:
        talk('Please say the command again.')


def wishme():
    hour = int(datetime.datetime.now().hour)
    print(datetime.datetime.now())
    if hour >= 0 and hour < 12:
        talk("good morning")
    elif hour >=12 and hour <=18:
        talk("good afternoon")
    else:
        talk("good evening")
    talk("I'm Alexa")

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
                print(command)
    except:
        pass
    return command

wishme()
while True:
    run_alexa()
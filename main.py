import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:

            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' +time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache but I am everywhere with you')
    elif 'are you single' in command:
        talk('I am in a relationship with Wifi')
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'kiss' in command:
        talk('I can but I am a Virtual Assistant')
    elif 'how are you' in command:
        talk('I am Good, Hope so as you are')
    elif 'hey' in command:
        talk('Hello, How are you....?')
    elif 'who made you' in command:
        talk('Sakshi Sonavane and Tejas Gupta')
    elif 'purpose' in command:
        talk('for their college mini project')
    elif 'thank you' in command:
        talk('Its my pleasure, Have a Great Day')
        return False
    elif 'chrome' in command:
        a='opening chrome....'
        engine.say(a)
        engine.runAndWait()
        program="C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])
        subprocess.Popen([program])
    elif 'youtube' in command:
        a='opening youtube....'
        engine.say(a)
        engine.runAndWait()
        url = "https://www.youtube.com/"
        webbrowser.open(url)
    elif 'power toys' in command:
        a='opening powertoys....'
        engine.say(a)
        engine.runAndWait()
        program="C:\Program Files\PowerToys\PowerToys.exe"
        subprocess.Popen([program])
    else:
        talk('please say it again')
    return True

while True:
    if not run_alexa():        
        break
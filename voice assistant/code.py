import speech_recognition as sr
import pyaudio
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises..Please wait')
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('ask me anything...')
        recordedaudio=recognizer.listen(source)

    try:
        command=recognizer.recognize_google(recordedaudio)
        command = command.lower()
        print(f"User said: {command}")

        if 'open chrome' in command:
            engine.say('Opening Google Chrome')
            engine.runAndWait()
            subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
        elif 'time' in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            engine.say(f"Current time is {time}")
            engine.runAndWait()
        elif 'play' in command:
            try:
                video = command.split('play')[1].strip()
                engine.say(f"Playing {video} on YouTube")
                engine.runAndWait()
                pywhatkit.playonyt(video)
            except Exception as e:
                print(f"An error occurred: {e}")
                engine.say(f"An error occurred: {e}")
                engine.runAndWait()
        elif 'open youtube' in command:
            engine.say('Opening YouTube')
            engine.runAndWait()
            webbrowser.open('https://www.youtube.com/')

    except sr.UnknownValueError:
        engine.say('Sorry, I could not understand what you said. Please try again.')
        engine.runAndWait()




with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('ask me anything...')
        recordedaudio=recognizer.listen(source)
        command=recognizer.recognize_google(recordedaudio)
        command = command.lower()
        # voice_ass = input("Enter password?")
        wake = "hey google"

        if command != wake:
            engine.say('wrong wake word')
            engine.runAndWait()
            exit()

        while command == wake:
            engine.say(f'hello surya')
            engine.runAndWait()
            cmd()



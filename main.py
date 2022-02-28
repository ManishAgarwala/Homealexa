import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Below line will choose voice type
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        speak("I am home Alexa. how can i help you?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        speak("I am home Alexa how can i help you")
    else:
        speak("Good Evening!")
        speak("I am home Alexa how can i help you")


def takeCommand():
    # TakeCommand function will take voice as input and convert is as string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    bol_output = True
    while bol_output:
        # These are the conditions
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(result)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("www.google.com")
        elif 'open fb' in query:
            speak('opening facebook')
            webbrowser.open("www.fb.com")
        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open("www.fb.com")
        elif 'open github' in query:
            speak('opening github')
            webbrowser.open("www.github.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\uttam\\OneDrive\\Desktop\\music'
            song = os.listdir(music_dir)
            # This line will list the songs in the music folder
            r = random.randint(0, len(song) - 1)
            # This line will generate random values
            os.startfile(os.path.join(music_dir, song[r]))
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {str_time}")
        elif 'open proteus' in query:
            codepath = "C:\\Users\\uttam\\OneDrive\\Desktop\\Proteus 8 Professional.lnk"
            os.startfile(codepath)
        else:
            bol_output = False

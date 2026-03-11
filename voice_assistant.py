
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return "none"

def assistant():
    speak("Hello, I am your voice assistant")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello, how can I help you")

        elif "time" in command:
            import datetime
            time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + time)

        elif "your name" in command:
            speak("I am a python voice assistant")

        elif "exit" in command:
            speak("Goodbye")
            break

assistant()

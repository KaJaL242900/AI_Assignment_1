# Voice Assistant in Python (Simple)

import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Start assistant
print("Voice Assistant Started (type 'bye' to exit)")
speak("Hello, I am your voice assistant")

while True:
    user = input("You: ").lower()

    if user == "hello":
        speak("Hello, how can I help you?")
        
    elif user == "time":
        speak("You can check the system time.")
        
    elif user == "name":
        speak("I am a Python voice assistant.")
        
    elif user == "bye":
        speak("Goodbye! Have a nice day.")
        break
        
    else:
        speak("Sorry, I don't understand.")

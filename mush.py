import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine=pyttsx3.init()
newsapi = "b44fa2ebc6004c42b6a6500d822e4c90"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "today's headlines" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=b44fa2ebc6004c42b6a6500d822e4c90")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
    
            # Extract the titles into a list
            headlines = [article['title'] for article in data['articles']]
    
            # Print the list of headlines
            print(headlines)
            speak(headlines)
    


if __name__=="__main__":
    speak("Initializing Jarvis ..........")

    while True:
    #listen for the wake word jarvis
        recognize = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = recognize.listen(source, timeout=2, phrase_time_limit=1)
            word = recognize.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya i'm listening")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = recognize.listen(source)
                    c = recognize.recognize_google(audio)

                    processCommand(c)

        except Exception as e:
            print("Error; {0}".format(0))

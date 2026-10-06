"""
Virtual ASs
===========

import gtts
from gtts import gTTS
from playsound3 import playsound
#now we will give a text and conver to audio
text="pfs lo ledhu oopu DA ne thoopu"
g=gTTS(text)
#save as audio file(.mp3)
g.save("audio.mp3")
playsound("audio.mp3")
"""

from gtts import gTTS
import subprocess
from playsound3 import playsound 
import speech_recognition as sr
from time import ctime #it returns current line 
import os 
import uuid
import time
import webbrowser
#first we will make out virtual assistant to understand what we speak 
def listen():
    """speechRecognition"""
    # we will make our system to check the microphone as source
    r=sr.Recognizer()
    with sr.Microphone() as source: 
        print("Now you can start talking")
        audio = r.listen(source,phrase_time_limit = 5)
        #what ever we speak lets store in data
        data = ''
        try:
            data=r.recognize_google(audio,language='en-US')
            print("You Said: ",data)
        except sr.UnknownValueError as e:
            print("Make Sure you speak louder")
        except sr.RequestError as e:
            print("No internet connect")
        return data
        #text=gTTS(data)
        #text.save("new.mp3")
        #playsound("new.mp3")
#listen()

# we will create a seperate function for responding back and virtual assistant actions

def responding(String):
    """Responding function to get audio saved and text is spoken back"""
    print(String)
    tts=gTTS(text=String)
    # we will use above audio file and modify the content in it
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# next we will make our virtualassistant to work with given conditions
def va(data):
    """now we will map our conditions"""
    if "hello" in data:
        listening=True
        responding("hey hi ra chinna")
    elif "how are you" in data:
        listening=True
        responding("nenu super!!!!")
    elif "don't talk" in data:
        listening=True
        responding("sarley ra na valleee problem ayithe vellipotha")
    elif "birthday" in data:
        listening=True
        responding("Vishalakshi birthday antaga party ledha")
    elif "open Google" in data:
        listening = True
        url = "https://www.google.com"
        webbrowser.open(url)
        print("Success")
        responding("Done openend")
    elif "Inorbit Mall Visakhapatnam" in data:
            listening = True
            url = "https://www.google.com/maps/search/"+data
            webbrowser.open(url)
            print("Success")
            responding("Done openend")
    elif "Jadal Zamana" in data:
            listening=True
            url="https://www.youtube.com/search"+data
            webbrowser.open(url)
    elif "stop" in data:
        listening=False
    try:
        return listening
    except UnboundLocalError:
        print("Speak properly")
responding("welcome brother")
listening=True
while listening:
    if listening==True:
        data=listen()
        listening=va(data)
    else:
        break
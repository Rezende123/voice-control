# -*- coding: utf-8 -*-

import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import sys

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def animation_load():
    animation = "|/-\\"

    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write("Ouvindo...\r" + animation[i % len(animation)])
        sys.stdout.flush()
    
    print ""

def speak_word(word):
    tts = gTTS(word,lang='pt-br')

    tts.save('assets/speak.mp3')

    playsound('assets/speak.mp3')

def listen_microfone(listenMessage = "Pode falar"):
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        
        clear()
        print(listenMessage)
        animation_load()
        
        audio = microfone.listen(source)
    try:
        
        word = microfone.recognize_google(audio, language='pt-BR')
        word = word.encode('utf8')
        
        print("Você disse: " + word)
        
    except LookupError:
        print("Não entendi")

    return word
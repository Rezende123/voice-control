# -*- coding: utf-8 -*-

import os
import re
import sys
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
sys.path.append('/home/felipe/Workspace/git/voice-control/models/')

import command as commandModule

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def search_command(request):
    for cmd in commandModule.commands:
        if (re.search(cmd.key, request, re.IGNORECASE)):
            os.system(cmd.content)

def speak_word(word):
    tts = gTTS(word,lang='pt-br')

    tts.save('assets/speak.mp3')

    playsound('assets/speak.mp3')

def listen_microfone(listenMessage = "Pode falar"):
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        
        # clear()
        print(listenMessage)
        
        audio = microfone.listen(source)
    try:
        
        word = microfone.recognize_google(audio, language='pt-BR')
        word = word.encode('utf8')
        
        print("Você disse: " + word)
        
    except LookupError:
        print("Não entendi")

    return word

word = listen_microfone()

if (re.search('olá nala', word, re.IGNORECASE)):
    speak_word('Oi, estou aqui para ajudar, basta pedir')
    print("Pode pedir:")
    pedido = listen_microfone()
    search_command(pedido)

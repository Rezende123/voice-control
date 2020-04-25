# -*- coding: utf-8 -*-

import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')

    tts.save('assets/speak.mp3')

    playsound('assets/speak.mp3')

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        
        clear()
        print("Pode falar")
        
        audio = microfone.listen(source)
    try:
        
        frase = microfone.recognize_google(audio, language='pt-BR')
        frase = frase.encode('utf8')
        
        print("Você disse: " + frase)
        
    except LookupError:
        print("Não entendi")

    return frase

frase = ouvir_microfone()

if (frase == 'Olá Nala'):
    cria_audio('Oi, estou aqui para ajudar, basta pedir')
    print("Pode pedir")

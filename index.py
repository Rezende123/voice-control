# -*- coding: utf-8 -*-

import os
import re
import sys

path = os.getcwd()
sys.path.append(path + '/lib/')

import command
import comunication

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

word = comunication.listen_microfone()

if (re.search('olá nala', word, re.IGNORECASE)):
    comunication.speak_word('Oi, estou aqui para ajudar, basta pedir')
    print("Pode pedir:")
    request = comunication.listen_microfone()
    command.search_command(request)

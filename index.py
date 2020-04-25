# -*- coding: utf-8 -*-

import os
import re
import sys

path = os.getcwd()
sys.path.append(path + '/lib/')

import command
import comunication

botName = 'Nala'

word = comunication.listen_microfone()

if (re.search('olá ' + botName, word, re.IGNORECASE)):
    comunication.speak_word('Oi, estou aqui para ajudar, basta pedir')
    request = comunication.listen_microfone('Pode pedir Felipe')
    command.search_command(request)

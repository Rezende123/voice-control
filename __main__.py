# -*- coding: utf-8 -*-

import os
import re
import sys

path = os.getcwd()
sys.path.append(path + '/modules/')

import modules.command as command
import modules.comunication as comunication

bootCommand = 'Botas'
botName = 'Botas'

word = comunication.listen_microfone()

if (re.search(botName, word, re.IGNORECASE)):
    comunication.speak_word('Oi, meu nome é Botas, estou aqui para ajudar, basta pedir')
    request = comunication.listen_microfone('Pode pedir Felipe')
    command.search_command(request)

# -*- coding: utf-8 -*-

import os
import re
import sys

path = os.getcwd()
sys.path.append(path + '/modules/')

import modules.command as command
import modules.comunication as comunication

bootCommand = 'Mensagem'
botName = 'Lexa'

word = comunication.listen_microfone()

if (re.search(bootCommand, word, re.IGNORECASE)):
    comunication.speak_word(f'Oi, meu nome é {botName}, estou aqui para ajudar, basta pedir')
    request = comunication.listen_microfone('Pode pedir Felipe')
    command.search_command(request)

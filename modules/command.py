import re
import os
from fuzzywuzzy import fuzz
import webbrowser
from whatsapp_messages import mandar_mensagem_whatsapp

class command: 
    def __init__(self, key, content):  
        self.key = key  
        self.content = content 

commands = []  
commands.append( command('Abrir Chrome', 'google-chrome') ) 
commands.append( command('Abrir Code', 'code') ) 

def getWords(word):
    return word.split(" ")

def makeParams(words):
    params = ''

    for word in words:
        if (params == ''):
            params = word
        else:
            params = params + '%20' + word
    
    return params

def searchInNavigator(request):
    words = getWords(request.upper())

    if 'BUSCAR' in words:
        words.remove('BUSCAR')
    elif 'PROCURAR' in words:
        words.remove('PROCURAR')

    params = makeParams(words)

    url = "https://www.google.com.tr/search?q={}".format(params)
    webbrowser.open_new_tab(url)

def enviar_mensagem(request):
    mensagem = request.split("mensagem")[1]
    mandar_mensagem_whatsapp(mensagem)

def search_command(request):
    for cmd in commands:
        if (
            re.search('buscar', request, re.IGNORECASE) or
            re.search('procurar', request, re.IGNORECASE)            
            ):
            searchInNavigator(request)
            return
        elif (re.search('mensagem', request, re.IGNORECASE)):
            enviar_mensagem(request)
            return
        elif (fuzz.partial_ratio(cmd.key, request) >= 80):
            os.system(cmd.content)
            return

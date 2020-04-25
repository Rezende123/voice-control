import re
import os
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz

class command: 
    def __init__(self, key, content):  
        self.key = key  
        self.content = content 

commands = []  
commands.append( command('Abrir Chrome', 'google-chrome') ) 
commands.append( command('Abrir Code', 'code') ) 

def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def search_command(request):
    for cmd in commands:
        if (fuzz.partial_ratio(cmd.key, request) > 80):
            os.system(cmd.content)
            return

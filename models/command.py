class command:  
    def __init__(self, key, content):  
        self.key = key  
        self.content = content 

commands = []  
commands.append( command('Abrir Chrome', 'google-chrome') ) 
commands.append( command('Abrir Code', 'code') ) 
# VOICE-CONTROL

Um controle de voz em python, que vai servir para executar comandos no computador a partir da voz. Ele foi criado para se adaptar a várias situações, basta definir as palavras chave e os comandos na página [command.py](./modules/command.py).

## EXECUÇÃO

Para executar basta ir até o diretório do projeto e rodar o comando:
```
python .
```

## BIBLIOTECAS

Utilização das bibliotecas:

- [speech_recognition](https://pypi.org/project/SpeechRecognition/): faz o reconhecimento de voz;
- [gTTS](https://pypi.org/project/gTTS/) e [playsound](https://pypi.org/project/playsound/): fala com o usuário através da voz do google;
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/): busca nas frases ditas os comandos pedidos;
- [webbrowser](https://docs.python.org/2/library/webbrowser.html): faz pesquisa no navegador;
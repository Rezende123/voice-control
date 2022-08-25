import webbrowser
import time
import urllib

def mandar_mensagem_whatsapp(mensagem):
    pessoa = "XXX"
    numero = 234234
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    webbrowser.open_new_tab(link)

    print("ABRIU A CONVERSA")
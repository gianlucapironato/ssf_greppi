# Corso accelerato Python (4 ore)

## I motivi della popolarità
- Linguaggio ad alto livello (vicino a come comunica l'umano) e con sintassi molto semplice
- Linguaggio di scripting (piccoli programmi con l'obiettivo di automatizzare task o procedure altrimenti manuali) che però supporta più paradigmi di programmazione (e quindi ben si presta anche alla realizzazione di programmi veri e propri)
- È multipiattaforma e gode di una vasta disponibilità di librerie (permettendo così la realizzazione di programmi estesi con diverse funzionalità implementate da terzi)

## 1. Ambiente di Sviluppo - REPLIT (15 min)

### 1.1 Introduzione a Replit
- Creazione nuovo progetto Python
- File principale `main.py`
- Struttura base:
```python
# Il classico "Hello World"
print("Hello World!")

# Input dall'utente
nome = input("Come ti chiami? ")
print(f"Ciao {nome}!")
```

## 2. Python Base (90 min)

### 2.1 Sintassi Fondamentale (25 min)
- Notiamo subito due cose: ogni riga ospita una singola istruzione e le istruzioni non terminano con il "punto e virgola"!
```python
# Variabili e tipi di dati
eta = 25                  # int
prezzo = 19.99           # float
nome = "Mario"           # str
is_studente = True       # bool

```
- Python è un linguaggio a tipizzazione dinamica (non si dichiara un tipo per la variabile a compile-time ed è possibile che il suo tipo cambi a run-time)
- Il tipo determina le operazioni che si possono svolgere sulle variabili

```python

# Operatori
somma = 5 + 3            # 8
differenza = 10 - 4      # 6
prodotto = 3 * 2         # 6
divisione = 15 / 3       # 5.0
modulo = 17 % 5          # 2

# Strutture di controllo
if eta >= 18:
    print("Maggiorenne")
else:
    print("Minorenne")

# range() crea una sequenza di numeri
# range(5)    -> 0,1,2,3,4
# range(2,5)  -> 2,3,4
# range(0,10,2) -> 0,2,4,6,8

# Cicli
for i in range(5):  # i assumerà i valori 0,1,2,3,4
    print(i)

# range con start e stop
for i in range(2, 5):  # i assumerà i valori 2,3,4
    print(i)

counter = 0
while counter < 3:
    print(counter)
    counter += 1
```

### 2.2 Strutture Dati Base (30 min)
```python
# Liste
# Liste
numeri = [1, 2, 3, 4, 5]
numeri.append(6)         # [1, 2, 3, 4, 5, 6]
numeri.insert(0, 0)      # [0, 1, 2, 3, 4, 5, 6]
primi_tre = numeri[:3]   # [0, 1, 2]

# Rimozione elementi da liste
numeri.remove(3)         # rimuove il primo '3' trovato: [0, 1, 2, 4, 5, 6]
elemento_rimosso = numeri.pop()  # rimuove e restituisce l'ultimo elemento (6)
elemento_pos = numeri.pop(1)     # rimuove e restituisce l'elemento in posizione 1 (1)
del numeri[0]           # rimuove l'elemento in posizione 0 (0)

# Iterazione su lista
for numero in numeri:    # numero assume ogni valore della lista
    print(numero)

# Iterazione con indice
for i in range(len(numeri)):  # i assume i valori da 0 a len(numeri)-1
    print(f"Posizione {i}: {numeri[i]}")

# Stringhe
nome = "Python"
lunghezza = len(nome)    # 6
maiuscolo = nome.upper() # "PYTHON"
frase = "ciao,mondo"
parole = frase.split(",")# ["ciao", "mondo"]
nuova = ",".join(parole) # "ciao,mondo"
```

### 2.3 Funzioni (35 min)
```python
# Funzione base
def saluta(nome):
    return f"Ciao {nome}!"

# Chiamate della funzione saluta
messaggio1 = saluta("Mario")    # "Ciao Mario!"
messaggio2 = saluta("Luigi")    # "Ciao Luigi!"
print(messaggio1)
print(messaggio2)

# Funzione con parametri di default
def calcola_sconto(prezzo, percentuale=10):
    sconto = prezzo * (percentuale / 100)
    return prezzo - sconto

# Chiamate di calcola_sconto con e senza parametro opzionale
prezzo1 = calcola_sconto(100)           # usa sconto default 10%: ritorna 90.0
prezzo2 = calcola_sconto(100, 20)       # sconto del 20%: ritorna 80.0
prezzo3 = calcola_sconto(50)            # sconto default su 50: ritorna 45.0
print(prezzo1)
print(prezzo2)
print(prezzo3)

# Funzione che opera su liste
def media_voti(voti):
    somma = sum(voti)
    return somma / len(voti)

# Chiamate con liste diverse
voti_mario = [6, 7, 8, 7]
voti_luigi = [8, 8, 7, 9]
media1 = media_voti(voti_mario)    # ritorna 7.0
media2 = media_voti(voti_luigi)    # ritorna 8.0
print(f"Media Mario: {media1}")
print(f"Media Luigi: {media2}")

# Esempio di scope
x = 10  # variabile globale
def test_scope():
    x = 5  # variabile locale
    print(f"X locale: {x}")  # stampa 5

test_scope()
print(f"X globale: {x}")     # stampa 10
```

## 3. Python Avanzato (105 min)

### 3.1 Dizionari (40 min)
```python
# Dizionari
# Creazione e manipolazione
studente = {
    "nome": "Mario",
    "età": 20,
    "corsi": ["Python", "Java"]
}

# Accesso e modifica
print(studente["nome"])      # Mario
studente["età"] = 21
studente["email"] = "mario@example.com"  # aggiunge nuovo campo

# Rimozione elementi da dizionari
del studente["email"]        # rimuove la chiave "email" e il suo valore
età_rimossa = studente.pop("età")  # rimuove e restituisce il valore della chiave "età"
ultimo_elemento = studente.popitem()  # rimuove e restituisce l'ultima coppia chiave-valore come tupla
studente.clear()            # rimuove tutti gli elementi dal dizionario

# Metodi utili
chiavi = studente.keys()     # dict_keys: vista delle chiavi
valori = studente.values()   # dict_values: vista dei valori

# Iterazione su chiavi e valori
for chiave, valore in studente.items():  # items() restituisce coppie chiave-valore
    print(f"{chiave}: {valore}")

# Verifica esistenza chiave
if "nome" in studente:  # verifica se esiste la chiave
    print("Nome trovato:", studente["nome"])
```

### 3.2 Gestione File (35 min)
```python
# Scrittura su file
file = open("dati.txt", "w")
file.write("Prima riga\n")
file.write("Seconda riga\n")
file.close()

# Lettura da file
file = open("dati.txt", "r")
contenuto = file.read()
file.close()
    
# Lettura riga per riga
file = open("dati.txt", "r")
for riga in file:
    print(riga.strip())
file.close()

# Gestione eccezioni base
try:
    file = open("file_non_esistente.txt", "r")
    contenuto = file.read()
    file.close()
except FileNotFoundError:
    print("File non trovato!")
```

### 3.3 Progetto Pratico (30 min)
```python
# Gestore contatti semplice
def carica_contatti(filename):
    contatti = {}
    try:
        file = open(filename, "r")
        for line in file:
            nome, tel = line.strip().split(",")
            contatti[nome] = tel
        file.close()
    except FileNotFoundError:
        pass
    return contatti

def salva_contatti(filename, contatti):
    file = open(filename, "w")
    for nome, tel in contatti.items():
        file.write(f"{nome},{tel}\n")
    file.close()

def aggiungi_contatto(contatti, nome, telefono):
    contatti[nome] = telefono
    return contatti

def cerca_contatto(contatti, nome):
    return contatti.get(nome, "Non trovato")

# Uso
contatti = carica_contatti("contatti.txt")
contatti = aggiungi_contatto(contatti, "Mario", "123456789")
print(cerca_contatto(contatti, "Mario"))
salva_contatti("contatti.txt", contatti)
```

## 4. Wrap-up e Q&A (30 min)

### Mini-esercizio di verifica
```python
# Esercizio: Creare funzioni per:
# 1. Leggere un file di numeri
# 2. Calcolare media e somma
# 3. Salvare i risultati in un nuovo file

def leggi_numeri(nome_file):
    file = open(nome_file, "r")
    contenuto = file.read()
    file.close()
    return [float(x) for x in contenuto.split()]

def calcola_statistiche(numeri):
    media = sum(numeri) / len(numeri)
    somma = sum(numeri)
    return media, somma

def salva_risultati(nome_file, media, somma):
    file = open(nome_file, "w")
    file.write(f"Somma: {somma}\n")
    file.write(f"Media: {media}\n")
    file.close()

# Uso
numeri = leggi_numeri("input.txt")
media, somma = calcola_statistiche(numeri)
salva_risultati("output.txt", media, somma)
```

### Note per il Docente
- Ogni esempio dovrebbe essere testato live
- Incoraggiare gli studenti a modificare il codice
- Proporre piccole sfide durante la lezione
- Mantenere il codice visibile durante le spiegazioni

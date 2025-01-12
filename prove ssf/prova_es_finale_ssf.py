def carica_contatti(contatti, nome_file):
    try:
        f=open(nome_file, "r")
        for line in f:
            nome, numero = line.strip().split(",")
            contatti[nome] = numero
        print("Contatti caricati")
    except FileNotFoundError:
        print("File non trovato")

def salva_contatti(contatti, nome_file):
    try:
        f=open(nome_file, "w")
        for nome in contatti:
            f.write(nome + "," + contatti[nome] + "\n")
        print("Contatti salvati")
    except FileNotFoundError:
        print("File non trovato")

def vedi_numero(contatti, nome):
    if nome in contatti:
        print("Il numero di", nome, "è", contatti[nome])
    else:
        print("Contatto non trovato")

def aggiungi_contatto(contatti, nome, numero):
    contatti[nome] = numero
    print("Contatto aggiunto")

def main():
    NOME_FILE = "contatti.txt"
    contatti = {}
    print("Benvenuto/a\n1. carica contatti\n2. salva contatti\n3. vedi numero\n4. aggiungi contatto\n5. esci")
    s = int(input("Digita la tua scelta:"))
    while s!=5:
        if s==1:
            carica_contatti(contatti, NOME_FILE)
        elif s==2:
            salva_contatti(contatti, NOME_FILE)
        elif s==3:
            nome = input("Inserisci il nome del contatto da cercare:")
            vedi_numero(contatti, nome)
        elif s==4:
            nome = input("Inserisci il nome del contatto da aggiungere:")
            numero = input("Inserisci il numero del contatto da aggiungere:")
            aggiungi_contatto(contatti, nome, numero)
        else:
            print("Scelta non valida")
        print("Benvenuto/a\n1. carica contatti\n2. salva contatti\n3. vedi numero\n4. aggiungi contatto\n5. esci")
        s = int(input("Digita la tua scelta:"))

# avvio exec main
main()
def main():
  d = {}
  NFILE = "contatti.txt"
  print("Benvenuto!\n1.carica contatti\n2.salva contatti\n3.vedi numero\n4.aggiungi contatto\n5.esci")
  s = int(input("Digita la scelta: "))
  while s != 5:
    if s == 1:
      carica_contatti(NFILE, d)
    elif s == 2:
      salva_contatti(NFILE, d)
    elif s == 3:
      nome = input("Di chi vuoi vedere il numero?")
      vedi_numero(nome, d)
    elif s == 4:
      nome = input("Come si chiama il nuovo contatto?")
      numero = input("Qual è il suo numero?")
      aggiungi_contatto(nome, numero, d)
    elif s == 5:
      print("Arrivederci")
    else:
      print("Scelta non valida")
    print("1.carica contatti\n2.salva contatti\n3.vedi numero\n4.aggiungi contatto\n5.esci")
    s = int(input("Digita la scelta: "))

def carica_contatti(nfile, d):
  f = open(nfile, "r")
  for r in f:
    temp = r.split(",")
    d[temp[0]] = temp[1]
  f.close()

def salva_contatti(nfile, d):
  f = open(nfile, "w")
  for nome,numero in d.items():
    f.write(nome + "," + numero + "\n")
  f.close()

def vedi_numero(nome, d):
  print(d.get(nome, "Contatto non trovato"))

def aggiungi_contatto(nome, numero, d):
  d[nome] = numero
  
main()

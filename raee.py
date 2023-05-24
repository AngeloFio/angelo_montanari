import os
def creazione_file1():
    for i in range(5):
        file = open(f"file{i+1}.txt","w")


lista1 = ["frigorifero","congelatori", "apparecchi", "condizionatori", "radiatori", "asciugatrici","altre apparecchiature"]
lista2 = ["lavatrici", "lavastoviglie","apparecchi di cottura"]
lista3 = ["televisori", "schermi", "monitor", "cornici digitali LCD","Notebook"]
lista4 = ["stampanti", "aspirapolvere","cellulari", "frullatore", "macchina per cucire"]
lista5 = ["lampade fluorescenti", "tubi", "led"]



def smistamento():
    print("Inserisci il gruppo di rifiuto tra questi: ")
    print("1--> Grande Bianco Freddo;")
    print("2--> Grande Bianco NON freddo")
    print("3 --> TV monitor")
    print("4 --> Elettronica di consumo")
    print("5 --> Sorgenti luminose a scarica")
    print()

    rifiuto = input()
    match rifiuto:
        case "1":
            
            controllo1()
        case "2":
           
            controllo2()
        case "3":
            
            controllo3()
        case "4":
            
            controllo4()
        case "5":
            
            controllo5()

def controllo1():
    os.system("cls")
    print(f"Ecco I rifiuti di questa opzione: {lista1}")
    file1 = open("file1.txt","a")
    oggetto = input("Inserisci l'oggetto:  ")
    while oggetto not in lista1:
        oggetto = input("Rinserisci il rifiuto: ")
    
    print("oggetto corretto")
    file1.write(f"Hai inserito il rifiuto:{oggetto} \n")
def controllo2():
    os.system("cls")
    print(f"Ecco I rifiuti di questa opzione: {lista2}")
    file2 = open("file2.txt","a")
    oggetto = input("Inserisci l'oggetto:  ")
    while oggetto not in lista2:
        oggetto = input("Rinserisci il rifiuto: ")
    
    print("oggetto corretto")
    file2.write(f"Hai inserito il rifiuto:{oggetto} \n")
def controllo3():
    os.system("cls")
    print(f"Ecco I rifiuti di questa opzione: {lista3}")
    file3 = open("file3.txt","a")
    oggetto = input("Inserisci l'oggetto:  ")
    while oggetto not in lista3:
        oggetto = input("Rinserisci il rifiuto: ")
    
    print("oggetto corretto")
    file3.write(f"Hai inserito il rifiuto:{oggetto} \n")
def controllo4():
    os.system("cls")
    print(f"Ecco I rifiuti di questa opzione: {lista4}")
    file4 = open("file4.txt","a")
    oggetto = input("Inserisci l'oggetto:  ")
    while oggetto not in lista4:
        oggetto = input("Rinserisci il rifiuto: ")
    
    print("oggetto corretto")
    file4.write(f"Hai inserito il rifiuto:{oggetto} \n")
    

def controllo5():
    os.system("cls")
    print(f"Ecco I rifiuti di questa opzione: {lista5}")
    file5 = open("file5.txt","a")
    oggetto = input("Inserisci l'oggetto:  ")
    while oggetto not in lista5:
        oggetto = input("Rinserisci il rifiuto: ")
    
    print("oggetto corretto")
    file5.write(f"Hai inserito il rifiuto:{oggetto} \n")

creazione_file1()
while True:
    smistamento()   
    print("Inserisci: ",
          "SI ---> se vuoi continuare",
          "NO ---> se vuoi interrompere il programma")
    smetti = input()
    smetti = smetti.lower()
    if smetti == "no":
        print("--------------------------------------",
              "\n ---> HAI TERMINATO IL PROGRAMMA <---",
              "\n--------------------------------------")
        break



#####################################################################################################################################

# -*- coding: utf-8 -*-

import csv
import pandas as pd 
import sys
import webbrowser
import time

caractere=["IP"]#texte à rechercher


print("Démmarage du programme")

with open("Fichier_a_traiter.txt", 'r') as fichier: #ouverture du fichier
   with open("Fichier_a_traiter2.txt", "w") as file: #ouverture du 2nd fichier
    lignes = fichier.readlines()

   


    for ligne in lignes:
        for caracteres in caractere:
            if caracteres in ligne:
                     #print(ligne) Affiche les lignes
                     file.write(ligne) #Creer un nouveau fichier et insere variables lignes
file.close() #Fermer le fichier creer 

with open("Fichier_a_traiter2.txt", 'r') as data: #réouvre le fichier creer sous un autre nom
    lignee= data.readlines()
f=open('Fichier_a_traiter2.txt','r')
chaine=f.read().replace('IP',';')
f.close()
f=open('Fichier_a_traiter2.txt','w')
f.write(chaine)
f.close()
f=open('Fichier_a_traiter2.txt','r')
chaine=f.read().replace('>',';')
f.close()
f=open('Fichier_a_traiter2.txt','w')
f.write(chaine)
f.close()
f=open('Fichier_a_traiter2.txt','r')
chaine=f.read().replace(',',';')
f.close()
f=open('Fichier_a_traiter2.txt','w')
f.write(chaine)
f.close()
f=open('Fichier_a_traiter2.txt','r')
chaine=f.read().replace('http:',';')
f.close()
f=open('Fichier_a_traiter2.txt','w')
f.write(chaine)
f.close()
data.close()

print("Création du Fichier_a_traiter2.txt")
#remplace les chaines de caractere choisit
with open('Fichier_a_traiter.csv','w') as fichiercsv:
    with open("Fichier_a_traiter2.txt", 'r') as data:
                 writer=csv.writer(fichiercsv)
                 writer.writerow(['HEURES ;IP SOURCE ;IP DESTINATION;FLAG;SEQUENCE;ACK/WIN; PROTOCOLE'])
                 writer.writerow(data)
                 print("Creation du cvs + trie")
                 
compteurligne = 0 
for row in open("Fichier_a_traiter.csv"):
    compteurligne+=1
    print("Nombres de ligne dans le fichier csv: - ", compteurligne)
    





  

time.sleep(32)
webbrowser.open_new_tab("triefinal.htm")
print("Fichier HTML créer")



                
                 
data.close()
print("Fin du programme")

    

   
    #print(lignee) Les lignes du Fichier_a_traiter2.txt

   
        
    #for line in range(0):
        #trame_split
    

        
     
    

    
                     


              


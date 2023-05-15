# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:44:40 2020

@author: Mr ABBAS-TURKI
"""
import random
import sys
sys.setrecursionlimit(1000000) #pour augmenter la limite de récursion

import hashlib
import binascii
import math


def home_mod_expnoent(x, y, n):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % n
        x = (x * x) % n
        y = y // 2
    return result

def home_ext_euclide(y,b): #algorithme d'euclide étendu pour la recherche de l'exposant secret
    if y==0: #si y=0 alors pgcd(b,0)=b et x=0 et y=1
        return b,0,1
    else: #sinon
        pgcd,x1,y1 = home_ext_euclide(b%y, y) #on applique l'algorithme d'euclide étendu à b%y et y
        x = y1 - (b//y) * x1 #on détermine x
        y = x1 #on détermine y
        return pgcd,x,y #on renvoie le pgcd, x et y    

     

def home_pgcd(a,b): #recherche du pgcd
    if(b==0): 
        return a 
    else: 
        return home_pgcd(b,a%b)

def home_string_to_int(x): # pour transformer un string en int
    z=0
    for i in reversed(range(len(x))):
        z=int(ord(x[i]))*pow(2,(8*i))+z
    return(z)


def home_int_to_string(x): # pour transformer un int en string
    txt=''
    res1=x
    while res1>0:
        res=res1%(pow(2,8))
        res1=(res1-res)//(pow(2,8))
        txt=txt+chr(res)
    return txt




def mot10char(): #entrer le secret
    secret=input("donner un secret ")
    return(secret)


#voici les éléments de la clé d'Alice
x1a=2507664037768206267142049874749912596696721705624614311043871638159594081658948017417517063175564773#p
x2a=9064535093468660039337794947273231252030184947112929047213791821593413585569214521502191998829419019#q
na=x1a*x2a  #n
phia=((x1a-1)*(x2a-1))//home_pgcd(x1a-1,x2a-1)
ea=65537 #exposant public
da=home_ext_euclide(phia,ea)[2] #exposant privé
#voici les éléments de la clé de bob
x1b=4626087618515902129396159758366441481444149960492184487788073913336907230583559790861246102949019369#p
x2b=1729638451894761439089347408461929402070175450059461011582895257173896628171384529155045116195674491 #q
nb=x1b*x2b # n
phib=((x1b-1)*(x2b-1))//home_pgcd(x1b-1,x2b-1)
eb=65537 # exposants public
db=home_ext_euclide(phib,eb)[2] #exposant privé




print("Vous êtes Bob, vous souhaitez envoyer un secret à Alice")
print("voici votre clé publique que tout le monde a le droit de consulter")
print("n =",nb)
print("exposant :",eb)
print("voici votre précieux secret")
print("d =",db)
print("*******************************************************************")
print("Voici aussi la clé publique d'Alice que tout le monde peut conslter")
print("n =",na)
print("exposent :",ea)
print("*******************************************************************")
print("il est temps de lui envoyer votre secret ")
print("*******************************************************************")
x=input("appuyer sur entrer")
secret=mot10char()
print("*******************************************************************")
print("voici la version en nombre décimal de ",secret," : ")
num_sec=home_string_to_int(secret)
print(num_sec)
print("voici le message chiffré avec la publique d'Alice : ")
chif=home_mod_expnoent(num_sec, ea, na)
print(chif)
print("*******************************************************************")
print("On utilise la fonction de hashage 256 pour obtenir le hash du message",secret)
Bhachis0=hashlib.sha256(secret.encode(encoding='UTF-8',errors='strict')).digest() #SHA-256 du message
print("voici le hash en nombre décimal ")
Bhachis1=binascii.b2a_uu(Bhachis0)
Bhachis2=Bhachis1.decode() #en string
Bhachis3=home_string_to_int(Bhachis2)
#Bhachis3 = int.from_bytes(Bhachis0, byteorder='big')
print(Bhachis3)
print("voici la signature avec la clé privée de Bob du hachis")
signe=home_mod_expnoent(Bhachis3, db, nb)
print(signe)
print("*******************************************************************")
print("Bob envoie \n \t 1-le message chiffré avec la clé public d'Alice \n",chif,"\n \t 2-et le hash signé \n",signe)
print("*******************************************************************")
x=input("appuyer sur entrer")
print("*******************************************************************")
print("Alice déchiffre le message chiffré \n",chif,"\nce qui donne ")
dechif=home_int_to_string(home_mod_expnoent(chif, da, na))
print(dechif)
print("*******************************************************************")
print("Alice déchiffre la signature de Bob \n",signe,"\n ce qui donne  en décimal")
designe=home_mod_expnoent(signe, eb, nb)
print(designe)
print("Alice vérifie si elle obtient la même chose avec le hash de ",dechif)
Ahachis0=hashlib.sha256(dechif.encode(encoding='UTF-8',errors='strict')).digest()
Ahachis1=binascii.b2a_uu(Ahachis0)
Ahachis2=Ahachis1.decode()
Ahachis3=home_string_to_int(Ahachis2)
#Ahachis3 = int.from_bytes(Ahachis0, byteorder='big')
print(Ahachis3)
print("La différence =",Ahachis3-designe)
if (Ahachis3-designe==0):
    print("Alice : Bob m'a envoyé : ",dechif)
else:
    print("oups")
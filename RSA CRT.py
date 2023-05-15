# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:44:40 2020

@author: Mr ABBAS-TURKI
"""
import random
import sys
#sys.setrecursionlimit(1000000) #pour augmenter la limite de récursion

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



def generate_large_prime():
    while True:
        p = random.getrandbits(1024)
        if is_prime(p):
            return p

def is_prime(n, k=5):
    if n <= 3:
        return n == 2 or n == 3
    for i in range(k):
        a = random.randint(2, n-2)
        x = pow(a, n-1, n)
        if x != 1:
            return False
    return True


def mot10char(): #entrer le secret
    secret=input("donner un secret ")
    return(secret)

def home_mod_inv(a, n):
    """
    Computes the modular inverse of a modulo n.
    Assumes that a and n are coprime.
    """
    t, newt = 0, 1
    r, newr = n, a

    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr

    if r > 1:
        raise ValueError("a is not invertible")
    if t < 0:
        t = t + n

    return t

#voici les éléments de la clé d'Alice
#x1a=2507664037768206267142049874749912596696721705624614311043871638159594081658948017417517063175564773#p
#x2a=9064535093468660039337794947273231252030184947112929047213791821593413585569214521502191998829419019#q
x1a=generate_large_prime()#p
x2a=generate_large_prime()#q
print(x1a)
print(x2a)
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


# Compute CRT Alice parameters
dp = da % (x2a - 1)
dq = da % (x1a - 1)
qinv = home_mod_inv(x1a, x2a)
print(qinv*x1a%x2a)

# Compute CRT Bob parameters
dp2 = db % (x1b - 1)
dq2 = db % (x2b - 1)
qinv2 = home_mod_inv(x2b, x1b)
print(qinv2*x2b%x1b)

print("Vous êtes Bob, vous souhaitez envoyer un secret à Alice")
print("voici votre clé publique que tout le monde a le droit de consulter")
print("n =", nb)
print("exposant :", eb)
print("voici votre précieux secret")
print("d =", db)
print("*******************************************************************")
print("Voici aussi la clé publique d'Alice que tout le monde peut consulter")
print("n =", na)
print("exposent :", ea)
print("*******************************************************************")
print("il est temps de lui envoyer votre secret ")
print("*******************************************************************")
x = input("appuyer sur entrer")
secret = mot10char()
print("*******************************************************************")
print("voici la version en nombre décimal de ", secret, " : ")
num_sec = home_string_to_int(secret)
print(num_sec)
print("voici le message chiffré avec la publique d'Alice : ")
chif = home_mod_expnoent(num_sec, ea, na)
print(chif)
print("*******************************************************************")
print("On utilise la fonction de hashage SHA256 pour obtenir le hash du message", secret)
Bhachis0 = hashlib.sha256(secret.encode(encoding='UTF-8', errors='strict')).digest()  # SHA-256 du message
print("voici le hash en nombre décimal ")
Bhachis1 = binascii.b2a_uu(Bhachis0)
Bhachis2 = Bhachis1.decode()  # en string
Bhachis3 = home_string_to_int(Bhachis2)
# Bhachis3 = int.from_bytes(Bhachis0, byteorder='big')
print(Bhachis3)
print("voici la signature avec la clé privée de Bob du hachis")
#Create signature with the normal thing
signe = home_mod_expnoent(Bhachis3, db, nb)
print(signe)
#Create signature with CRT using Bob's private key
vp = home_mod_expnoent(Bhachis3, dp2, x1b)
vq = home_mod_expnoent(Bhachis3, dq2, x2b)
u = (qinv2 * (vp - vq)) % x1b
r = (vq + u * x2b) % nb
signe = r
print(signe)
print("*******************************************************************")
print("Bob envoie \n \t 1-le message chiffré avec la clé public d'Alice \n", chif, "\n \t 2-et le hash signé \n", signe)
print("*******************************************************************")
x = input("appuyer sur entrer")
print("*******************************************************************")
print("Alice déchiffre le message chiffré \n", chif, "\nce qui donne ")
# Decrypt using CRT
vp = home_mod_expnoent(chif, dp, x2a)
vq = home_mod_expnoent(chif, dq, x1a)
u = (qinv * (vp - vq)) % x1a
r = (vq + u * x1a) % nb
dechif = home_int_to_string(r)
print(dechif)
print("*******************************************************************")
print("Alice déchiffre la signature de Bob \n",signe,"\n ce qui donne  en décimal")
designe=home_mod_expnoent(signe, eb, nb)
print(designe)
print("*******************************************************************")
print("Alice vérifie le hash du message déchiffré \n", dechif)
Ahash0 = hashlib.sha256(dechif.encode(encoding='UTF-8', errors='strict')).digest()  # SHA-256 du message
Ahash1 = binascii.b2a_uu(Ahash0)
Ahash2 = Ahash1.decode()  # en string
Ahash3 = home_string_to_int(Ahash2)
# Ahash3 = int.from_bytes(Ahash0, byteorder='big')
print("ce qui donne en décimal")
print(Ahash3)
print("*******************************************************************")
print("Alice vérifie que le hash du message déchiffré est égal au hash de la signature")
if Ahash3 == designe:
    print("le message est authentique")
else:
    print("le message n'est pas authentique")


#**********************************************************************************************************************
#**********************************************************************************************************************
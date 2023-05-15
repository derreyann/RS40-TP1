import hashlib
import binascii

def home_mod_expnoent(x,y,n): #exponentiation modulaire
    if y==0: #si y=0
        return 1 #on retourne 1
    else:
        res=home_mod_expnoent(x,y//2,n) #sinon on appelle la fonction avec y/2
        if y%2==0: #si y est pair
            return (res*res)%n #on retourne le carré de res modulo n
        else:
            return (x*res*res)%n #sinon on retourne x fois le carré de res modulo n
     

print (home_mod_expnoent(2,3,5))

#check with the pow function

print(pow(2,3,5))

# more tests

print (home_mod_expnoent(2,3,7))
print(pow(2,3,7))

print (home_mod_expnoent(2,3,8))
print(pow(2,3,8))

print (home_mod_expnoent(2,3,9))
print(pow(2,3,9))

def home_ext_euclide(y,b): #algorithme d'euclide étendu pour la recherche de l'exposant secret
    if y==0:
        return b,0,1
    else:
        pgcd,x1,y1 = home_ext_euclide(b%y, y)
        x = y1 - (b//y) * x1
        y = x1
        return pgcd,x,y

    

print (home_ext_euclide(137,131))


# Python program to demonstrate working of extended
# Euclidean Algorithm
     
# function for extended Euclidean Algorithm
def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y
     
 
# Driver code
a, b = 137,131
g, x, y = gcdExtended(a, b)
print("gcd(", a , "," , b, ") = ", g, x, y)


def home_mod_expnoent(x,y,n): #exponentiation modulaire
    if y==0: #si y=0
        return 1 #on retourne 1
    else:
        res=home_mod_expnoent(x,y//2,n) #sinon on appelle la fonction avec y/2
        if y%2==0: #si y est pair
            return (res*res)%n #on retourne le carré de res modulo n
        else:
            return (x*res*res)%n #sinon on retourne x fois le carré de res modulo n
     
print (home_mod_expnoent(2,3,5))

#check with the pow function

print(pow(2,3,5))
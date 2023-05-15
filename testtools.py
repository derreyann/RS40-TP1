import array


def askchar(): #pour demander un caractère et le transformer en entier

    x=input("donner un caractère ")

    return(ord(x))


def addition(a,b): #addition binaire a+b

    return(a^b)

def multiple (a,b): #multiplication binaire a*b

    res=0 #initialsation du résultat

    c=a #initialsation de la multiplication

    bb=b #initialisation de y

    for i in range(8):

        if ((bb % 2)==1):res^=c

        c=twotimes(c)

        bb=bb//2

    return(res)

def twotimes(a): #multiplication par 2

    if (a<128):
        
        return(a*2)

    else:
        
        return((a-128)*2^27)

def inverse(a):

    t=0
    newt=1
    r=poly_AES

    newr=a

    while newr>1:
        
        quotient=division_e(r,newr)[0]

        t,newt=newt,t^(multiple(quotient,newt))
        p=r^(multiple(quotient,newr))
        r,newr=newr,division_e(r,newr)[1]
        print(p,newr)
    return(newt)


def deg(a): # calcul du degré du polynôme

    aa=a

    res=0

    while (int(int(aa)/2)>0):

        aa=int(aa/2)

        res+=1

    return (res)

 
def division_e(a,b): #div euclidienne a/b en donnant le quotient de la division et le reste

    #!!!!! attention il ne s'agit pas de de l'inverse

    aa=a

    degb=deg(b)

    divis=array.array('B',2*[00000000])

    while deg(aa)>=degb:

        divis[0]=divis[0]^(2**(deg(aa)-degb))

        aa=aa^((2**(deg(aa)-degb))*b)

    divis[1]=aa


    return divis

def multiple(a,b): # multiplication a*b

    res=0 #initialsation du résultat 

    c=a #initialsation de la multiplication 

    bb=b #initialisation de y

    for i in range(8):

        if ((bb % 2)==1):res^=c 

        c=twotimes(c)

        bb=bb//2


    return(res)


poly_AES=283 #Polynôme irreductible d'AES x^8+x^4+x^3+x+1=256+16+8+2+1


xx=array.array('B',5*[00000000])

 

for i in range(2):

    xx[i]=askchar()

    print("voici en valeur entière ",xx[i], " en binaire ",bin(xx[i])) 

 

xx[2]=addition(xx[0],xx[1])

print("le résultat de l'addition ",xx[2]," et en caractère ça donne ", chr(xx[2]))

xx[3]=multiple(xx[0],xx[1])

print("le résultat de la multiplication ",bin(xx[3])," et en caractère ça donne ", chr(xx[3]))

xx[4]=multiple(xx[0],inverse(xx[1]))

print("le résultat de la division de ",chr(xx[0])," / ",chr(xx[1])," = ",chr(xx[4]),", ce qui fait en binaire ", bin(xx[4]))


print("pour vérifier voici le résultat de ",bin(xx[0])," / ",bin(xx[0])," = ",bin(multiple(xx[0],inverse(xx[0]))))

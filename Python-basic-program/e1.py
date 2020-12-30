'''for i in range(10):
    for j in range(i):
        print ("*", end=" ")
    print ()'''

'''for i in range(10):
    for j in range(i,10):
         print ("*", end=" ")
    print ()'''

'''for i in range(10,0,-1):
    print (" "*i, "*"*(10-i))'''

'''for i in range(10):
    print (" "*(10-i),"*"*(2*i-1))'''

'''a=int (input("enter a"))
print(a)'''

'''for a in range(1,100):
    i=1
    count=0
    while(i<=a):
        if a%i==0:
            count=count+1
        i=i+1
    if count==2:
            print(a, end=" ")


for i in range(10):
    for j in range(i):
        print ()'''

'''from math import floor

def prime(a):
    i=1
    count=0
    while(i<=a):
        if(a%i==0):
            count=count+1
        i=i+1

    if(count==2):
        
        return 1
    else:
        return 0

def rev(a):
    rev=0
    while(a>0):
        ld=a%10
        rev=(rev*10)+ld
        a=floor(a/10)
        
    return rev

for i in range(10,1000):
    n=rev(i)
    if(prime(i)==1 and prime(n)==1):
        print(i, end=" ")    '''

'''from math import floor

def niven(n):
    sum=0
    while(n>0):
        ld=n%10
        sum=sum+ld
        n=floor(n/10)

    return sum

for i in range(10,1000):
    a=niven(i)
    if(i%a==0):
        print(i, end=" ")'''
'''for i in range(100):
    print(i*(i+1), end=" ")'''

'''import math

def disarm(a):
    len=0
    n=a
    while(n>0):
        ld=n%10
        len=len+1
        n=math.floor(n/10)

    no=a 
    sum=0
    while(a>0):
        ld=a%10
        sum =sum +math.pow(ld,len)
        a=math.floor(a/10)
        len=len-1

    if(no==sum):
        return 1


for j in range (100000):
    if(disarm(j)==1):
        print(j, end=" ")'''

'''import math

def auto(a):
    sq=a*a

    n=a
    no=0
    ans=1
    while(n>0):
        ld=sq%10
        n_ld=n%10
        if(n_ld!=ld):
            ans=0
            break
        
        sq=math.floor(sq/10)
        n=math.floor(n/10)

    if(ans==1):
        return 1
    else:
        return 0

for b in range (1000):
    if (auto(b)==1):
        print(b, end=" ")'''
import math

def duck(a):
    n=a
    while(n>0):
        ld=n%10
        if(ld==0):
            return 1
        n=math.floor(n/10)

    return 0

for i in range (1,10000):
    if(duck(i)==1):
        print(i, end=" ")
    
    
            

#geometry calculator
#submitted by banshita

def menu() :
    print("Geometry Calculator")
    print("1. Calculate the Area of a Circle")
    print("2. Calculate the Area of a Square")
    print("3. Calculate the Area of a Triangle")
    print("4. Quit")
    return int(input())
def negCheck(no):
    if(no<0):
        print("Negative value are not allowed")
        return False
    return True
def cricle():
    r = float(input("Enter Radius"))
    if (negCheck(r)):
        print(3.14159 * r * r)
    else:
        cricle()

def square():
    s = float(input("Enter the side of Square"))
    if (negCheck(s)):
        print(s * s)
    else:
        square()

def triangle():
    base = float(input("Enter base :"))
    height = float(input("Enter height"))
    if(negCheck(base) and negCheck(height)):
        print(base * height * 0.5)
    else:
        triangle()

no=menu()
while(no!=4):
    if(no==1):
        cricle()
    elif(no==2):
        square()
    elif(no==3):
        triangle()
    elif(no==4):
        break
    else:
        print("Invalid Input")
    no=menu()



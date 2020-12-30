#print pattern
#submitted by banshita

no = int(input("Enter a value between 1 -15 : "))

for i in range(1,no+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
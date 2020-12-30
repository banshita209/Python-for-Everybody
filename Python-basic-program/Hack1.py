#print roman number
#submitted by banshita

no=int(input("Enter a number"))
print("Roman no from ",no," to 10")
roman={ 1 : "I" , 5:"V" , 10:"X" }
flag=True
ro= ""
for i in range(no,11) :
    if(i in roman.keys()):
        print(roman[i])
    else :
        if(i <4):
            ro=""1
            for j in range(1,i+1) :
                ro=ro+"I"
            print(ro)
        elif i == 4:
            print("IV")
        elif (i > 5 and i < 9) :
            ro="V"
            for j in range(1,i-4):
                ro=ro+"I"
            print(ro)
        elif i == 9:
            print("IX")
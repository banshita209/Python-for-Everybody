#program to find the number of days between 2 months
#written by Banshita

def leapOrnot(year):                    #To find the leap year
    if(year%100==0):
        if(year%400):
            return True
    else:
        if(year%4==0):
            return True
    return False

mon1=int(input("Enter month 1 : "))
mon2=int(input("Enter month 2 : "))
year=int(input("Enter year : "))

total_days =0
if((mon1>0 and mon2<13) and mon2 > mon1):

    for i in range(mon1, mon2+1):
        if(i<8):                             #for months jan to july
            if(i%2==0):
                if(i==2):
                    if(leapOrnot(year)):
                        total_days+=29
                    else:
                        total_days+=28
                    continue
                total_days+=30
            else:
                total_days+=31
        else:                           #for months aug to dec
            if(i%2==0):
                total_days+=31
            else:
                total_days+=30
    print(total_days," days")
else:
    print("Please enter proper months i.e 1-12 and mon1 < mon2")
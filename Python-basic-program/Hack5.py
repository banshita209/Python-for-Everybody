#print distance travled
#submitted by banshita

speed= int(input("Speed in (miles per hour)"))
hrs=int(input("Time Tarveled ()hours"))

print("Hours \t Distance Traveled")
print("-----------------------------")
for i in range(1,hrs+1):
    print(i," \t ",(speed*i))
#find the 1st 2nd and 3rd postion between three runner
#submited by : Banshita

def getUser(userList):
    name=input("Enter your Name : ")
    time=int(input("Time took to complete the race (in sec) : "))
    if(time<0):
        print("Please enter postive number only")
        getUser(userList)
    else:
        userList[name]=time
    return userList

runners=dict()

for i in range(0,3):
    runners=getUser(runners)

winner=list()
user=list();

for key in runners.keys():
    user.append(key)
if( (runners[user[0]] < runners[user[1]] ) and (runners[user[0]] < runners[user[2]]) ):
    winner.insert(0,user[0])
    if(runners[user[1]] <  runners[user[2]]):
        winner.insert(1,user[1])
        winner.insert(2, user[2])
    else:
        winner.insert(1,user[2])
        winner.insert(2, user[1])
elif (runners[user[1]] < runners[user[2]]):
    winner.insert(0, user[1])
    if (runners[user[0]] < runners[user[2]]):
        winner.insert(1, user[0])
        winner.insert(2, user[2])
    else:
        winner.insert(1, user[2])
        winner.insert(2, user[0])
else:
    winner.insert(0, user[2])
    if (runners[user[0]] < runners[user[1]]):
        winner.insert(1, user[0])
        winner.insert(2, user[1])
    else:
        winner.insert(1, user[0])
        winner.insert(2, user[1])



   # for i in runners.keys():
    #    if(runners[key] < runners[i] and key !=i):
     #       winner.insert(pos,key)

   # pos+=1
pos=1
for key in winner:
    print(pos," is ",key," with time ",runners[key]," sec")
    pos+=1
#print occupied room and other details
#submitted by banshita

floor = int(input("Enter the no of floors : "))
total_room = 0
room_occupied = 0
t_room=0
o_room=0
for i in range(1, floor + 1):
    if (i == 13):
        continue
    else:
        t_room = int(input("Enter total no of room on floor "+str(i)+ " : "))
        o_room = int(input("Enter the NO of room occupied from "+str(t_room)+ " : "))
        total_room += t_room
        room_occupied += o_room
print("Total number of rooms on ", floor, " are : ", total_room)
print("Total number of occupied rooms are : ", room_occupied)
print("Total number of unoccupied rooms are :  ", (total_room - room_occupied))
print("Percentage of occupied rooms are : ", (room_occupied / total_room * 100))

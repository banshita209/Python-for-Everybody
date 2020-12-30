fname = input("Enter file name: ")
file=open(fname)
lst=list()
count = 0
for line in file:
    if line.startswith('From'):
        ls=line.split()
        lst.append(ls[1])
    else :
        continue

for word in lst:
    print(word)
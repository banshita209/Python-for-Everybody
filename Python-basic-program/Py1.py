import re

file = open("regex_sum_466753.txt")
num = list()
sum1=0
for line in file:
    line = line.strip()
    n=re.findall('[0-9]+', line)
    if len(n) ==0:
        continue
    else:
        num.append(n)
        for n1 in n:
            sum1=sum1+int(n1)
print(sum1)
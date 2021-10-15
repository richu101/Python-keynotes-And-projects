i = int(input("enter a num"))
sum = i%10
i = i/10
lastval = 0
while(i>1):
    lastval = i%10
    i = i/10

print(int(sum+lastval))

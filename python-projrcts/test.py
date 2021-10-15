def summ(m):
    s = 0
    while(m>1):
        s = s + m%10
        m = m/10
     
    return int(s)

num = int(input("enter the total number u r going to enter"))


sum = 0
while(num!=0):
    val = int(input(" "))
    sum = sum + summ(val) 
    print(sum)
    num = num-1
print("final ",sum)



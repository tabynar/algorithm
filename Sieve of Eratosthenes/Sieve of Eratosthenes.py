import math

# Input & Variable Set
n = int(input("N : "))
sn = int(math.sqrt(n))
memo = [0 for i in range(n+2)]

# Output & Main Function
for i in range(2,sn+1) :
    if memo[i] == 0 :
        j=2
        while i*j < n :
            memo[i*j]=1
            j+=1
for i in range(2,n+1) :
    if memo[i] == 0 : print(i)
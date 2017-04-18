c = int(input("num= "))
a = []
ca = c-1

for i in range(c) :
    a.append(int(input()))

for i in range(c-1) :
    for j in range(ca) :
        if(a[j]>a[j+1]) :
            null = a[j]
            a[j] = a[j+1]
            a[j+1] = null
    ca -= 1

for i in range(c) :
    print(a[i])
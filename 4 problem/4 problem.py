import random

def dice() :
    n = int(input("N : "))
    sn = 0

    for i in range(n) :
        rn = random.randint(1,6)
        print(rn)
        sn += rn
    print("avr :",sn/n)

def landmine() :
    n = int(input("plz call the number of 1 to 10 : "))
    arr = [0 for i in range(1,102)]
    TF = 0

    for i in range(10) :
        for j in range(10) :
            while TF == 0:
                rn = random.randint(1, 100)
                if arr[rn] == 0:
                    if rn <= 10*n : print("#",end=" ")
                    else : print(".",end=" ")
                    arr[rn] = 1
                    TF = 1
            TF = 0
        print("")

def yellow() :
    name = []
    TF = 0

    while TF == 0 :
        print("1. 친구 리스트 출력")
        print("2. 친구추가")
        print("3. 친구삭제")
        print("4. 이름변경")
        print("9. 종료")
        n = int(input("메뉴를 선택하시오: "))

        if n == 1 : print(name)
        elif n == 2 : name.append(input())
        elif n == 3 : name.remove(input())
        elif n == 4 :
            named = input()
            dn = name.index(named)
            name.remove(named)
            name.insert(dn,input())
        elif n == 9 : TF = 1

def lotto() :
    num = [0 for i in range(1,10)]
    arr = [0 for i in range(1,47)]
    TF = 0

    for i in range(7) :
        while TF == 0:
            n = random.randint(1, 45)
            if arr[n] == 0:
                arr[n] = 1
                num[i] = n
                TF = 1
        TF = 0
    cn = 6
    for i in range(6):
        for j in range(cn):
            if (num[j] > num[j+1]):
                null = num[j]
                num[j] = num[j+1]
                num[j+1] = null
        cn -= 1
    for i in range(7) : print(num[i])

#Main
print("1: dice\n2: landmin\n3: yellow\n4: lotto")
n = int(input())

if n == 1 : dice()
elif n == 2 : landmine()
elif n == 3 : yellow()
elif n == 4 : lotto()
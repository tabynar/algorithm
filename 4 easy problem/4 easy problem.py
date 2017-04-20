import random

def sum() :
    n = int(input("Num : "))
    TF = 0
    i = 10
    z = 1
    sn = 0
    dn = 0

    while TF == 0 :
        sn += (n%i-dn)/z
        dn = n%i
        if n%i == n :
            TF=1
        i *= 10
        z *= 10
    print(int(sn))

def facto() :
    f = 1
    for i in range(2,11) : f *= i
    print(f)

def function() :
    x1 = int(input("X1 : "))
    y1 = int(input("Y1 : "))
    x2 = int(input("X2 : "))
    y2 = int(input("Y2 : "))
    m = (y2-y1)/(x2-x1)
    print("y =",int(m),"* ( x -",x1,") +",y1)

def quiz() :
    num = random.randint(1,100)
    an = 0
    while an != num :
        an = int(input("숫자를 입력해주세요 : "))
        if an > num : print("정답이 더 작습니다.")
        elif an < num : print("정답이 더 큽니다.")
    print(an,"정답입니다!")

#Main Function
print("1: sum\n2: facto\n3: function\n4: quiz")
num = int(input())

if num == 1 : sum()
elif num == 2 : facto()
elif num == 3 : function()
elif num == 4 : quiz()
else : print("해당하는 메뉴가 존재하지 않습니다.")
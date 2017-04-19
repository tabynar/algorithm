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
    n = int(input("원하는 확률을 입력해주세요. : "))
    arr = [0 for i in range(1,102)]
    TF = 0

    for i in range(10) :
        for j in range(10) :
            while TF==0:
                rn = random.randint(1, 100)
                if arr[rn] == 0 :
                    if rn <= n : print("#",end=" ")
                    else : print(".",end=" ")
                    arr[rn] = 1
                    TF=1
            TF=0
        print()

def yellow() :
    name = []
    n = 0

    while n != 9 :
        print("1. 친구 리스트 출력")
        print("2. 친구추가")
        print("3. 친구삭제")
        print("4. 이름변경")
        print("9. 종료")
        n = int(input("메뉴를 선택하시오: "))

        if n == 1 : print(name)
        elif n == 2 :
            named = input("추가할 이름을 입력해주세요 : ")
            name.append(named)
            print("이름이 추가되었습니다.")
        elif n == 3 :
            named = input("삭제할 이름을 입력해주세요 : ")
            if named in name :
                name.remove(named)
                print("이름이 제거되었습니다.")
            else : print("해당하는 이름이 존재하지 않습니다.")
        elif n == 4 :
            named = input("삭제할 이름을 입력해주세요 : ")
            if named in name :
                dn = name.index(named)
                name.remove(named)
                name.insert(dn, input("변경할 이름을 입력해주세요 : "))
                print("변경이 완료되었습니다.")
            else : print("해당하는 이름이 존재하지 않습니다.")
        elif n != 9 : print("해당하는 메뉴가 없습니다")

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

#Main Function
print("1: dice\n2: landmin\n3: yellow\n4: lotto")
num = int(input())

if num == 1 : dice()
elif num == 2 : landmine()
elif num == 3 : yellow()
elif num == 4 : lotto()
else : print("해당하는 메뉴가 존재하지 않습니다.")
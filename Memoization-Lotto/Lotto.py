import random

arr = [0 for i in range(1,47)]
TF = 0

for i in range(5) :
    while TF == 0 :
        n = random.randint(1, 45)
        if arr[n]==0 :
            arr[n]=1
            print(n)
            TF=1
    TF=0

# TF = 일종의 스위치.
# arr[n] = 이미 등장한 숫자는 체크해놨다가 중복되지 않게 막아준다
# Memoization이라는 방법
# Memo할 공간 (ex- arr[])을 만들어 미리 결과값을 메모해놓는다.
# 결과값이 필요할 때 언제든 불러오자.
# 메모리를 할당해 속도를 챙기는 방법
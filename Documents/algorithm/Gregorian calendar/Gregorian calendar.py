day = [0,31,28,31,30,31,30,31,31,30,31,30,31] #매 월 날짜 모음
wday = ["일요일 입니다.", "월요일 입니다", "화요일 입니다", "수요일 입니다",
        "목요일 입니다", "금요일 입니다.", "토요일 입니다" ] #날짜의 선언
ld = 0 #총 경과한 날

Year = int(input("Year : ")) #년도의 입력
while Year<=0 :
    Year = int(input("Year : ")) #년도는 0이하가 될 수 없음.
Month = int(input("Month : ")) #달의 입력
while Month<=0 or Month>12 :
    Month = int(input("Month : ")) #달은 1~12의 범위
if Month >= 2 and (Year % 400 == 0 or (Year % 4 == 0 and Year % 100 != 0)) :
    day[2] += 1 #2월 이상이며 윤년이면 2월의 날 수에 하루를 더해줌.
Day = int(input("Day : ")) #날짜의 입력
while Day<=0 or Day>day[Month] :
    Day = int(input("Day : ")) #입력받은 달의 날짜수를 초과할 수 없고 0이하가 될 수 없음.

for i in range(1,Month) :
    ld += day[i] #입력받은 달 수 만큼 그 달에 해당하는 날짜를 더해줌.
ld += (Year-1)*365 + Day #입력받은 년도 만큼 지난 날 수를 구해줌.
for i in range(1, Year):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0): ld += 1  # 윤년인 년마다 지난 날짜 추가

print (ld) #지난 날 수 호출
print (wday[ld%7]) #지난 날 수를 7로 나눈 나머지에 적합한 날짜를 불러옴.
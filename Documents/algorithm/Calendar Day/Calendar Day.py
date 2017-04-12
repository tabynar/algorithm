day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
wday = ["일요일 입니다.", "월요일 입니다", "화요일 입니다", "수요일 입니다",
        "목요일 입니다", "금요일 입니다.", "토요일 입니다" ]
ld = 0

Year = int(input("Year : "))
Month = int(input("Month : "))
if Month >= 2 and (Year % 400 == 0 or (Year % 4 == 0 and Year % 100 != 0)) : day[2] += 1
Day = int(input("Day : "))
n = int(input("N : "))

for i in range(1,Month) : ld += day[i]
ld += (Year-1)*365 + Day
for i in range(1, Year):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0): ld += 1

ld += n
if Year % 400 == 0 or (Year % 4 == 0 and Year % 100 != 0) : day[2] = 29

for i in range(n) :
    Day+=1
    if Day>=day[Month] :
        Day=Day%day[Month]
        Month=Month%12+1
        if Month==1 :
            Year+=1
            if Year % 400 == 0 or (Year % 4 == 0 and Year % 100 != 0): day[2] = 29
            else : day[2] = 28
print(Year,"-",Month,"-",Day)
print (ld,"일 경과",wday[ld%7])
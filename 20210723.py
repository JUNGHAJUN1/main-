'''weather=input("오늘 날씨는 어때요?")
if weather=="비":
    print("우산을 챙기세요")
elif weather=="미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp=int(input("기온은 어떄요? "))
if 30<=temp:
    print("너무 더워요. 나가지 마세요")
elif 10<=temp and temp<30:
    print("괜찮은 날씨에요")
elif 0<=temp<10:
    print("외투를 챙기세요")
else :
    print("너무 추워요. 나가지 마세요")   

for waiting_no in range(1,6) 

students=[1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)


students=["Iron man","Thor","I am groot"]
students=[len(i) for i in students]
print(students)

students=["Iron man","Thor","I am groot"]
students=[i.upper() for i in students]
print(students)

a={"a":1,"b":3,"c":5,"d":7}
b=[(x,a[x])for x in a]
print(b)

from random import*
cnt=0
for i in range(1,51):
    time=int (random()*51)+1
    if 5<=time<=15 & cnt<2:
        print("[O]",i,"번째 손님 (소요시간 :",time,"분)" )
        cnt+=1
    elif time<5 or 15<time & cnt<2:
        print("[ ]",i,"번째 손님 (소요시간 :",time,"분)" )

print("총 탑승 승객:%d분"%cnt)




def deposit(balance,money):
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
    return balance+money

deposit(20000,30000)

def withdraw_night(balance,money):
    commission=100
    return commission,balance-money-commission
balance=0
#balance=deposit(balance,1000)
commission,balance=withdraw_night(balance,500)
print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(commission,balance))



gun=10

def checkpoint(soldiers):
    global gun
    gun=gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
def checkpoint_ret(gun,soldiers):
    gun=gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
gun=checkpoint_ret(gun,2)    
print("남은 총: {0}".format(gun))

def std_weight(height,gender):
    if gender==0:
    tota=height*height*22

    else
    tota=height*height*21
    
return tota

height=175
gender=0

weight=round(std_weight(height/100,gender),2)


print("키{0}cm{1}의 표준체중은 {2}kg 입니다.".format(height,gender,weight))


score_file=open("score.txt","w",encoding="utf8")
print("수학 : 0",file=score_file)
print("영어 : 50",file=score_file)
score_file.close()

score_file=open("score.txt","r",encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file=open("score.txt","r",encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file=open("score.txt","r",encoding="utf8")
lines=score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

import pickle

with open("profile.pickcle"."rb") as profile_file:
    print(pickle.load(profile_file))
with open("stude.txt"."w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
with open("stude.txt"."r",encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :") '''

class unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0},공격력{1}".format(self.hp,self.damage))




















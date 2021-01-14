##### 함수
'''
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()

##### 전달값과 반환값
def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다." .format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다." .format(commission, balance))
'''

##### 기본값
'''
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t사용 언어 : {2}" .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반, 같은 수업.
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t사용 언어 : {2}" .format(name, age, main_lang))

profile("유재석")
profile("김태호")
'''

##### 키워드값
'''
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=20, name = "김태호")
'''

##### 가변인자
'''
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C#", "C++", "javaScriptf") # 언어를 하나더 추가하려면 함수를 바꿔줘야하므로 가변인자를 사용한다.
profile("김태호", 23, "Kotlin", "Swift")
'''

##### 지역변수와 전역변수
'''
gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun을 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun

print("전체 총 : {0}" .format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}" .format(gun))
'''
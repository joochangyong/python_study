##### 숫자 자료형
'''
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
'''


##### 문자열 자료형
'''
print('풍선')
print("나비")
print("나비 " * 3)
'''

##### boolean(참 / 거짓) 자료형
'''
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))
'''

##### 변수
'''
# 애완동물을 소개해 주세요
animal = "고양이"
name = "해피"
age = 2
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
# 변수를 중간에 선언해도 됨.
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# +대신 ,도 가능. 변수 타입 안바꿔줘도 됨.
print(name, "는 ", (age), "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
'''
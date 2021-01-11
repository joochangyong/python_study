'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에서 춫엄을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
-- 당첨자 발표 --
치킨당첨자  : 1
커피당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
1st = [1, 2, 3, 4, 5]
print(1st)
shuffle(1st)
print(1st)
print(sample(1st, 1))
'''

from random import *
id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(id_list)
chicken = sample(id_list, 1)
coffee = sample(id_list, 3)
print(f" -- 당첨자 발표 -- \n 치킨당첨자 : {chicken} \n 커피당첨자 : {coffee} \n -- 축하합니다 --")

# 정답
users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)
shuffle(users)

winners = sample(users, 4) # 4명중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨당첨자  : {0}" .format(winners[0]))
print("커피당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다 --")
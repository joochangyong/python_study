##### 표준 입출력
'''
print("Python", "Java", sep = ", ", end = "? ") # sep = 사이에 , 넣어주기  end = 문장 맨 끝을 줄바꿈이 아닌 ?로 바꾸기
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file = sys.stdout) # 표준 출력으로 출력
print("Python", "Java", file = sys.stderr) # 표준 에러로 출력

# 시험 성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(3), str(score).rjust(4), sep = " : ") # .ljust(8) 왼쪽으로 정렬을 하는데 8칸을 확보한 상태에서 정렬

# 은행 대기순번표
for num in range(1, 21):
    print("대기번호 : ", str(num).zfill(3)) # .zfill(3) 3개의 공간을 확보하고 비어있는 공간은 0으로 대체한다

answer = input("아무값이나 입력하세요 : ") # input으로 값을 받게되면 항상 str타입으로 받는다
print("입력하신 값은 " + answer + "입니다.")
'''

##### 다양한 출력포맷
'''
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬(>)을 하되, 총 10자리 공간을 확보
print("{0: >10}" .format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}" .format(500))
print("{0: >+10}" .format(-500))
# 왼쪽 정렬(<)하고, 빈칸으로 _로 채움
print("{0:_<+10}" .format(500))
# 3자리마다 콤마 찍어주기
print("{0:,}" .format(100000000000))
# 3자리마다 콤마 찍어주기, +- 부호도 붙이기
print("{0:+,}" .format(100000000000))
print("{0:+,}" .format(-100000000000))
# 3자리마다 콤마를 찍어주기, +-부호도 붙이고, 자릿수 확보하기, 빈자리는 ^로 채워주기
print("{0:^<+30,}" .format(10000000000000000000))
# 소수점 출력
print("{0:f}" .format(5/3))
# 소수점 특정 자리수까지만 출력
print("{0:.2f}" .format(5/3)) # 소수점 2째자리까지 표시. 소수점 3째 자리에서 반올림
'''

##### 파일입출력
'''
score_file = open("score.txt", "w", encoding="utf8") # "w" 쓰기위한 용도, 덮어쓰기가 됨
print("국어 : 100", file=score_file)
print("영어 : 50", file=score_file)
print("수학 : 0", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # "a" 뒤에 내용을 계속 추가할 수 있음
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # .write를 쓸때는 줄바꿈이 안되서 \n을 써준다
score_file.close()

# 한번에 모든 내용 읽어오기
score_file = open("score.txt", "r", encoding="utf8") # "r" 읽기위한 용도
print(score_file.read())
score_file.close()

# 한줄씩 내용 읽어오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 파일이 몇줄인지 모를 때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# 리스트에 값을 다 넣어서 처리하는 방법
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
'''

##### pickle (데이터를 파일 형태로 저장해주는 것, 그 파일을 누군가에게 주면 상대방이 pickle을 이용해서 데이터를 가져와서 사용 가능)
'''
import pickle
profile_file = open("profile.pickle", "wb") # wb 쓰기, 바이너리타입으로 정의
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

# 파일에서 데이터 가져오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
'''

##### with (close를 해줄 필요가 없음)
'''
import pickle

with open("profile.pickle", "rb") as profile_file: # 파일을 profile_file로 저장
    print(pickle.load(profile_file))

# pickle을 사용하지않고 with로 읽어오기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
'''
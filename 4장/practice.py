##### 문자열
'''
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
'''

##### 슬라이싱
'''
jumin = "960525-1234567"
print("성별 : " + jumin[7])
print(jumin[0:2] + "년")
print(jumin[2:4] + "월")
print(jumin[4:6] + "일")
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지. 0:6에서 0 생략가능
print("뒤 7자리 : " + jumin[7:]) # 7 번째부터 끝까지 7:14에서 14 생략가능
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지. 맨뒤는 -1번째
'''

##### 문자열 처리 함수
'''
python = "Python is Amazing"
print(python.lower()) # 소문자로 변경
print(python.upper()) # 대문자로 변경
print(python[0].isupper()) # []에 있는 문자가 대문자인지 확인
print(len(python))
print(python.replace("Python", "Java")) # 문자열 바꾸기. Python을 Java로 바꾸기

index = python.index("n") # 문자가 몇번째 있는지 찾기
print(index)

index = python.index("n", index + 1) # 처음으로 나온 다음 자리수 찾기
print(index)

print(python.find("Java")) # 원하는 값이 없을 경우 -1 반환
# print(python.index("Java")) # 원하는 값이 없을 경우 오류 반환

print(python.count("n")) # n이 몇번나왔는지 반환
'''

##### 문자열 포맷
'''
# 방법1 %사용
print("나는 %d살입니다." %20) # %d는 숫자
print("나는 %s을 좋아해요." %"파이썬") # %s는 문자열
print("Apple은 %c로 시작해요." %"A") # %c는 문자

# %s는 모두 사용가능
print("나는 %s살입니다." %20) # %d는 숫자

print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법2 .format사용
print("나는 {}살입니다." .format(20))
print("나는 {}을 좋아해요." .format("파이썬"))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간")) # 포맷 순서 바꾸기

# 방법3 변수사용
print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color="빨간"))
print("나는 {color}살이며, {age}색을 좋아해요" .format(age = 20, color="빨간")) # 순서 바꾸기

# 방법4 (v3.6이상~) 변수 지정후 사용. print할때 맨 앞에 f 사용
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
'''

##### 탈출문자
'''
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# \" \' : 문장 내에서 따옴표 사용 가능
print("저는 '나도코딩'입니다. ")
print('저는 "나도코딩"입니다. ')
print("저는 \"나도코딩\"입니다. ")
print("저는 \'나도코딩\'입니다. ")

# \\ : 문장 내에서 하나의 \로 변경
print("C:\\Users\\JOO\\vscode\\Python\\PythonWorkspace") # \하나만 쓰면 에러.

# \r : 커서를 맨 앞으로 이동
print("Red Apple \rpine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")
'''
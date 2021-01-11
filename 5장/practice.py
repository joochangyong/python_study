##### 리스트[]
'''
# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 리스트 맨뒤에 추가 .append(object)
subway.append("하하") 
print(subway)

# 리스트 사이에 추가 .insert(index, object)
subway.insert(1, "정형돈") 
print(subway)

# 뒤에서부터 삭제
# subway.pop()
# print(subway)

# 같은 object가 몇개 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬

num_list = [5, 1, 3, 2, 4]
num_list.sort() # 오름차순
print(num_list)

num_list.reverse() # 내림차순
print(num_list)

num_list.clear() # 모두 지우기
print(num_list)


# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 1, 3, 2, 4]
num_list.extend(mix_list)
print(num_list)
'''

##### 사전{}
'''
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet[100])
print(cabinet.get(100))
# print(cabinet[5]) => 프로그램 중지
# print(cabinet.get(5)) => none 출력후 계속 실행

# 값이 있는지 여부 확인
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
cabinet["c-20"] = "조세호" # 값이 없을 경우 추가
print(cabinet)
cabinet["c-20"] = "김종국" # 값이 있을 경우 업데이트
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# Key 들만 출력
print(cabinet.keys())

# values 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)
'''

##### 튜플 (값을 추가하거나 변경은 불가능)
'''
menu = ("돈까스", "치즈까스")
print(menu[0], menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)
'''

##### 집합(set)
'''
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set) # 3은 한번만 출력

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)
'''

##### 자료구조의 변경
'''
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
'''
##### 클래스
'''
# 일반유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다." .format(self.name), end = " ")
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
'''

##### __init__
'''
Python에서 쓰이는 생성자. 즉, 객체(어떤 클래스로부터 만들어 지는 것들(marine, tank))가 만들어질때 호출되는 부분
marine, tank은 Unit클래스의 인스턴스라고함
'''

##### 멤버 변수
'''
위의 클래스 내에서 self.name, self.hp, self.damage을 멤버 변수라고 함
클래스 내에서 정의된 변수.

wraith1 = Unit("레이스", 80, 5)
# 멤버 변수를 외부에서도 사용 가능
print("유닛 이름 : {0}, 체력 : {1}, 공격력 : {2}" .format(wraith1.name, wraith1.hp, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
# 외부에서도 멤버 변수를 생성 가능. wraith2.clocking를 생성
wraith2.clocking = True

if wraith1.clocking == True:
    print("{0}는 현재 클로킹 상태입니다." .format(wraith2.name))
'''

##### 메소드
'''
# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # 공격하는 함수
    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]" .format(self.name, location, self.damage))

    # 공격받는 함수
    def damaged(self, damage):
        print("{0} : {1}데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25) # 공격 2번받는다고 과정
'''

##### 상속
'''
# 부모클래스. 일반유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 자식클래스. 공격 유닛. 클래스명()안에 상속받을 클래스명
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # Unit와 공통된 부분을 상속받는다
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp)
        self.damage = damage

    # 공격하는 함수
    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]" .format(self.name, location, self.damage))

    # 공격받는 함수
    def damaged(self, damage):
        print("{0} : {1}데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25) # 공격 2번받는다고 과정
'''

##### 다중 상속(부모가 둘 이상)
# 부모클래스. 일반유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 자식클래스. 공격 유닛. 클래스명()안에 상속받을 클래스명
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # Unit와 공통된 부분을 상속받는다
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp)
        self.damage = damage

    # 공격하는 함수
    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격 합니다. [공격력 {2}]" .format(self.name, location, self.damage))

    # 공격받는 함수
    def damaged(self, damage):
        print("{0} : {1}데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도 : {2}]" .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
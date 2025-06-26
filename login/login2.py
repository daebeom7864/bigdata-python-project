class Animal:
    #필드, 멤버변수
    #생성자
    def __init__(self, type, name, age, address, food):
        self.type=type
        self.name=name
        self.age=age
        self.address=address
        self.food=food

    #자기소개
    def introduce(self):
        print(f'{self.type}의 이름은 {self.name}입니다.')

    #음식 먹기
    def eat(self):
        print(f'{self.name}이(가) {self.food}를 먹습니다.')
        

dog = Animal('강아지', '뽀삐', 5, '서울', '개껌')
cat = Animal('고양이', '냐옹이', 3, '부산', '츄르')

print(dog.type)
print(dog.name)
print(dog.age)
print(dog.address)

dog.introduce()
cat.introduce()
class Korea:
    def __init__(self):
        self.nation_name='대한민국'
        self.capital='서울'
        self.language='한국어'

    def getNationName(self):
        print(self.nation_name)


class Person(Korea):
    def __init__(self, name, age):
        super().__init__()
        self.name=name
        self.age=age

    def getNationName(self):
        print(self.nation_name)
    #17, 18 넣고 안넣고 차이 보기

man = Person('홍길동', 20)
man.getNationName()
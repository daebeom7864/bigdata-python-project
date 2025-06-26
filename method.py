
#함수명
#로직
#매개변수
#리턴
fruits = ['apple', 'banana', 'cherry']
def get_data_from_list(list,index):
    data = list[index]
    print(data)
    
get_data_from_list(fruits,2)









#함수 선언
def add_two_numbers(num1,num2=0):
    sum = num1 + num2
    print(sum)

add_two_numbers(10,20)

def add10_20():
    a = 10
    b = 20
    c = a + b
    print(c)


#함수 호출
add_two_numbers(17,20)
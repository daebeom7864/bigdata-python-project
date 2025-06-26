#items = ['냉장고', '세탁기', 'TV','노트북','모니터']

#size = len(items)
#print(size)

#for i in range(len):
#    print(items[i])

usersFromDB = [
   {'id':'coco1422','pw':'1234','name':'김민수','birth':2004},
   {'id':'kim1234','pw':'5678','name':'김철수','birth':1999},
   {'id':'lee5678','pw':'abcd','name':'이영희','birth':2002},
   {'id':'park9999','pw':'qwer','name':'박민수','birth':1996},
   {'id':'choi1111','pw':'zxcv','name':'최지영','birth':2000},
   {'id':'jung2222','pw':'asdf','name':'정현우','birth':1998},
   {'id':'yoon3333','pw':'tyui','name':'윤서연','birth':2001},
   {'id':'kang4444','pw':'ghjk','name':'강동원','birth':1995},
   {'id':'shin5555','pw':'bnm','name':'신미영','birth':2003},
   {'id':'oh6666','pw':'poiu','name':'오태호','birth':1997},
   {'id':'hwang7777','pw':'lkjh','name':'황수진','birth':1999},
   {'id':'baek8888','pw':'mnbv','name':'백준호','birth':2000},
   {'id':'song9999','pw':'vcxz','name':'송하나','birth':2002},
   {'id':'lim0000','pw':'qaz','name':'임지훈','birth':1998},
   {'id':'han1111','pw':'wsx','name':'한소희','birth':2001},
   {'id':'ryu2222','pw':'edc','name':'류승우','birth':1996},
   {'id':'kwon3333','pw':'rfv','name':'권미라','birth':1999},
   {'id':'seo4444','pw':'tgb','name':'서준영','birth':2000},
   {'id':'jo5555','pw':'yhn','name':'조은영','birth':1997},
   {'id':'bae6666','pw':'ujm','name':'배현수','birth':1998},
]

#for i in range(len(usersFromDB)):
#    print(usersFromDB[i]['name']+"님은",str(usersFromDB[i]['birth'])+"년생 입니다.")

for user in usersFromDB:
   #데이터 추출
   name = user['name']
   birth = user['birth']

   #나이 계산
   age = 2025 - birth
   
   print(name + "님의 나이는" , str(age) + "살 입니다.")






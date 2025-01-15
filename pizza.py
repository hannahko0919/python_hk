# 피자 주문 함수
#음료 주문 함수수
pizmanu={'페퍼로니 피자': 3000, '치즈 피자': 3200,'콤비네이션 피자': 3500,'불고기 피자':3600,'해산물 피자': 3800}
dnkmanu={'콜라': 1500, '사이다': 1500,'생수': 1000}

def pizorder(ord):
   print('피자를 선택해주세요>', '\n', pizmanu,end=" ")
   while True:
        ord=input('메뉴 이름을 입력하세요(종료는 exit): ')
        if ord in pizmanu:
            count=int(input('수량을 입력하세요: '))
        elif ord=='exit':
            print('end')
            break
        else:
            print('error')
        
    
pizorder(ord)


def pizdnk(ord):
   print('음료수를 선택해주세요>', '\n', dnkmanu, end=" ")
   while True:
        ord=input('메뉴 이름을 입력하세요(종료는 exit): ')
        if ord in dnkmanu:
            count=int(input('수량을 입력하세요: '))
        elif ord=='exit':
            print('end')
            break
        else:
            print('error')
        
    
pizdnk(ord)

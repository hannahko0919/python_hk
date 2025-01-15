#피자 주문문
def pizza_select():
    pizmanu={'페퍼로니 피자': 3000,
    '치즈 피자': 3200,
    '콤비네이션 피자': 3500,
    '불고기 피자':3600,
    '해산물 피자': 3800}
    order_pizza={}

    for name, price in pizmanu.items():
            print(f'{name} ({price}원)')

    while True:
        pizname=input('메뉴이름 입력하세요(종료: exit): ')
        if pizname == 'exit':
            break
        elif pizname in pizmanu:
            count=int(input('수량 입력하세요: '))
            order_pizza[pizname]=count 
            print('주문 완료!')

    return order_pizza, pizmanu


#음료수 주문
def dnk_select():
    dnkmanu={'콜라': 1500, '사이다': 1500,'생수': 1000}
    order_drink={}

    for name, price in dnkmanu.items():
            print(f'{name} ({price}원)')

    while True:
        dnkname=input('메뉴이름 입력하세요(종료: exit): ')
        if dnkname == 'exit':
            break
        elif dnkname in dnkmanu:
            count=int(input('수량 입력하세요: '))
            order_drink[dnkname]=count
            print('주문 완료!')
    return order_drink, dnkmanu
if __name__=='__main__':
    print( pizza_select())
    print(dnk_select())
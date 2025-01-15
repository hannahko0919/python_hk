#피자 주문문
def select(menu,menuname):
    order={}
    print(f'\n***{menuname}목록***')
    for name, price in menu.items():
            print(f'{name} ({price}원)')

    while True:
        pizname=input(f'주문할 {menuname} 입력하세요(종료: exit): ')
        if pizname == 'exit':
            break
        elif pizname in menu:
            count=int(input('수량 입력하세요: '))
            order[pizname]=count 
            print('주문 완료!')

    return order

def money_calc(order,menu,menuname):
    totprice=0
    for x in order.keys():
        price=0
        if x in menu.keys():
            price=price+(order[x]*menu[x])   #order_pizza[x]=x의 값, ex. pizmenu['치즈피자']=3200
        print(f'{x}({menu[x]}원) x {order[x]} = {price:,}원')
        totprice=totprice+price

    print(f'{menuname} 가격: {totprice:,}원')
    return totprice


if __name__=='__main__':
    pizmenu={'페퍼로니 피자': 3000,
    '치즈 피자': 3200,
    '콤비네이션 피자': 3500,
    '불고기 피자':3600,
    '해산물 피자': 3800}
    dnkmenu={'콜라': 1500, '사이다': 1500,'생수': 1000}
    
    order_pizza=select(pizmenu,'피자')   #select(menu,menuname)
    print(order_pizza)
    order_drink=select(dnkmenu,'음료수')
    print(order_drink)
   
    totpiz= money_calc(order_pizza, pizmenu,'피자')
    totdnk=money_calc(order_drink, dnkmenu,'음료')

    print(f'전체 가격: 피자 + 음료: {totpiz + totdnk:,}원')


#영수증
# def money_calc():
# totprice=0
# for x in order_pizza.keys():    #name만 가져옴옴
#     price=0
#     if x in pizmenu.keys():
#          price=price+(order_pizza[x]*pizmenu[x])   #order_pizza[x]=x의 값, ex. pizmenu['치즈피자']=3200
#     print(f'{x}({pizmenu[x]}원) x {order_pizza[x]} = {price:,}원')
#     totprice=totprice+price
# print(f'피자 전체 가격: {totprice}')
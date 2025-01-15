import pizzorder_techer as p

pizmenu={'페퍼로니 피자': 3000,
'치즈 피자': 3200,
'콤비네이션 피자': 3500,
'불고기 피자':3600,
'해산물 피자': 3800}
dnkmenu={'콜라': 1500, '사이다': 1500,'생수': 1000}

#주문문
order_pizza=p.select(pizmenu,'피자') 
print(order_pizza)
order_drink=p.select(dnkmenu,'음료수')
print(order_drink)

totpiz= p.money_calc(order_pizza, pizmenu,'피자')
totdnk=p.money_calc(order_drink, dnkmenu,'음료')

print(f'전체 가격: 피자 + 음료: {totpiz + totdnk:,}원')



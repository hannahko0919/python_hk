import polyArea

print('사각형 넓이 계산')
width=float(input('사각형 가로 입력: '))
height=float(input('사각형 세로 입력: '))

print(f'사각형 넓이 = {polyArea.rectArea(width,height)}')

print('삼각형 넓이 계산')
width=float(input('삼각형 밑변 입력: '))
height=float(input('삼각형 높이 입력: '))
print(f'삼각형 넓이 = {polyArea.triArea(width,height)}')
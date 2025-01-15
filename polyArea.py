def rectArea(width,height):
    # a= width*height
    return width*height

def triArea(base,height):
    return base * height /2

if __name__=='__main__':         #'__name__' 과 '__main__':이 함수가 만들어진 곳에서만 호출. 다른 곳에서는 실행되지 않음.
    print(f'사각형 넚이: {rectArea(5,10)}')
    print(f'삼각형형 넚이: {triArea(5,10)}')
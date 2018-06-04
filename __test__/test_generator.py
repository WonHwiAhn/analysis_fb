# generator test

def squares(n=10):
    data = []
    for i in range(n):
        # data.append(i**2)
        # 종료 안됬을 경우에는 계속 값을 담아놨다가 마지막에 리턴
        yield(i, i**2)
        
    # return data

for x in squares(20):
    print(x, type(x))
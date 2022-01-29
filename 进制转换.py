

# 十进制转二进制
def solution(n):
    b = ''
    while True:
        s = n // 2
        y = n % 2
        # print(y)
        b = b +str(y)
        if s==0:
            break
        n = s
    print(b[::-1])
    print(b.count('1'))
solution(1234)
# http://www.spoj.com/problems/ADDREV/
n = int(input())

while n != 0:
    a, b = input().split(' ')
    a = int(a[::-1])
    b = int(b[::-1])
    sum = str(a + b)
    sum = sum[::-1]
    print(int(sum))
    n -= 1
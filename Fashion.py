# http://www.spoj.com/problems/FASHION/
t = int(input())

while t != 0:
    n = int(input())
    male = sorted([int(x) for x in input().split(' ')])
    female = sorted([int(x) for x in input().split(' ')])
    sum = 0
    for i in range(n):
        sum += male[i] * female[i]
    print(sum)
    t -= 1 
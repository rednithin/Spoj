# http://www.spoj.com/problems/CANDY3/

t = int(input())

while t != 0:
    i = input()
    if i == '':
        continue
    n = int(i)
    sum = 0
    for _ in range(n):
        sum += int(input())
    if(sum % n == 0):
        print('YES')
    else:
        print('NO')
    t -= 1
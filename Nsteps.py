# http://www.spoj.com/problems/NSTEPS/
t = int(input())

while t != 0:
    t -= 1
    x, y = [int(i) for i in input().split(' ')]
    if not (x >= 0 and y >= 0 and (x == y or x == y + 2)):
        print('No Number')
        continue
    if x & 1 == 0:
        print(x + y)
    else:
        print(x + y -1)
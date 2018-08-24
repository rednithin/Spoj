# http://www.spoj.com/problems/WILLITST/

n = int(input())
if n == 1:
    print('NIE')
    exit(0)
n = n & (n - 1)
if n == 0:
    print('TAK')
else:
    print('NIE')
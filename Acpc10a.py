# http://www.spoj.com/problems/ACPC10A/

while True:
    a, b, c = [int(x) for x in input().split(' ')]
    if a == 0 and b == 0 and c == 0:
        break
    if c - b == b - a:
        print('AP ' + str(c + (b - a)))
    else:
        print('GP ' + str(c * (b // a)))
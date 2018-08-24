# http://www.spoj.com/problems/ABSYS/
import re

t = int(input())

while t != 0:
    myStr = input()
    if myStr == '':
        continue
    a, b, c =[ x.strip() for x in myStr.replace('=', '+').split('+')]
    if 'machula' in a:
        a = str(int(c) - int(b))
    elif 'machula' in b:
        b = str(int(c) - int(a))
    else:
        c = str(int(a) + int(b))
    print(a + ' + ' + b + ' = ' + c)
    t -= 1
# http://www.spoj.com/problems/FCTRL2/

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

t = int(input())
while t != 0:
    n = int(input())
    print(fact(n))
    t -= 1
# http://www.spoj.com/problems/COINS/

def max(a, b):
    if a > b:
        return a
    else:
        return b

d = {0: 0, 1: 1, 2: 2}

def getmax(i):
    if i in d.keys():
        return d[i]
    ans = max(i, getmax(i//2) + getmax(i//3) + getmax(i//4))
    d[i] = ans
    return ans

while True:
    try:
        i = input()
    except:
        break
    n = int(i)
    print(getmax(n))
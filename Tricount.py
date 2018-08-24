# http://www.spoj.com/problems/TRICOUNT/

t = int(input())

while t != 0:
    n = int(input())
    print(n * (n + 2) * (2 * n + 1) // 8)
    t -= 1
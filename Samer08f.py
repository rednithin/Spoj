# http://www.spoj.com/problems/SAMER08F/

while True:
    n = int(input())
    if n == 0:
        break
    ans = n * (n + 1) * (2 * n + 1) / 6
    print(int(ans))
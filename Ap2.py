# http://www.spoj.com/problems/AP2/
import sys
t = int(input())

while t != 0:
    first, second, third = [int(x) for x in input().strip().split(' ')]
    n = third * 2 // (first + second)
    d = (second - first) // (n - 5)
    a = first - 2 * d
    sys.stdout.write(str(n) + '\n')
    s = ' '.join([str(x) for x in list(range(a, a + n * d, d))])
    sys.stdout.write(s + '\n')
    t -= 1
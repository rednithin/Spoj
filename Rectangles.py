# http://www.spoj.com/problems/AE00/


n = int(input())

sum = 0

for i in range(int(n ** 0.5)):
    sum += n // (i + 1) - i

print(sum)
# http://www.spoj.com/problems/HANGOVER/

arr = []
for i in range(2, 275):
    arr.append(1/i)

while True:
    n = float(input())
    if n == 0.00:
        break
    sum = 0
    i = 0
    while sum < n:
        sum += arr[i]
        i += 1
    print(str(i) + ' card(s)')

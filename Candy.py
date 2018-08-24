# http://www.spoj.com/problems/CANDY/

while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    sum = 0
    for i in range(n):
        arr.append(int(input()))
        sum += arr[-1]
    avg = sum // n
    if avg != sum / n:
        print(-1)
        continue
    change = 0
    for num in arr:
        if num > avg:
            change += num - avg
    print(change)
# http://www.spoj.com/problems/STAMPS/

t = int(input())
k = 1
while t != 0:
    threshold, maxFriends = [int(x) for x in input().split(' ')]
    arr = [int(x) for x in input().split(' ')]
    arr.sort(reverse=True)
    sum = 0
    i = 0
    while sum < threshold and i <= maxFriends and i != len(arr):
        sum += arr[i]
        i += 1
    if sum >= threshold:
        print('Scenario #' + str(k) +':')
        print(i)
        print()
    else:
        print('Scenario #' + str(k) +':')
        print('impossible')
        print()
    k += 1
    t -= 1
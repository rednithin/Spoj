# http://www.spoj.com/problems/PERMUT2/

while True:
    n = int(input())
    if n == 0:
        exit(0)
    arr = [int(x) for x in input().strip().split(' ')]
    flag = 0
    arr = [0] + arr
    for i in range(1, len(arr) // 2 + 1):
        if i != arr[arr[i]]:
            flag = 1
            break            
        i += 1
    if flag:
        print('not ambiguous')
    else:
        print('ambiguous')
            

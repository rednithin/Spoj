# http://www.spoj.com/problems/STPAR/

while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(x) for x in input().strip().split(' ')]
    stack = []
    carToPass = 1
    cantPass = 0
    for i in arr:
        while len(stack) != 0 and carToPass == stack[-1]:
            carToPass += 1
            stack.pop()
        if i == carToPass:
            carToPass += 1
            continue
        if len(stack) != 0 and i > stack[-1]:
            cantPass = 1
            break
        stack.append(i)
    if cantPass:
        print('no')
    else:
        print('yes')
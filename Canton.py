# http://www.spoj.com/problems/CANTON/
arr = [0]

i = 1
while arr[-1] < 10 ** 7:
    arr.append(i * (i + 1) // 2)
    i += 1

t = int(input())

while t != 0:
    t -= 1
    n = int(input())
    index = 1
    while arr[index] < n:
        index += 1
    diff = arr[index] - n
    if index & 1 == 1:
        output = str(1 + diff) + '/' + str(index - diff)
    else:
        output = str(index - diff) + '/' + str(1 + diff)
    print('TERM {0} IS {1}'.format(n, output))

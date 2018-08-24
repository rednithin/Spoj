# http://www.spoj.com/problems/ACODE/

while True:
    s = input()
    if s[0] == '0':
        exit(0)
    arr = [1, 1]

    for i in range(1, len(s)):
        curr = int(s[i])
        join = int(s[i-1:i+1])
        if join == 0 or (join > 26 and curr == 0):
            arr.append(0)
            break
        if curr == 0:
            arr.append(arr[-2])
        elif join > 26 or join < 10:
            arr.append(arr[-1])
        else:
            arr.append(arr[-1] + arr[-2])
    print(arr[-1])

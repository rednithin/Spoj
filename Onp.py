# http://www.spoj.com/problems/ONP/

def pref(ch):
    if ch == '^':
        return 3
    if ch == '*' or ch == '+':
        return 2
    if ch == '+' or ch == '-':
        return 1

def postfix(exp):
    arr = []
    for ch in exp:
        if int(ch.isalpha()):
            print(ch, end='')
            continue
        if ch == '(' or arr[-1] == '(':
            arr.append(ch)
            continue
        if ch == ')':
            index = ''.join(arr).rfind('(')
            rev = ''.join(arr[index+1:][::-1])
            arr = arr[:index]
            print(rev, end='')
            continue
        while True:
            print(ch)
            print(arr)
            input()
            now = pref(ch)
            prev = pref(arr[-1])
            if now > prev:
                break
            print(arr[-1], end='')
            arr = arr[:-1]
        arr.append(ch)


t = int(input())
while t != 0:
    exp = input()
    postfix(exp)
    print()
    t -= 1

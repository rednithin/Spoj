# http://www.spoj.com/problems/TOANDFRO/

while True:
    col = int(input())
    if col == 0:
        break
    myStr = input()
    modStr = ''
    for i in range(0, len(myStr), col):
        if (i // col) & 1 == 0:
            modStr += myStr[i:i+col]
        else:
            modStr += myStr[i:i+col][::-1]
    finalStr = ''
    for i in range(col):
        finalStr += modStr[i::col]
    print(finalStr)
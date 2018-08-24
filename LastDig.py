# http://www.spoj.com/problems/LASTDIG/

# import math

# t = int(input())

# while t != 0:
#     a, b = [int(x) for x in input().split(' ')]
#     if a != 0 and b == 0:
#         print(1)
#         continue
#     if a == 0:
#         print(0)
#         continue
#     a = a % 10    
#     b = 1 + (b - 1) % 4
#     ans = str( a ** b )[-1]
#     print(ans)


def getIt():
    testCases=int(input())
    allCases=[]
    for i in range(testCases):
        allCases.append([int(x) for x in input().split()])
    return allCases

def lastDig(a,b):
    if b<=4:
        lastDigit=str(a**b)[-1]
        return lastDigit
    else:
        if b%4==0:
            return lastDig(a,4)
        else:
            return lastDig(a,b%4)
        
               
def main():
    Tcases=getIt()
    for case in Tcases:
        print(lastDig(case[0],case[1]))
        
main()
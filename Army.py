# http://www.spoj.com/problems/ARMY/

t = int(input())

while t != 0:
    t -= 1
    input()
    input()
    god = [int(x) for x in input().strip().split(' ')]     
    mech = [int(x) for x in input().strip().split(' ')]
    if max(god) >= max(mech):
        print('Godzilla')
    else:
        print('MechaGodzilla')
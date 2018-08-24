# http://www.spoj.com/problems/PT07Y/

n, m = [int(x) for x in input().strip().split()]
parent = [-1] * (n + 1)

def findParent(a):
    if parent[a] == -1:
        return a
    return findParent(parent[a])
    
if m != n - 1:
    print('NO')
    exit(0)
for i in range(m):
    a, b = [int(x) for x in input().strip().split()]
    iA = findParent(a)
    iB = findParent(b)
    if iA == iB:
        print('NO')
        exit(0)
    if iA < iB:
        parent[iB] = iA
    else:
        parent[iA] = iB
print('YES')
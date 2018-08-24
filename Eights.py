# http://www.spoj.com/problems/EIGHTS/

# k = 1
# for i in range(12000):
#     if str(i*i*i)[-3:] == '888':
#         print(str(k) + ': ' + str(i))
#         k += 1
"""
1: 192
2: 442
3: 692
4: 942
5: 1192
6: 1442
7: 1692
8: 1942
9: 2192
10: 2442
11: 2692
12: 2942
13: 3192
14: 3442
15: 3692
16: 3942
17: 4192
18: 4442
19: 4692
20: 4942
21: 5192
22: 5442
23: 5692
24: 5942
25: 6192
26: 6442
27: 6692
28: 6942
29: 7192
30: 7442
31: 7692
32: 7942
33: 8192
34: 8442
35: 8692
36: 8942
37: 9192
38: 9442
39: 9692
40: 9942
41: 10192
42: 10442
43: 10692
44: 10942
45: 11192
46: 11442
47: 11692
48: 11942
"""

t = int(input())

arr = [192, 442, 692, 942]
while t != 0:
    k = int(input())
    k -= 1
    prefix = k // 4 * 1000
    postfix = arr[k % 4]
    ans = prefix + postfix
    print(ans)
    t -= 1
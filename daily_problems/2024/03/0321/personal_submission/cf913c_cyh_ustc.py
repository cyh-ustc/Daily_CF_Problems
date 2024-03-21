import sys
from collections import Counter, defaultdict
from functools import lru_cache
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


n, a = invr()
c = inlt()
d = [c[i] * pow(2, n - 1 - i) for i in range(n)]

x = []

t = 2 ** 63
for i in range(n):
    if d[i] <= t:
        x.append((c[i], pow(2, i)))
        t = d[i]

@lru_cache(None)
def f(a, i):
    if a <= 0:
        return 0
    if i == 0:
        return x[0][0] * a
    t = (a + x[i][1] - 1) // x[i][1]
    return min(f(a - t * x[i][1], i - 1) + t * x[i][0], f(a - (t - 1) * x[i][1], i - 1) + (t - 1) * x[i][0])

print(f(a, len(x) - 1))
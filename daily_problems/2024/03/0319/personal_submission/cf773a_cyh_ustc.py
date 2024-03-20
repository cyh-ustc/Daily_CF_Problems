import sys
from math import lcm
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



T = inp()
for _ in range(T):
    x, y, p, q = invr()
    if p == q and x < y:
        ret = -1
    elif p == 0 and x > 0:
        ret = -1
    else:
        l = 1
        r = 10 ** 10
        def f(u):
            if u * q < y:
                return False
            diff = u * q - y
            tgtx = u * p
            return diff + x >= tgtx and x <= tgtx

        while l < r - 1:
            mid = (l + r) // 2
            if f(mid):
                r = mid
            else:
                l = mid
        if f(l):
            ret = l * q - y
        else:
            ret = r * q - y
    print(ret)

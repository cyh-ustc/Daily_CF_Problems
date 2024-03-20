import sys
from math import lcm
from collections import Counter
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

def factorize(x):
    x = x
    ret = Counter()
    while x % 2 == 0:
        x //= 2
        ret[2] += 1
    t = 3
    while x >= t * t:
      while x % t == 0:
        x //= t
        ret[t] += 1
      t += 2
    if x != 1:
        ret[x] += 1
    return ret



T = inp()
for _ in range(T):
    n_, q = inlt()
    n = n_
    facn = factorize(n)
    n = n_
    for i in range(q):
        x = inlt()
        #print(x)
        if x[0] == 1:
            n *= x[1]
            facn += factorize(x[1])
            t = 1
            for v in facn.values():
                t *= (v + 1)
            if n % t == 0:
                print('YES')
            else:
                print('NO')
        else:
            n = n_
            facn = factorize(n)
    print('')


import sys
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


x = ('9681', '8961', '9816', '6891', '8691', '9861', '8196')

p = insr()
cnt = Counter(p)
cnt['1'] -= 1
cnt['6'] -= 1
cnt['8'] -= 1
cnt['9'] -= 1
z = ''
for i in '1234567890':
    z += i * cnt[i]

z += '0000'
if z[0] == '0':
    ret = '9681' + '0' * cnt['0']
else:
    t = 0
    b = 1
    for c in reversed(z):
        t += (ord(c) - ord('0')) * b
        t %= 7
        b *= 10
        b %= 7
    z = z[:-4] + x[(-t % 7) % 7]
    ret = z
print(ret)


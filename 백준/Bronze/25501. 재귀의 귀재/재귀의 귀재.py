import sys
input = sys.stdin.readline

def rec(s, l, r):
    global cnt
    cnt += 1 

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    return rec(s, l + 1, r - 1)

def asdf(s):
    return rec(s, 0, len(s) - 1)

n = int(input())

for _ in range(n):
    cnt = 0
    print(asdf(input().rstrip()), cnt)
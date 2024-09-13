def sol(a,b,c):
    if b == 1: 
        return a%c
    else:
        k = sol(a, b // 2, c)
        if b % 2 == 0:
            return (k**2) % c
        else:
            return (k**2 * a) % c

a,b,c = map(int, input().split())

print(sol(a,b,c))
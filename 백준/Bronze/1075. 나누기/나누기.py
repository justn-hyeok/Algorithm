n = int(input()) // 100 * 100
f = int(input())

for i in range(100):
    if n % f == 0:
        n = str(n)
        break
    n += 1

print(n[-2:])
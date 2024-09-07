n = int(input())

a = 0
b = 1

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(n - 1):
        a, b = b, a + b
    print(b)
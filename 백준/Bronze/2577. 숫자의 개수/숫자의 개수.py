from collections import Counter

a, b, c = int(input()), int(input()), int(input())
count = Counter(str(a * b * c))

for i in range(10):
    print(count.get(str(i), 0))
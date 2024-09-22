k = int(input())
stack = []
total = 0

for formoonsootja in range(k):
    num = int(input())

    if stack and num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
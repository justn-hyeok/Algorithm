a = int(input())
user = []

for i in range(a):
    age, name = input().split()
    user.append([int(age), name])
    
for i in sorted(user, key = lambda x : x[0]):
    print(i[0], i[1])
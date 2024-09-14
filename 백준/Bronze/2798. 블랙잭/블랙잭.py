n, m = map(int, input().split())
arr = list(map(int, input().split()))
r = 0

for i in range(n):
    for j in range(i+1, n):
        for asdf in range(j+1, n):
            if arr[i] + arr[j] + arr[asdf] > m:
                continue
            else:
                r = max(r, arr[i] + arr[j] + arr[asdf])
                
print(r)
a = int(input())

for i in range(a):
    prob, ans = map(str, input().split('='))
    
    if eval(prob) == int(ans):
        print("correct")
    else:
        print("wrong answer")
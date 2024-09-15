grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total_credit = 0
total_score = 0

for i in range(20):
    a = list(map(str, input().strip().split()))
    credit = float(a[1])
    
    if a[2] == "P":
        continue
    
    else:
        idx = grade.index(a[2])
        score0 = score[idx]
        total_score += (credit*score0)
        total_credit += credit

r = float(total_score / total_credit)
print(r)
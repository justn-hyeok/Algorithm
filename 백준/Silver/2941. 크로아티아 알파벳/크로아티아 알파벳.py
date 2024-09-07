def solution(s):
    fucking_stupid_strange_alphabets = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
    
    for alphabet in fucking_stupid_strange_alphabets:
        s = s.replace(alphabet, '*')
    count = len(s)
    
    return count


input_string = input().strip()
print(solution(input_string))
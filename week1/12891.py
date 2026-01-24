s, p = map(int, input().split())
dna = input()
min_A, min_C, min_G, min_T = map(int, input().split())

# 현재 윈도우의 각 문자 개수
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0} 

# 첫 윈도우 초기화 (0 ~ p-1)
for i in range(p):
    count[dna[i]] += 1

result = 0

def is_valid():
    return (count['A'] >= min_A and 
            count['C'] >= min_C and 
            count['G'] >= min_G and 
            count['T'] >= min_T)

# 첫 윈도우 체크
if is_valid():
    result += 1 

# 슬라이딩 윈도우: 한 칸씩 오른쪽 이동
for i in range(p, s):
    count[dna[i]] += 1       # 오른쪽 문자 추가
    count[dna[i - p]] -= 1   # 왼쪽 문자 제거
    
    if is_valid(): 
        result += 1

print(result)
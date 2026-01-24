import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열
prefix = [0] * n
prefix[0] = arr[0]

# 나머지 카운트 배열
mod_cnt = [0] * m

result = 0

# 누적합 구하기
for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]

# 각 누적합의 나머지 확인
for i in range(n):
    mod = prefix[i] % m
    
    # 나머지가 0이면 그 자체로 m의 배수
    if mod == 0:
        result += 1
    
    # 나머지 카운트 증가 
    mod_cnt[mod] += 1

# 같은 나머지끼리 조합
for i in range(m):
    if mod_cnt[i] > 1:
        # 같은 나머지를 가진 것 중 2개 선택
        result += mod_cnt[i] * (mod_cnt[i] - 1) // 2

print(result)
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0 

for i in range(n): # 각 수를 만들려는 목표 수로 설정
    target = arr[i]  # 만들려는 목표 수
    left = 0 
    right = n - 1
    
    while left < right: # 투 포인터 알고리즘 사용
        sum_val = arr[left] + arr[right] # 두 수의 합 계산
        if sum_val == target: # 합이 목표 수와 같으면
            answer += 1 # 카운트 증가
            break
        elif sum_val < target: # 합이 목표 수보다 작으면
            left += 1 # 왼쪽 포인터 증가
        else: # 합이 목표 수보다 크면
            right -= 1 # 오른쪽 포인터 감소

print(answer)
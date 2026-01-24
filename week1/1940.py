import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 투 포인터를 위한 정렬     

result = 0 
left = 0 
right = n - 1

while left < right: 
    sum_val = arr[left] + arr[right] # 두 값의 합 계산  
    
    if sum_val < m: # 합이 m보다 작으면 왼쪽 포인터를 오른쪽으로 이동
        left += 1
    elif sum_val > m: # 합이 m보다 크면 오른쪽 포인터를 왼쪽으로 이동
        right -= 1
    else:  # 합이 m과 같으면 카운트하고 양쪽 포인터를 이동
        result += 1
        left += 1
        right -= 1

print(result)
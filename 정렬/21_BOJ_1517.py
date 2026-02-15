import sys
input = sys.stdin.readline

result = 0

def merge_sort(s, e):
    global result
    if e - s < 1: return
    
    mid = s + (e - s) // 2
    merge_sort(s, mid)
    merge_sort(mid + 1, e)
    
    # 병합 과정
    temp = []
    i, j = s, mid + 1
    
    while i <= mid and j <= e:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            # 오른쪽 원소가 왼쪽보다 작아서 앞으로 올 때, 
            # 왼쪽 그룹에 남아있는 원소 개수만큼 swap이 발생한 것임
            result += (mid - i + 1)
            j += 1
            
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= e:
        temp.append(arr[j])
        j += 1
        
    for k in range(len(temp)):
        arr[s + k] = temp[k]

n = int(input())
arr = list(map(int, input().split()))
merge_sort(0, n - 1)
print(result)
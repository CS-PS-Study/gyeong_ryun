import sys
input = sys.stdin.readline

# N: 데이터 개수, K: 찾고자 하는 위치
n, k = map(int, input().split())
# 데이터 리스트 입력
a = list(map(int, input().split()))

# 파이썬 내장 정렬 (Timsort: 평균 O(N log N))
a.sort()

# K번째 수는 인덱스로 K-1
print(a[k-1])
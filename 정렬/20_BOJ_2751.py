import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

# 데이터가 많을 때는 sorted() 혹은 list.sort()가 가장 효율적
for i in sorted(nums):
    sys.stdout.write(str(i) + '\n')
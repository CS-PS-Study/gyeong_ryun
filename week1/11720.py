import sys

n = int(sys.stdin.readline()) # readline() 문자열로 입력받아서 int()로 형변환
numbers = list(sys.stdin.readline().strip()) #strip()로 개행문자 제거하고 리스트에 저장
sum = 0

for num in numbers:
    sum += int(num) #각 자리수를 정수로 변환하여 합산
    
print(sum)
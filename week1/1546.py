# 과목 수 저장
n = int(input()) #input()도 문자열로 입력받으므로 int()로 형변환
# 점수들을 공백 기준으로 나누어 리스트에 저장
scores = list(map(int, input().split()))
# 점수들의 합과 최대값 찾기
total_score = sum(scores) #합 구하기
max_score = max(scores) #최대값 찾기
# 점수들의 합으로 새로운 평균 계산 (분배법칙 이용)
new_average = (total_score / max_score * 100) / n
# 새로운 평균 출력
print(new_average)
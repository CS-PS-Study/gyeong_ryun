import sys
input = sys.stdin.readline

def backtracking():
    # 배열 길이가 m이 되면 출력 후 종료
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    for i in range(1, n+1):
        # 이미 사용한 숫자는 건너뜀 (중복 방지)
        if i not in array:
            array.append(i) # 선택
            backtracking() # 재귀
            array.pop() # 선택 취소 (백트래킹)

n, m = map(int,input().split())
array = [] # 선택한 숫자 저장 배열

backtracking()
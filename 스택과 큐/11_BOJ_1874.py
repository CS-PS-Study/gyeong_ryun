import sys

st = [] # 스택
op = '' # 연산 기록 
i = 1 # 현재 스택에 push할 수 있는 다음 숫자 (1부터 시작)
n = int(sys.stdin.readline()) # 수열의 길이

for j in range(0, n):
    num = int(sys.stdin.readline()) #만들어야 할 수열의 현재 숫자

    # 1) 현재 push할 수 있는 숫자(i)가 목표 숫자(num) 이하인 경우
    # -> i부터 num까지 순서대로 push한 후, num을 pop
    if i <= num:
        while i <= num:
            st.append(i)
            op += '+'
            i += 1
        op += '-'
        st.pop()

    # 2) 현재 push할 수 있는 숫자(i)가 목표 숫자(num)보다 큰 경우
    # -> 이미 num은 지나갔으므로, 스택 top에 num이 있어야만 pop 가능
    else:
        # 스택의 top이 num보다 작으면 num을 만들 수 없음
        if st[-1] < num:
            print('NO')
            exit() # 프로그램 종료
        
        # 스택의 top이 num이면 pop 가능
        else:
            op += '-'
            st.pop()

for i in op:
    print(i) # 모든 연산을 한 줄씩 출력
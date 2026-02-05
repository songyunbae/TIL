import sys
sys.stdin = open('input.txt')

# <problem>17413<is hardest>problem ever<end>
# <problem>31471<is hardest>melborp reve<end> 

# 괄호 는 그대로 두고 

str_list = str(input())
answer = ''
s_idx, e_idx = 0, 0

for i, s in enumerate(str_list):
    print('현재 글자', s)
    # 괄호가 오면, 일단 넘어간다
    if (s == '<'):
        answer += s
        pass
    elif (s == '>'):
        pass
    
    # 공백을 만나면, 그 인덱스 그대로 넣을거다.
    # 기록한 인덱스는 초기화 한다.
    elif (s == ' '):
        answer += s
        gap = e_idx - s_idx
        for j in range(0, gap+1):
            new_idx = (s_idx + gap + j) - (2*j)
        
            answer += str_list[new_idx]
        
        s_idx, e_idx = 0, 0
        pass
    # 괄호가 아니면 인덱스 바로 메모
    
    if (s_idx == 0): 
        s_idx = i
        pass

    if (e_idx == 0):
        e_idx = i
        pass
    
print(answer)
    # 그 다음부터 공백이 아니라면 인덱스를 메모한다.
    # 공백을 만나면, -1 해서 그 인덱스 까지 메모 후 다시 반복문돌려서 문자열 붙여넣기

    
# 변경 대상 시작, 끝 찾기

# 시작 끝 -2 씩해서 자리 교체 해서 담기

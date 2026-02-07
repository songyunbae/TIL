import sys
sys.stdin = open('input.txt')

def reverse_word (s_idx, e_idx, answer, org_str):
    # 마지막 인덱스 대입.
    if (i == len(str_list)-1): e_idx = i
    
    tmp_str = org_str[s_idx:e_idx+1]
    answer += tmp_str[::-1]
   
    if(s == ' '): answer+=s      
    s_idx, e_idx = -1, -1
    return s_idx, e_idx, answer


str_list = str(input())

answer = ''
flag = False # 인덱스 만남 여부
s_idx, e_idx = -1, -1

for i, s in enumerate(str_list):
    # 여는 괄호
    if (s == '<'):
        # 바꿀 단어가 있다면 함수 호출
        if (s_idx != -1): s_idx, e_idx, answer = reverse_word(s_idx, e_idx, answer, str_list)
        flag = True
        answer += s
        continue
    # 닫는 괄호
    elif (s == '>'):
        flag = False
        answer += s
        continue
    
    # 괄호 안의 문자인 경우.
    if (flag):
        answer += s
        continue
    
    # 공백을 만나거나, 문자열의 마지막인 경우
    elif (s == ' ' or (i == len(str_list)-1)):
        s_idx, e_idx, answer = reverse_word(s_idx, e_idx, answer, str_list)
        continue
    
    # 바꿔야 하는 대상 문자열의 마지막 인덱스.
    e_idx = i
    
    if (s_idx == -1): 
        s_idx = i
        continue    
    
print(answer)
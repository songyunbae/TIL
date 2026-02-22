import sys
sys.stdin = open('input.txt')

N, new_sc, P = map(int, input().split())
sc_list = []
answer = 0
tmp_ans = 0
same_num = 0

if(N > 0):
    sc_list = list(map(int, input().split()))
    for sc in sc_list:
        # 갱신중인 최대값 이상이라면 갱신
        if (new_sc < sc):
            tmp_ans += 1
        # 랭크 내에 같은 값이 몇 개 있는지.
        if (new_sc == sc):
            same_num += 1
    
    # 새로운 점수 앞에 몇 개 있는지 체크한 것 이므로 +1 해준다.
    answer = tmp_ans + 1
    
    # 랭킹 리스트 갯수보다 많아지는지 체크한다. 
    # 같은 점수와 내 앞의 점수의 갯수를 합해서 랭크 제한(P)를 넘어가는지 확인.
    if (same_num + tmp_ans >= P):
        answer = -1
else :
    answer = 1

print(answer)


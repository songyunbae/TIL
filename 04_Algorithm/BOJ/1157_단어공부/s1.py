import sys
sys.stdin = open('input.txt')

# 가장 많이 사용된 문자 하나 출력
# 여러개 일 경우 '?' 출력
# 입력 : Mississipi
input_str = list(input().upper())
word = input().strip().upper()
print(word)

max_cnt = 0
max_chr = ''
res_cnt = 0
key_obj = {}

for i in range(len(input_str)):
    if(key_obj.get(input_str[i])):
        cur_cnt = key_obj.get(input_str[i])
        cur_cnt+=1
        key_obj[input_str[i]] = cur_cnt

    else:
        key_obj.setdefault(input_str[i], 1)

    if (max_cnt < key_obj[input_str[i]]):
        max_cnt = key_obj[input_str[i]]
        max_chr = input_str[i]

for obj in key_obj.values():
    if (obj == max_cnt):
        res_cnt+=1
    
if (res_cnt >= 2):
    print('?')
else:
    print(max_chr)

import sys
sys.stdin = open('input.txt')


stu_list = sys.stdin.readlines()[1:]

# 나이 어린 순으로, 
# 나이가 같다면 가입한 순으로    

stu_list.sort(key=lambda age: int(age.split()[0]))
print("".join(stu_list))



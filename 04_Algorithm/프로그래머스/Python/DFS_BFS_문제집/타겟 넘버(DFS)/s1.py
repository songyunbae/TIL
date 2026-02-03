def solution(numbers, target):
    global answer 
    answer = 0

    def dfs(now_num, idx, tmp_cnt):    
        global answer
        
        if idx == len(numbers):
            if now_num == target:
                answer+=1
            return
        
        dfs(now_num + numbers[idx], idx+1, tmp_cnt)
        dfs(now_num - numbers[idx], idx+1, tmp_cnt)
    
    dfs(0, 0, 0)
    
    
    return answer



# numbers =  [4, 1, 2, 1]
# target = 4
from collections import deque

def bfs(arr, num):
    res = []
    q = deque([ ([], 0) ])
    while q:
        subset, next_id = q.popleft()
        
        if sum(subset) == num:
            if subset not in res:
                res.append(subset)
            
        if next_id == len(arr):
            continue
            
        else:
            for i in range(next_id, len(arr)):
                if sum(subset) + arr[i] > num:
                    continue
                
                q.append( (subset+[arr[i]], i+1) )
                
    return res
            
    
def solution(arr, num):
    return sorted(bfs(arr, num))

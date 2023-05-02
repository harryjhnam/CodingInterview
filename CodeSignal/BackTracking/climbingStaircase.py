def dfs(n, k):
    stack = [ [] ]
    res = []
    while stack:
        steps = stack.pop()
        
        if sum(steps) == n:
            res.append(steps)
        
        elif sum(steps) < n:
            for i in range(1, k+1):
                if sum(steps) + i <= n:
                    stack.append(steps+[i])
    return res

def solution(n, k):
    return sorted(dfs(n,k))
  

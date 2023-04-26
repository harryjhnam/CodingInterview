#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

from collections import deque

def bfs(t):
    q = deque([(0,t)])
    
    level = 0
    level_nums = []
    while q:
        if q[0][0] == level:
            l, t = q.popleft()
            if t:
                level_nums.append(t.value)
                q.append((l+1, t.left))
                q.append((l+1, t.right))
            else:
                level_nums.append(-1)
            
        else:
            if level_nums != level_nums[::-1]:
                return False
                
            level += 1
            level_nums = []
    
    return True
        
def solution(t):
    if t:
        return bfs(t)
    else:
        return True
       

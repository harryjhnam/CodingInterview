#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def dfs(v, total, s):
    total += v.value
    
    if v.left == None and v.right == None:
        return total == s
    
    if v.left:
        left = dfs(v.left, total, s)
    else:
        left = False
        
    if v.right:
        right = dfs(v.right, total, s)
    else:
        right = False
    
    return left or right

def solution(t, s):
    if t:
        return dfs(t, 0, s)
    return False
  

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def dfs(t, k):
    stack = [t]
    i = 0
    while stack:
        v = stack.pop()
        if v.left == None:
            i += 1
            if i == k:
                return v.value
        if v.right:
            stack.append(v.right)
            v.right = None
        if v.left:
            stack.append(v)
            stack.append(v.left)
            v.left = None
        
def solution(t, k):
    return dfs(t, k)
  

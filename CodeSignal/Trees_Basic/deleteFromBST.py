#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def solution(t, queries):
    
    def max_of_tree(t):
        if t.right is None:
            return t
        else:
            t = max_of_tree(t.right)
        return t
            
    def remove_right(t):
        if t.right is None:
            return t.left
        else:
            t.right = remove_right(t.right)
        return t

    def f1(t, x):
        if t is None:
            return None
        if t.value == x:
            if t.left:
                t.value = max_of_tree(t.left).value
                t.left = remove_right(t.left)
                return t
            else:
                return t.right
            
        elif x < t.value:
            t.left = f1(t.left, x)
        elif x > t.value:
            t.right = f1(t.right, x)
            
        return t
        
    for q in queries:
        t = f1(t, q)
        
    return t

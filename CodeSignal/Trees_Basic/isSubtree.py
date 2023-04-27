#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def is_leaf(t):
    return t.left == None and t.right == None

def compare(anc, sub_comp, comp):
    if anc == None and sub_comp == None:
        return True
    if anc == None or sub_comp == None:
        return False
    
    if is_leaf(anc) and is_leaf(sub_comp):
        return anc.value == sub_comp.value
    
    if is_leaf(comp):
        return compare(anc.left, comp, comp) or compare(anc.right, comp, comp)
    
    if (is_leaf(anc) and not is_leaf(sub_comp)) or (not is_leaf(anc) and is_leaf(sub_comp)):
        return False
        
    if anc.value == sub_comp.value:
        return compare(anc.left, sub_comp.left, comp) and compare(anc.right, sub_comp.right, comp)
    else:     
        return compare(anc.left, comp, comp) or compare(anc.right, comp, comp)


def solution(t1, t2):
    if t2 == None:
        return True
    return compare(t1, t2, t2)

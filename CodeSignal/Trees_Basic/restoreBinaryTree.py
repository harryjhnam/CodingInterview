def build_bt(inorder, preorder):
    if not preorder:
        return None
    
    i = inorder.index(preorder[0])
    t = Tree(preorder[0])
    t.left = build_bt(inorder[:i+1], preorder[1:i+1])
    t.right = build_bt(inorder[i+1:],preorder[i+1:])
    return t

def solution(inorder, preorder):
    return build_bt(inorder, preorder)
  

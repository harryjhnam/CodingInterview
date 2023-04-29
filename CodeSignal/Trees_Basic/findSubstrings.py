class Trie():
    def __init__(self, s):
        self.letter = s
        self.is_terminal = False
        self.children = {}
        
def append_Trie(root, part):
    cur = root
    for s in part:
        if s not in cur.children:
            cur.children[s] = Trie(s)
        cur = cur.children[s]
    cur.is_terminal = True
    return root

def find_part(word, root):
    start_pos = 0
    max_len = 0
    
    for start_i in range(len(word)):
        cur = root
        for i in range(start_i, len(word)):
            s = word[i]
            if s not in cur.children:
                break
            cur = cur.children[s]
            
            length = i - start_i + 1
            if cur.is_terminal and length > max_len:
                max_len = length
                start_pos = start_i
            
    if max_len > 0:
        end_pos = start_pos + max_len
        return word[:start_pos]+'['+word[start_pos:end_pos]+']'+word[end_pos:]
    
    return word
                
        

def solution(words, parts):
    
    root = Trie('')
    for part in parts:
        root = append_Trie(root, part)
        
    res = []
    for word in words:
        res.append(find_part(word, root))
        
    return res
  

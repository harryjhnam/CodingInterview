from copy import deepcopy

def update(n, valid_positions, row, col):
    
    n_valid = 0
    for i in range(n):
        for j in range(col, n):
            if i == row:
                valid_positions[i][j] = False
            elif j == col:
                valid_positions[i][j] = False
            elif i + j == row + col:
                valid_positions[i][j] = False
            elif i - j == row - col:
                valid_positions[i][j] = False
            else:
                if j == col+1 and valid_positions[i][j]:
                    n_valid += 1
    
    if n_valid > 0 or col == n-1:
        valid = True
    else:
        valid = False
    
    return valid_positions, valid
    
        
def dfs(n):
    
    valid_positions = [[True]*n for _ in range(n)]
    res = []
    
    stack = [([], valid_positions)]
    
    while stack:
        placed_rows, valid_positions = stack.pop()
        
        if len(placed_rows) == n:
            res.append([r+1 for r in placed_rows])
        
        else:
            next_col = len(placed_rows)
            for i, row_valid in enumerate(valid_positions):
                if row_valid[next_col]: 
                    new_valid_position, valid = update(n, deepcopy(valid_positions), i, next_col)
                    if valid:
                        stack.append( (placed_rows+[i], new_valid_position) )
        
    return res

def solution(n):
    
    return sorted(dfs(n))

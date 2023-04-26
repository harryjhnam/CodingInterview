def solution(level, pos):
    if pos == 1:
        return "Engineer"
    if pos == 2**(level-1):
        if level % 2 == 0:
            return "Doctor"
        else:
            return "Engineer"
            
    if pos % 2 == 0:
        return "Doctor" if solution(level-1, pos//2) == "Engineer" else "Engineer"
    else:
        return solution(level-1, (pos+1)//2)
        

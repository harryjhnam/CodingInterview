N = int(input())
directions = input().split()

vec = {'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0)}

loc = [1,1]

for direction in directions:
  loc[0] += vec[direction][0]
  loc[1] += vec[direction][1]
  
  loc[0] = max(1, min(N, loc[0]))
  loc[1] = max(1, min(N, loc[1]))

print(loc)
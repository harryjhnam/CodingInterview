S = input()

alphas = []
is_num_included = False
sum = 0

for s in S:
  if s.isnumeric():
    sum += int(s)
    is_num_included = True
  else:
    alphas.append(s)

if is_num_included:
  print(''.join(sorted(alphas))+str(sum))
else:
  print(''.join(sorted(alphas)))
  
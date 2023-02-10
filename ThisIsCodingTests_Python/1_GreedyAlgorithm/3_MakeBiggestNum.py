nums = map(int, list(input()))

result = 0
for n in nums:
  if n <= 1 or result <= 1:
    result += n
  else:
    result *= n

print(result)
  
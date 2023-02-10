
def process_N(N, K, n_steps=0):
  
  if N == 1:
    return n_steps
  
  elif N % K == 0:
    return process_N(N//K, K, n_steps+1)

  else:
    return process_N(N-1, K, n_steps+1)


def better_process_N(N, K, n_steps=0):

  if N == 0:
      return n_steps-1
  
  elif N == 1:
    return n_steps
  
  elif N % K == 0:
    return process_N(N//K, K, n_steps+1)

  else:
    return process_N(N-N%K, K, n_steps+N%K)


N, K = map(int, input().split())
print(better_process_N(N, K))
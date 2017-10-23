def fatorial(n):
  if n == 0:
      return 1
  else:
      return n * fatorial(n-1)


def eulerSerieTaylor(x,n):

    euler = 1.0
    i = n - 1
    while(i > 0):
        euler = 1 + x * euler/i
        i -= 1
    return euler

def eulerFatorial(x,n):

    if (x<0):
        y = -x
    else:
        y = x

    euler = 1.0
    for i in range(1,n):
        euler += y**i/fatorial(i)
    return euler


print( eulerSerieTaylor(1,10))
print( eulerFatorial(1,10))

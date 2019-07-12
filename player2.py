def fact(b):
  if b==0:
    return 1
  else:
    return b*fact(b-1)
b=int(input())
print(fact(b))

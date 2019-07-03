print("1.Prime number for a Range")
print("2.Check whether a number is prime")
c=eval(input(("Enter your Choice:")))
if(c==1):
  r=eval(input("Enter the Range:"))
  if(r>0):
    for i in range(2,r+1):
      if(i%i==1):
        print(i)
        i=+1
      else:
        print(i)
  else:
    print("Not proper Range")
if(c==2):
  a=eval(input("Enter the Number:"))
  for i in range(2,a):
    if(a% i)== 0:
        print(a, "is not a prime number")
        exit()
  else:
        print(a, "is a prime number")

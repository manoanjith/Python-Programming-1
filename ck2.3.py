a=eval(input("Enter the Number:"))
while(a<1000):
  for i in range(2,a):
    if(a% i)== 0:
        print("yes")
        exit()
  else:
        print("no")

x=int(input())
temp=x
rev=0
while(x>0):
  digit=x%10
  rev=rev*10+digit
  x=x//10
if(temp==rev):
  print("yes")
else:
  print("no")

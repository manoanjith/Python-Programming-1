class a:
  def __init__(self):
    self.a=[]
  def add(self,dataval):
    if dataval not in self.a:
      self.a.append(dataval)
      return True
    else:
      return False
  def remove(self):
    if len(self.a)<=0:
      return("no element")
    else:
      return self.a.pop()
b=a()
b.add("MON")
b.add("sa")
b.add("ra")
b.add("th")
b.add("ds")
print(b.remove())
print(b.remove())





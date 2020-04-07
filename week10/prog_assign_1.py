n=input()
cone, czero = 0,0
a = [ int(i) for i in str(n)]
for i in a:
  if i == 0:
  	cone+=1  
  else:
    czero+=1
if cone==1 or czero==1:
  print("YES", end='')
else:
  print("NO",end='')

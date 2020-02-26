x, y = [int(x) for x in input().split()] 
k=1
for i in range(x):
  for j in range(y):
    if(j!=y-1):
      print(k,end=' ')
      k=k+1
    else:
      print(k,end='')
      k=k+1
  if(i!=x-1):
    print()
  else:
    print(end='')

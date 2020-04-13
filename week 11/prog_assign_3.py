m, n = (int (x) for x in input().split(','))
items =[]
for i in range(m, n+1):
  flag=0
  s=str(i)
  for j in range(len(s)):
    if(int(s[j])%2!=0):
    	flag=1
  if(flag==0):
    items.append(s)
print( ",".join(items),end="")

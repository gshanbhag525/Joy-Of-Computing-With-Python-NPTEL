o=list(map(int,input().split()))
d=[]
for i in o:
  if i not in d:
    d.append(i)
print(*d,end="")

s=input()
print(s.swapcase(), end=" ")

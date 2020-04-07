a=input()
b=a.split(' ')
b=[int(i) for i in b]
n = len(b)
total=int((n+1)*(n+2)/2)
s = int(sum(b))
print(total-s,end='')

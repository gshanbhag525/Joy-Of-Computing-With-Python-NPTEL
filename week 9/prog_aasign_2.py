def k(a):
  if len(a)<2:
    return' '
  else:
    return a[0:2] + a[-2:]
a=input()
print(k(a), end="")

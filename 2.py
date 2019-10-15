fi = raw_input("Insert directory(only name if in the same directory with program): ")
d = 0
t = 0
s = 0
b = 0
with open(fi) as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if (c == '\t'):
     t += 1
    if (c == '\b'):
     b += 1
    if (c == " "):
      s += 1
    if (c == '\u007F'):
     d += 1
print s , " spaces"
print t , " tabs"
print b , " backspaces"
print d , " deletes"

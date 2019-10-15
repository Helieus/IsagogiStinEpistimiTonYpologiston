fi = raw_input("Insert directory(only name if in the same directory with program): ")
doubles = []
doubles2 = []
with open(fi) as f:
  d = f.read(1)
  while True:
    if not d:
      break
    else:
      c = d
      d = f.read(1)
    if not d:
      break
    if (c == d):
      s = 0
      for i in range(0,len(doubles)):
        if (doubles[i] == c*2):
          s = i
      if (s != 0):
          doubles2[s] += 1
      else:
          doubles.append(c*2)
          doubles2.append(1)
for j in range(0,len(doubles)):
    print doubles2[j] , " " , doubles[j] 

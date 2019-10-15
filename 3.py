fi = raw_input("Insert directory(only name if in the same directory with program): ")
comments = ''
end = 0
with open(fi) as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if (end == 1):
        break
    if (c == '/'):
      c = f.read(1)
      if (c == '/'):
        comments += '\n//'
        c = f.read(1)
        while (c != '\n'):
          comments += c
          c = f.read(1)
      elif (c == '*'):
        comments2 = '\n/*'
        while True:
          c = f.read(1)
          if not c:
            end = 1
            break
          if (c == '*'):
            c = f.read(1)
            if (c == '/'):
              comments2 += '*/'
              comments += comments2
              break
            else:
              comments2 += '*'
          comments2 += c
print comments



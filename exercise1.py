first = []
for num in range(1, 1000, 2):
    IsFirst = True
    for i in range(2, num - 1):
        if(num % i == 0):
            IsFirst = False
            continue
    if(IsFirst):
        first.append(num)
for x in first:
    print(x)
distance =0
for x in range(1,len(first)):
   if((first[x]-first[x-1])>distance):
       distance = first[x]-first[x-1]
       position1= first[x-1]
       position2= first[x]
print('Biggest Distance:',distance)
print('Between',position1,position2)
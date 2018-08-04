num = list(input())
if (len(num) not in range(0, 41)):
  print ("length of inputs out of range")
  exit()
for i in range(len(num)):
  if (int(num[i]) not in range(2, 10)):
     exit()
  num[i] = int(num[i])
alpha = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
op=[]
for i in range(len(num)):
  op.append(alpha[(num[i]-2)][0])
for i in range(len(num)-1):
  if((num[i+1] != 7) or (num[i+1] != 9)):
     n=((num[i] -1)%3)
     op.append(alpha[(num[i+1] -2)][n])
  else:
     n=((num[i] -1)%4)
     op.append(alpha[(num[i+1] -2)][n])
op=list(set(op))
print (len(op))


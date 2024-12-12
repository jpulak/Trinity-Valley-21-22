num = int(input())

f = []
for i in range(num):
  ask = input()
  new = ask.split()
  for i in range(len(new[0])):
    if i==2:
      new = new[0].replace('2','0')
      f.append(new)
for i in range(num):
  print(f[i])

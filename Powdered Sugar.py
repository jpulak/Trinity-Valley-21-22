all=[]
nums=[]
final=[]
n=int(input())
for i in range(n):
  agent= input().split()
  all.append(agent)

for x in all:
  x[2]= int(x[2])

all.sort(key=lambda x:x[2])

for i in range(0,n):
  del all[i][2]
  
for i in range(len(all)):
  print(' '.join(map(str,all[i])))

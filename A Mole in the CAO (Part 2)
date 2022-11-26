all=[]
uniqueList = []
duplicateList = []
reals=[]
n= int(input())
for i in range(n):
  all.append(input().split())

all=(sum(all,[]))
all= list(map(int,all))
for i in all:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
for i in range(len(duplicateList)):
  count= all.count(duplicateList[i])
  if count ==n:
    print(duplicateList[i])

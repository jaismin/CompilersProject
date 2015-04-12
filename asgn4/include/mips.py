def printCode123(currElement):
  # print len(currElement.tempvar)
  for i in currElement.code :
    for j in range(5):
      if (i[j]!=None):
        if type(i[j])==str and "@t" in i[j]:
          if (i[j][0]=='*'):
            print i[j][0:2]+i[j][3:],
          else:
            print i[j][1:],
        else:
          print i[j],
    print 
  print 
  print


def traversetree123(SCOPE):
  queue=list()
  objects=list()
  queue.append(SCOPE)
  while len(queue) >0 :
    currElement=queue[0]
    del queue[0]
    for i in range (len(currElement.childs)):
      queue.append(currElement.childs[i])
        
    printCode123(currElement)


def generateMips(SCOPE):
	traversetree123(SCOPE)

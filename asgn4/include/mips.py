def printCode123(currElement):
  # print len(currElement.tempvar)
  for i in currElement.code :
    # for ele in i:
    #   if type(ele) == type("fuck"):
    #     ele = ele.replace("@", "")
    if i[3] == '|' :
      print "or $"+i[0] +",$"+i[2]+",$"+i[4];
    elif i[3] == '^' :
      print "xor $"+i[0] +",$"+i[2]+",$"+i[4];
    elif i[3] == '&' :
      print "and $"+i[0] +",$"+i[2]+",$"+i[4];
    elif i[2] == '==':
      print "beq $"+i[1]+",$"+i[3].split()[0]+","+i[4];
    elif i[2] == '!=':
      print "bne $"+i[1]+",$"+i[3].split()[0]+","+i[4];
    elif i[2] == '>':
      print "slt $_temp,$"+i[3].split()[0]+",$"+i[1]
      print "beq $_temp,1,"+i[4];
    elif  i[2] == '<' :
      print "slt $_temp,$"+i[3].split()[0]+",$"+i[1]
      print "beq $_temp,$zero,"+i[4];
    elif i[2] == '>=':
      print "slt $_temp,$"+i[3].split()[0]+","+i[1]
      print "beq $_temp,1,$"+i[4];
      print "beq $"+i[1]+",$"+i[3].split()[0]+",$"+i[4];
    elif  i[2] == '<=' :
      print "slt $_temp,$"+i[3].split()[0]+","+i[1]
      print "beq $_temp,$zero,"+i[4];
      print "beq $"+i[1]+",$"+i[3].split()[0]+","+i[4];
    elif i[3] == '<<':
      print "sll $"+i[0]+",$"+i[2]+",$"+i[4]
    elif i[3] == '>>':
      print "srl $"+i[0]+",$"+i[2]+",$"+i[4]
    elif i[3] == '+' :
      print "add $"+i[0]+",$"+i[2]+",$"+i[4]
    elif i[3] == '-' :
      print "sub $"+i[0]+",$"+i[2]+",$"+i[4]
    elif i[3] == '*':
      print "mult $"+i[2]+",$"+i[4]
      print "mflo $"+i[0]
    elif i[3] == '/':
      print "div $"+i[2]+",$"+i[4]
      print "mflo $"+i[0]
    elif i[3] == '%':
      print "div $"+i[2]+",$"+i[4]
      print "mfhi $"+i[0]

    elif i[1] == '=' and i[2]!= 'Lcall' :
      # print type(i[2]) 
      if type(i[2]) == type(10):
        print "lw $_temp, "+str(i[2]);
      else:
        print "lw $_temp, $"+i[2];
          
      print "sw $_temp, $"+i[0];
      
    elif i[2] == "== 1":
      print "beq $"+i[1]+",1,"+i[4];
    elif i[3] == "goto":
      print "b "+i[4] ;
    elif ":" in i[3]:
      print i[3] 
      
    
    # SCOPE.code.append(["if",p[3].holdingVariable,"== 1","goto",startLabelChild])
  

    
      
    # tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable
    

    

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

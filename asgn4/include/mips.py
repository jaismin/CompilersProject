varStart="temp"
globalTempShootDown=0;


def printCode123(currElement):
  # print len(currElement.tempvar)
  for i in currElement.code :
    print i
    for x in range(len(i)):
      # print i[x]
      if i[x] != None and type(i[x]) ==type("@") and "@" in i[x]:
        i[x] = i[x].replace("@", "")
        # print i[x]
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
      t1 = returnTemp()
      print "slt $"+t1+",$"+i[3].split()[0]+",$"+i[1]
      print "beq $"+t1+",1,"+i[4];
    elif  i[2] == '<' :
      t1 = returnTemp()
      print "slt $"+t1 +",$"+i[3].split()[0]+",$"+i[1]
      print "beq $"+t1+",$zero,"+i[4];
    elif i[2] == '>=':
      t1 = returnTemp()
      print "slt $"+t1+",$"+i[3].split()[0]+",$"+i[1]
      print "beq $"+t1+",1,"+i[4];
      print "beq $"+i[1]+",$"+i[3].split()[0]+",$"+i[4];
    elif  i[2] == '<=' :
      t1 = returnTemp();
      print "slt $"+t1 +",$"+i[3].split()[0]+",$"+i[1]
      print "beq $"+t1+",$zero,"+i[4];
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
      t1 = returnTemp();
      if type(i[2]) == type(10):
        print "li $"+t1+", "+str(i[2]);
      else:
        print "lw $"+t1+", $"+i[2];
          
      print "sw $"+t1+", $"+i[0];
      
    elif i[2] == "== 1":
      print "beq $"+i[1]+",1,"+i[4];
    elif i[3] == "goto":
      print "b "+i[4] ;
    elif ":" in i[3]:
      print i[3] 
      
    
    # SCOPE.code.append(["if",p[3].holdingVariable,"== 1","goto",startLabelChild])
  

    
      
    # tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable
    
def returnTemp():
  global globalTempShootDown
  globalTempShootDown+=1
  return varStart+"_"+str(globalTempShootDown)
    

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

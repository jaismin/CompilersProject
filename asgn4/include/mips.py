varStart="temp"
globalTempShootDown=0;

def loadStackAddress(SCOPE,currElement,variable):
  retval=list()
  if '__' in variable:
    startname=variable.split('__')[0]
    variable="__".join(variable.split('__')[1:])
    if (startname!=currElement.name):
      print 'Cannot support access links right now'
      print currElement.name
      print startname
      print variable
      assert(False)
  variable = variable.split( )[0]
  value=currElement.get_attribute_value(variable,'stackOffset',"symbol")
  retval.append(str(value)+"($fp)")
  return retval



def printCode123(SCOPE,currElement):
  # print len(currElement.tempvar)
  for i in currElement.code :
    print i
    t=dict()
    for x in range(len(i)):
      prev=""
      if (x>0):
        prev=i[x-1]
      # print i[x]
      if not (i[x]==None or type(i[x]) !=type("@") or ':' in i[x] or prev=='Lcall'):
        if ("@" in i[x]) or (len(i[x])>6 and i[x][0:4]=="node" and '__' in i[x]):
          if (i[x] != None and type(i[x]) ==type("@") and "@" in i[x]):
            i[x] = i[x].replace("@", "")
          retval=loadStackAddress(SCOPE,currElement,i[x])
          if (len(retval)>1):
            print 'Will handle access links here'
          else:
            t1 = returnTemp();
            i[x]=retval[0];
            print "lw $"+t1+", "+i[x];
            t[x]= t1;







        # print i[x]
    if i[3] == '|' :
      print "or "+t[0] +","+t[2]+","+t[4];
    elif i[3] == '^' :
      print "xor "+t[0] +","+t[2]+","+t[4];
    elif i[3] == '&' :
      print "and "+t[0] +","+t[2]+","+t[4];
    elif i[2] == '==':
      print "beq "+t[1]+","+t[3]+","+t[4];
    elif i[2] == '!=':
      print "bne "+t[1]+","+t[3]+","+t[4];
    elif i[2] == '>':
      t1 = returnTemp()
      print "slt $"+t1+","+t[3]+","+t[1]
      print "beq $"+t1+",1,"+i[4];
    elif  i[2] == '<' :
      t1 = returnTemp()
      print "slt $"+t1 +","+t[3]+","+t[1]
      print "beq $"+t1+",$zero,"+i[4];
    elif i[2] == '>=':
      t1 = returnTemp()
      print "slt $"+t1+","+t[3]+","+t[1]
      print "beq $"+t1+",1,"+i[4];
      print "beq "+t[1]+","+t[3]+","+i[4];
    elif  i[2] == '<=' :
      t1 = returnTemp();
      print "slt $"+t1 +","+t[3]+","+t[1]
      print "beq $"+t1+",$zero,"+i[4];
      print "beq "+t[1]+","+t[3]+","+i[4];
    elif i[3] == '<<':
      print "sll "+t[0]+","+t[2]+","+t[4]
    elif i[3] == '>>':
      print "srl "+t[0]+","+t[2]+","+t[4]
    elif i[3] == '+' :
      print "add "+t[0]+","+t[2]+","+t[4]
    elif i[3] == '-' :
      print "sub "+t[0]+","+t[2]+","+t[4]
    elif i[3] == '*':
      print "mult "+t[2]+","+t[4]
      print "mflo "+i[0]
    elif i[3] == '/':
      print "div "+t[2]+","+t[4]
      print "mflo "+i[0]
    elif i[3] == '%':
      print "div "+t[2]+","+t[4]
      print "mfhi "+i[0]

    elif i[1] == '=' and i[2]!= 'Lcall' :
      # print type(i[2]) 
      if type(i[2]) == type(10):
        t1 = returnTemp();
        print "li $"+t1+", "+str(i[2]);
      # else:
      #   # print i
      #   # print "lw $"+t1+", "+t[2];
          
      print "sw $"+t1+", "+i[0];
      
    elif i[2] == "== 1":
      print "beq "+t[1]+",1,"+i[4];
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
        
    printCode123(SCOPE,currElement)


def generateMips(SCOPE):
	traversetree123(SCOPE)

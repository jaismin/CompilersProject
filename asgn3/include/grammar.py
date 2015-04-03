from symbolTable import *
SCOPE = Env(None)                          # Current Scope
globalTemp=list()
globalLabel=1
globalFunc=1
registerSize=1000
varStart="@t"
labelStart="Label"
functionStart="Function"
for i in range(1,registerSize+1):
  globalTemp.append(0)


def returnTemp():
  global globalTemp
  temp=globalTemp[0]
  j=1
  while j<registerSize and temp==1:
    temp=globalTemp[j]
    j=j+1
    
  if (j==registerSize):
    print "Not enough variables"
  else :
    globalTemp[j-1]=1
    SCOPE.tempvar.add(varStart+"_"+str(j))
    return varStart+"_"+str(j)

def returnLabel():
  global globalLabel
  globalLabel+=1
  return labelStart+str(globalLabel)

def returnFunction():
  global globalFunc
  globalFunc+=1
  return functionStart+str(globalFunc)

def backpatch(listL1,string1):
  for i in listL1:
    SCOPE.code[i][4]=string1
    # [None,None,label+":",None,None]
    # append([None,None,label+":",None,None])

  

def freeVar(a):
  if a!=None:
    if varStart in a:
      b=int(a.split('_')[1])
      global globalTemp
      globalTemp[b-1]=0

def Updatep1(pnew):
  if pnew.isQualifiedName:
      # print p[1].value
    query=((pnew.value).split('.'))[0]
    query1=((pnew.value).split('.'))[1]
    # print query
    if SCOPE.is_present(query,updateField="symbol"):
      val1=SCOPE.get_attribute_value(query,'Type',"symbol")
      if "Object" in val1:
        pnew.value=val1.split('@')[1]+"@"+query1
        # print pnew.value
      else:
        print "No such object definition found at line,",p.lexer.lineno()
        raise Exception("Check your semantics! :P")
    else:
      print "No such variable found at line,",p.lexer.lineno()
      raise Exception("Check your semantics! :P")
  return pnew.value

def Updatehold(pnew):
  if pnew.isQualifiedName:
      # print p[1].value
    query=((pnew.holdingVariable).split('.'))[0]
    query1=((pnew.holdingVariable).split('.'))[1]
    # print query
    if SCOPE.is_present(query,updateField="symbol"):
      val1=SCOPE.get_attribute_value(query,'Type',"symbol")
      if "Object" in val1:
        pnew.holdingVariable=val1.split('@')[1]+"@"+query1
        # print pnew.value
      else:
        print "No such object definition found at line,",p.lexer.lineno()
        raise Exception("Check your semantics! :P")
    else:
      print "No such variable found at line,",p.lexer.lineno()
      raise Exception("Check your semantics! :P")
  return pnew.holdingVariable





class Node(object): 
    gid = 1   
    def __init__(self,name,children,dataType="Unit",val=None,size=None,argumentList=None,holdingVariable=None,trueList=None,falseList=None,nextList=None):
        self.name = name
        self.children = children
        self.id=Node.gid
        self.value=val
        self.size=size
        self.argumentList=argumentList
        self.dataType=dataType
        self.trueList = trueList;
        self.falseList = falseList
        self.nextList = nextList
        self.holdingVariable=holdingVariable
        self.isQualifiedName=False
        Node.gid+=1

def create_leaf(name1,name2,dataType="Unit"):
    leaf1 = Node(name2,[],dataType)
    leaf2 = Node(name1,[leaf1],dataType)
    return leaf2

def printCode(currElement):
  # print len(currElement.tempvar)
  for i in currElement.code :
    for j in range(5):
      if (i[j]!=None):
        if type(i[j])==str and "@t" in i[j]:
          print i[j][1:],
        else:
          print i[j],
    print 
  print 
  print


def traversetree():
  global SCOPE
  queue=list()
  queue.append(SCOPE)
  while len(queue) >0 :
    currElement=queue[0]
    del queue[0]
    for i in range (len(currElement.childs)):
      queue.append(currElement.childs[i])
    printCode(currElement)


def p_start_here(p):
  '''start_here : ProgramStructure end_here'''
  p[0] = Node("startOfProgram", [p[1], p[2]])



def p_end_here(p):
  '''end_here : empty '''
  p[0] = Node("endhere", [p[1]])
  traversetree()
  # SCOPE.subtree()


def p_program_structure(p):
    '''ProgramStructure : ProgramStructure  class_and_objects
                      | class_and_objects '''
    if len(p) == 3:
      if not (p[1].dataType=="Unit" and p[2].dataType=="Unit"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      p[0] = Node("ProgramStructure", [p[1], p[2]])
    else:
      if not (p[1].dataType=="Unit"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      p[0] = Node("ProgramStructure", [p[1]])
    
def p_class_and_objects(p):
  '''class_and_objects : SingletonObject
                       | class_declaration'''
  if not (p[1].dataType=="Unit"):
    print "Type Error at line  ",p.lexer.lineno
    raise Exception("Correct the above Semantics! :P")
  p[0] = Node("class_and_objects", [p[1]])

def p_SingletonObject(p):
    'SingletonObject : ObjectDeclare block'
    if not (p[1].dataType=="Unit" and p[2].dataType=="Unit" ):
      print "Type Error at line  ",p.lexer.lineno
      raise Exception("Correct the above Semantics! :P")
    p[0] = Node("SingletonObject", [p[1], p[2]])

   
# object declaration
def p_object_declare(p):
    '''ObjectDeclare : KWRD_OBJECT IDENTIFIER 
                | KWRD_OBJECT IDENTIFIER KWRD_EXTNDS IDENTIFIER'''
    if len(p) == 3:
      child1 = create_leaf("KWRD_OBJECT", p[1])
      child2 = create_leaf("IDENTIFIER", p[2])
      if not (child1.dataType=="Unit" and child2.dataType=="Unit"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      p[0] = Node("ObjectDeclare", [child1, child2])
    else:
      child1 = create_leaf("KWRD_OBJECT", p[1])
      child2 = create_leaf("IDENTIFIER", p[2])
      child3 = create_leaf("KWRD_EXTNDS", p[3])
      child4 = create_leaf("IDENTIFIER", p[4])
      if not (child1.dataType=="Unit" and child2.dataType=="Unit" and child3.dataType=="Unit" and child4.dataType=="Unit"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      p[0] = Node("ObjectDeclare", [child1, child2, child3, child4])


# expression
def p_expression(p):
    '''expression : assignment_expression'''
    p[0] = Node("expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)

def p_expression_optional(p):
        '''expression_optional : expression
                          | empty'''
        p[0] = Node("expression_optional", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)

def p_assignment_expression(p):
    '''assignment_expression : assignment
                             | conditional_or_expression'''

    returnHold=p[1].holdingVariable
    if p[1].trueList!=None and p[1].falseList!=None and (len(p[1].trueList) >0 or len(p[1].falseList) >0):
      truelabel=returnLabel()
      falselabel=returnLabel()
      jumplabel=returnLabel()
      retVar=returnTemp()
      SCOPE.code.append([None,None,truelabel+":",None,None])
      SCOPE.code.append([retVar,"=","1",None,None])
      SCOPE.code.append([None,None,None,"goto",jumplabel])
      SCOPE.code.append([None,None,falselabel+":",None,None])
      SCOPE.code.append([retVar,"=","0",None,None])
      SCOPE.code.append([None,None,jumplabel+":",None,None])
      backpatch(p[1].trueList,truelabel)
      backpatch(p[1].falseList,falselabel)
      returnHold=retVar
    elif p[1].trueList!=None and len(p[1].trueList) >0 :
      truelabel=returnLabel()
      retVar=returnTemp()
      SCOPE.code.append([None,None,truelabel+":",None,None])
      SCOPE.code.append([retVar,"=","1",None,None])
      backpatch(p[1].trueList,truelabel)
      returnHold=retVar

    elif p[1].falseList!=None and len(p[1].falseList) >0 :
      falselabel=returnLabel()
      retVar=returnTemp()
      SCOPE.code.append([None,None,falselabel+":",None,None])
      SCOPE.code.append([retVar,"=","0",None,None])
      backpatch(p[1].falseList,falselabel)
      returnHold=retVar
    else:
      pass
    p[0] = Node("assignment_expression", [p[1]],p[1].dataType,None,None,None,returnHold)
# assignment

def p_assignment(p):
    '''assignment : valid_variable assignment_operator assignment_expression'''
    if (p[1].dataType == p[3].dataType):
      pass
    # elif ((p[1].dataType=="Double" and p[3].dataType=="Int") or (p[3].dataType=="Double" and p[1].dataType=="Int")):
    #   print "Do type cast here "
    #   pass
    else:
      print "Type Error at line  ",p.lexer.lineno
      raise Exception("Correct the above Semantics! :P")

    if (p[2].value=="="):
      SCOPE.code.append([p[1].holdingVariable,"=",p[3].holdingVariable,None,None])
      freeVar(p[3].holdingVariable)
    else:
      val=p[2].value[0]
      tempVar=returnTemp()
      SCOPE.code.append([tempVar,"=",p[1].holdingVariable,None,None])
      SCOPE.code.append([p[1].holdingVariable,"=",tempVar,val,p[3].holdingVariable])
      freeVar(p[3].holdingVariable)
      freeVar(tempVar)
    # print p[1].holdingVariable," ",p[2].value," ",p[3].holdingVariable

    p[0] = Node("assignment", [p[1], p[2], p[3]],p[1].dataType)


def p_assignment_operator(p):
    '''assignment_operator :    ASSIGN
                               | TIMES_ASSIGN
                               | DIVIDE_ASSIGN
                               | REMAINDER_ASSIGN
                               | PLUS_ASSIGN
                               | MINUS_ASSIGN
                               | LSHIFT_ASSIGN
                               | RSHIFT_ASSIGN
                               | AND_ASSIGN
                               | OR_ASSIGN
                               | XOR_ASSIGN'''
    # print p.lineno

    child1 = create_leaf("ASSIGN_OP", p[1])
    p[0] = Node("assignment_operator", [child1],"Unit",p[1])        

def p_Marker(p):
    '''Marker : empty '''
    label=returnLabel()
    p[0] = Node("Marker", [p[1]],"Unit",label)      
    SCOPE.code.append([None,None,label+":",None,None])
  
# OR(||) has least precedence, and OR is left assosiative 
# a||b||c => first evalutae a||b then (a||b)||c
def p_conditional_or_expression(p):
    '''conditional_or_expression : conditional_and_expression
                                | conditional_or_expression OR Marker conditional_and_expression'''
    if len(p) == 2:
      p[0] = Node("conditional_or_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
    else:
      # handle using jump statements
      child1 = create_leaf("OR", p[2])
      if not (p[1].dataType=="Boolean" and p[4].dataType=="Boolean"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")

      p[0] = Node("conditional_or_expression", [p[1], child1, p[4]],p[1].dataType)
      backpatch(p[1].falseList,p[3].value)
      p[0].trueList = p[1].trueList+p[4].trueList;
      p[0].falseList = p[4].falseList;

# AND(&&) has next least precedence, and AND is left assosiative 
# a&&b&&c => first evalutae a&&b then (a&&b)&&c

def p_conditional_and_expression(p):
    '''conditional_and_expression : inclusive_or_expression
                                    | conditional_and_expression AND Marker inclusive_or_expression'''
    if len(p) == 2:
      p[0] = Node("conditional_and_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
    else:

      # handle later
      child1 = create_leaf("AND", p[2])
      if not (p[1].dataType=="Boolean" and p[4].dataType=="Boolean"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      p[0] = Node("conditional_and_expression", [p[1], child1, p[4]],p[1].dataType)
      backpatch(p[1].trueList, p[3].value)
      p[0].trueList = p[4].trueList
      p[0].falseList = p[1].falseList+p[4].falseList

def p_inclusive_or_expression(p):
    '''inclusive_or_expression : exclusive_or_expression
                                   | inclusive_or_expression OR_BITWISE exclusive_or_expression'''
    if len(p) == 2:
      p[0] = Node("inclusive_or_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
    else:
      child1 = create_leaf("OR_BITWISE", p[2])
      if not (p[1].dataType == "Int" and p[3].dataType == "Int"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      tempVar=returnTemp()
      SCOPE.code.append([tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable])
      freeVar(p[1].holdingVariable)
      freeVar(p[3].holdingVariable)
      # print tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable
      p[0] = Node("inclusive_or_expression", [p[1], child1, p[3]],p[1].dataType,None,None,None,tempVar)


def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                                   | exclusive_or_expression XOR and_expression'''
    if len(p) == 2:
      p[0] = Node("exclusive_or_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
    else:
      child1 = create_leaf("XOR", p[2])
      if not (p[1].dataType == "Int" and p[3].dataType == "Int"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      tempVar=returnTemp()
      SCOPE.code.append([tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable])
      freeVar(p[1].holdingVariable)
      freeVar(p[3].holdingVariable)
      # print tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable
      p[0] = Node("exclusive_or_expression", [p[1], child1, p[3]],p[1].dataType,None,None,None,tempVar)

def p_and_expression(p):
    '''and_expression : equality_expression
                          | and_expression AND_BITWISE equality_expression'''
    if len(p) == 2:
      p[0] = Node("and_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
    else:
      child1 = create_leaf("AND_BITWISE", p[2])
      if not (p[1].dataType == "Int" and p[3].dataType == "Int"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      tempVar=returnTemp()

      SCOPE.code.append([tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable])
      freeVar(p[1].holdingVariable)
      freeVar(p[3].holdingVariable)

      p[0] = Node("and_expression", [p[1], child1, p[3]],p[1].dataType,None,None,None,tempVar)

def p_equality_expression(p):
    '''equality_expression : relational_expression
                            | equality_expression EQUAL relational_expression 
                            | equality_expression NEQUAL relational_expression''' #Marker Marker
    if len(p) == 2:
      p[0] = Node("relational_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList

    else:
      child1 = create_leaf("EqualityOp", p[2])
      if not (p[1].dataType == p[3].dataType):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")

      p[0] = Node("relational_expression", [p[1], child1, p[3]],"Boolean",None,None,None,None)
      SCOPE.code.append(["if",p[1].holdingVariable,p[2],p[3].holdingVariable+" goto",None])
      p[0].trueList=list()
      (p[0].trueList).append(len(SCOPE.code)-1)
      SCOPE.code.append([None,None,None,"goto",None])
      p[0].falseList=list()
      (p[0].falseList).append(len(SCOPE.code)-1)
      freeVar(p[1].holdingVariable)
      freeVar(p[3].holdingVariable)
      


def p_relational_expression(p):
    '''relational_expression : shift_expression
                                 | relational_expression GREATER shift_expression
                                 | relational_expression LESS shift_expression
                                 | relational_expression GEQ shift_expression
                                 | relational_expression LEQ shift_expression'''
    if len(p) == 2:
      p[0] = Node("relational_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
      
    else:
      child1 = create_leaf("RelationalOp", p[2])
      if not (p[1].dataType == p[3].dataType):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      
      p[0] = Node("relational_expression", [p[1], child1, p[3]],"Boolean",None,None,None,None)
      SCOPE.code.append(["if",p[1].holdingVariable,p[2],p[3].holdingVariable+" goto",None])
      p[0].trueList=list()
      (p[0].trueList).append(len(SCOPE.code)-1)
      SCOPE.code.append([None,None,None,"goto",None])
      p[0].falseList=list()
      (p[0].falseList).append(len(SCOPE.code)-1)
      freeVar(p[1].holdingVariable)
      freeVar(p[3].holdingVariable)

def p_shift_expression(p):
        '''shift_expression : additive_expression
                            | shift_expression LSHIFT additive_expression
                            | shift_expression RSHIFT additive_expression'''
        if len(p) == 2:
          p[0] = Node("shift_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
          p[0].trueList=p[1].trueList
          p[0].falseList=p[1].falseList
        else:
          child1 = create_leaf("ShiftOp", p[2])
          if not (p[1].dataType == p[3].dataType and p[1].dataType=="Int"):
            print "Type Error at line  ",p.lexer.lineno
            raise Exception("Correct the above Semantics! :P")
          tempVar=returnTemp()
          SCOPE.code.append([tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable])
          freeVar(p[1].holdingVariable)
          freeVar(p[3].holdingVariable)
      
          p[0] = Node("shift_expression", [p[1], child1, p[3]],p[1].dataType,None,None,None,tempVar)
          # p[0].trueList=p[1].trueList
          # p[0].falseList=p[1].falseList
       

def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                               | additive_expression PLUS multiplicative_expression
                               | additive_expression MINUS multiplicative_expression'''
    if len(p) == 2:
      p[0] = Node("additive_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
    else:
      child1 = create_leaf("AddOp", p[2])
      currType="Int"
      if (p[1].dataType=="Int" and p[3].dataType=="Int"):
        currType="Int"
      elif (p[1].dataType=="Int" and p[3].dataType=="Double"):
        currType="Double"
      elif (p[1].dataType=="Double" and p[3].dataType=="Double"):
        currType="Double"
      elif (p[1].dataType=="Double" and p[3].dataType=="Int"):
        currType="Double"
      elif (p[1].dataType=="String" and p[3].dataType=="String" and p[2]=="+"):
        currType="String"
      else:
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      tempVar=returnTemp()

      SCOPE.code.append([tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable])
      freeVar(p[1].holdingVariable)
      freeVar(p[3].holdingVariable)

      p[0] = Node("additive_expression", [p[1], child1, p[3]],currType,None,None,None,tempVar)
      # p[0].trueList=p[1].trueList
      # p[0].falseList=p[1].falseList
   

def p_multiplicative_expression(p):
    '''multiplicative_expression : unary_expression
                                     | multiplicative_expression TIMES unary_expression
                                     | multiplicative_expression DIVIDE unary_expression
                                     | multiplicative_expression REMAINDER unary_expression'''
    if len(p) == 2:
      p[0] = Node("multiplicative_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
    else:
      child1 = create_leaf("MultOp", p[2])
      currType="Int" 
      if (p[1].dataType=="Int" and p[3].dataType=="Int"):
        currType="Int"
      elif (p[1].dataType=="Int" and p[3].dataType=="Double" and p[2] != "%"):
        currType="Double"
      elif (p[1].dataType=="Double" and p[3].dataType=="Double" and p[2] != "%"):
        currType="Double"
      elif (p[1].dataType=="Double" and p[3].dataType=="Int" and p[2] != "%"):
        currType="Double"
      else:
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")

      tempVar=returnTemp()

      SCOPE.code.append([tempVar,"=",p[1].holdingVariable,p[2],p[3].holdingVariable])
      freeVar(p[1].holdingVariable)
      freeVar(p[3].holdingVariable)

      p[0] = Node("multiplicative_expression", [p[1], child1, p[3]],currType,None,None,None,tempVar)
      # p[0].trueList=p[1].trueList
      # p[0].falseList=p[1].falseList
    

def p_unary_expression(p):
    '''unary_expression : PLUS unary_expression
                            | MINUS unary_expression
                            | unary_expression_not_plus_minus'''
    if len(p) == 3:
      if not (p[2].dataType == "Int" or p[2].dataType=="Double"):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      
      tempVar1=returnTemp()
      # print tempVar1,"= 0"

      tempVar=returnTemp()
      # print tempVar,"=",tempVar1,p[1],p[2].holdingVariable



      SCOPE.code.append([tempVar1,"=","0",None,None])
      SCOPE.code.append([tempVar,"=",tempVar1,p[1],p[2].holdingVariable])
      
      freeVar(p[2].holdingVariable)
      freeVar(tempVar1)

      child1 = create_leaf("UnaryOp", p[1])
      p[0] = Node("unary_expression", [child1, p[2]],p[2].dataType,None,None,None,tempVar)
      p[0].trueList=p[2].trueList
      p[0].falseList=p[2].falseList
    else:
      p[0] = Node("unary_expression", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList


def p_unary_expression_not_plus_minus(p):
    '''unary_expression_not_plus_minus : base_variable_set
                                           | NOT unary_expression
                                           | cast_expression'''
    if len(p) == 2:
      p[0] = Node("unary_expression_not_plus_minus", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
      p[0].trueList=p[1].trueList
      p[0].falseList=p[1].falseList
    else:
      if (p[2].dataType=="Boolean"):
        pass
      else:
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")

      child1 = create_leaf("Unary_1Op", p[1])
      p[0] = Node("unary_expression_not_plus_minus", [child1, p[2]],p[2].dataType,None,None,None,None)
      p[0].trueList=p[2].falseList
      p[0].falseList=p[2].trueList
def p_unary_expression_not_plus_minus_1(p):
    '''unary_expression_not_plus_minus : TILDA unary_expression '''
    if (p[2].dataType=="Int"):
      pass
    else:
      print "Type Error at line  ",p.lexer.lineno
      raise Exception("Correct the above Semantics! :P")

    child1 = create_leaf("Unary_1Op", p[1])
    tempVar=returnTemp()
    SCOPE.code.append([tempVar,"=",None,p[1],p[2].holdingVariable])
    freeVar(p[2].holdingVariable)
    p[0] = Node("unary_expression_not_plus_minus", [child1, p[2]],p[2].dataType,None,None,None,tempVar)
    p[0].trueList=p[2].trueList
    p[0].falseList=p[2].falseList

def p_base_variable_set(p):
  '''base_variable_set : variable_literal
                        | LPAREN expression RPAREN'''
  if len(p) == 2:
    p[0] = Node("base_variable_set", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
    p[0].trueList=p[1].trueList
    p[0].falseList=p[1].falseList
  else:
    child1 = create_leaf("LPAREN", p[1])
    child2 = create_leaf("RPAREN", p[3])
    p[0] = Node("base_variable_set", [child1, p[2], child2],p[2].dataType,None,None,None,p[2].holdingVariable)
    p[0].trueList=p[2].trueList
    p[0].falseList=p[2].falseList

def p_cast_expression(p):
        '''cast_expression : LPAREN primitive_type RPAREN unary_expression'''

        flag=0
        currType="Int"
        if (p[2].dataType=="Unit" and (p[4].dataType=="Double" or p[4].dataType=="Int")):
          if (p[2].value=="Int" or p[2].value=="Double"):
            flag=1
            if (p[2].value=="Int"):
              currType="Int"
            elif (p[2].value=="Double"):
              currType="Double"
          else:
            flag=2

        if (flag==0):
          print "Type Error at line  ",p.lexer.lineno
          raise Exception("Correct the above Semantics! :P")
        elif (flag==2):
          print "Cast Error at line  ",p.lexer.lineno
          raise Exception("Correct the above Semantics! :P")

        tempVar=returnTemp()
        SCOPE.code.append([tempVar,"=",None,"("+p[2].value+")",p[4].holdingVariable])
        freeVar(p[4].holdingVariable)
        # print tempVar,"=","cast to",p[2].value,p[4].holdingVariable


        
        child1 = create_leaf("LPAREN", p[1])
        child2 = create_leaf("RPAREN", p[3])
        p[0] = Node("cast_expression", [child1, p[2], child2, p[4]],currType,None,None,None,tempVar)
        p[0].trueList=p[4].trueList
        p[0].falseList=p[4].falseList
       

def p_primary(p):
    '''primary : literal
                | method_invocation'''
    p[0] = Node("primary", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
    p[0].trueList=p[1].trueList
    p[0].falseList=p[1].falseList



def p_literal_1(p):
  '''literal : int_float'''
  p[0] = Node("literal", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
  p[0].trueList=p[1].trueList
  p[0].falseList=p[1].falseList


def p_literal_2(p):
  '''literal : CHARACTER'''
  child1 = create_leaf("LiteralConst", p[1],"Char")
  tempVar=returnTemp()
  SCOPE.code.append([tempVar,"=",p[1],None,None])
  p[0] = Node("literal", [child1],"Char",None,None,None,tempVar)
  p[0].trueList=p[1].trueList
  p[0].falseList=p[1].falseList

def p_literal_3(p):
  '''literal : STRING_CONST'''
  child1 = create_leaf("LiteralConst", p[1],"String")
  tempVar=returnTemp()
  SCOPE.code.append([tempVar,"=",p[1],None,None])
  p[0] = Node("literal", [child1],"String",None,None,None,tempVar)
  p[0].trueList=p[1].trueList
  p[0].falseList=p[1].falseList
  

def p_literal_4(p):
  '''literal : BOOL_CONSTT'''
  child1 = create_leaf("LiteralConst", p[1],"Boolean")
  # tempVar=returnTemp()
  # SCOPE.code.append([tempVar,"=",p[1],None,None])
  p[0] = Node("literal", [child1],"Boolean",None,None,None,None)
  SCOPE.code.append([None,None,None,"goto",None])
  p[0].trueList=list()
  (p[0].trueList).append(len(SCOPE.code)-1)

def p_literal_7(p):
  '''literal : BOOL_CONSTF'''
  child1 = create_leaf("LiteralConst", p[1],"Boolean")
  p[0] = Node("literal", [child1],"Boolean",None,None,None,None)
  SCOPE.code.append([None,None,None,"goto",None])
  p[0].falseList=list()
  (p[0].falseList).append(len(SCOPE.code)-1)
  

def p_literal_5(p):
  '''literal : KWRD_NULL'''
  child1 = create_leaf("LiteralConst", p[1],"Unit")
  tempVar=returnTemp()
  SCOPE.code.append([tempVar,"=",p[1],None,None])
  p[0] = Node("literal", [child1],"Unit",None,None,None,tempVar)
  

def p_int_float_1(p):
    '''int_float : FLOAT_CONST'''
    child1 = create_leaf("FloatConst", p[1],"Double")
    tempVar=returnTemp()
    SCOPE.code.append([tempVar,"=",p[1],None,None])
    p[0] = Node("int_float", [child1],"Double",None,None,None,tempVar)

def p_int_float_2(p):
    '''int_float : INT_CONST'''
    child1 = create_leaf("IntConst", p[1],"Int")
    tempVar=returnTemp()
    SCOPE.code.append([tempVar,"=",p[1],None,None])
    p[0] = Node("int_float", [child1],"Int",None,None,None,tempVar)


def p_method_invocation(p):
    '''method_invocation : name LPAREN argument_list_opt RPAREN '''
    child1 = create_leaf("LPAREN", p[2])
    child2 = create_leaf("RPAREN", p[4])
    val=""
    retType=""
    print "QualifiedName:",p[1].isQualifiedName
    oldVal=p[1].value
    if p[1].isQualifiedName:
      oldVal=oldVal.split('.')[1]
    p[1].value=Updatep1(p[1])

    if SCOPE.is_present(p[1].value,updateField="function"):
      val=SCOPE.get_attribute_value(p[1].value,'Type',"function")
      retType=SCOPE.get_attribute_value(p[1].value,'returnType',"function")
      if (val==p[3].dataType):
        pass
      else:
        print "Mismatch in arguement types to invoke the function at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
    else:
      print "Function is not defined at line ",p.lexer.lineno
      raise Exception("Correct the above Semantics! :P")
    p[0] = Node("method_invocation", [p[1], child1, p[3], child2],retType)


    for i in p[3].holdingVariable:
      j=i

      if varStart in i:
        i=i[1:]
      SCOPE.code.append([None,None,None,"PushParam",i])
      freeVar(j)

    holding=None
    if (retType!="Unit"):
      holding=returnTemp()
      SCOPE.code.append([holding,"=","Lcall",SCOPE.get_attribute_append_name(p[1].value,updateField="function").name+"__"+oldVal,None])
    else:
      SCOPE.code.append([None,None,"Lcall",SCOPE.get_attribute_append_name(p[1].value,updateField="function").name+"__"+oldVal,None])

    SCOPE.code.append([None,None,None,"PopParam",len(p[3].holdingVariable)*4])
    p[0].holdingVariable=holding
    






        

def p_array_access(p):
    '''array_access : name LBPAREN expression RBPAREN '''
    child1 = create_leaf("LBPAREN", p[2])
    child2 = create_leaf("RBPAREN", p[4])
    val1=list()
    oldVal=p[1].value
    p[1].value=Updatep1(p[1])
    if SCOPE.is_present(p[1].value,updateField="symbol"):
      val=SCOPE.get_attribute_value(p[1].value,'Type',"symbol")
      val1=val.split(",")
      if (val1[0]!="Array"):
        print "Array Undefined at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      if (p[3].dataType=="Int"):
        pass
      else:
        print "Only Integer Indices Allowed at line ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
    else:
      print "Array Undefined at line  ",p.lexer.lineno
      raise Exception("Correct the above Semantics! :P")
    p[0] = Node("array_access", [p[1], child1, p[3], child2],",".join(val1[1:]))  
    temp= returnTemp()
    SCOPE.code.append([temp,"=","4",None,None])
    temp1= returnTemp()
    SCOPE.code.append([temp1,"=",temp,"*",p[3].holdingVariable])
    SCOPE.code.append([temp,"=",SCOPE.get_attribute_append_name(p[1].value,updateField="symbol").name+"__"+oldVal,"+",temp1])
    SCOPE.code.append([temp1,"=*","(",temp,")"])
    freeVar(temp)
    p[0].holdingVariable=temp1
    






def p_argument_list_opt(p):
    '''argument_list_opt : argument_list'''
    p[0] = Node("argument_list_opt", [p[1]],p[1].dataType)
    p[0].holdingVariable=p[1].holdingVariable


def p_argument_list_opt2(p):
    '''argument_list_opt : empty'''
    p[0] = Node("argument_list_opt", [p[1]],p[1].dataType)
    p[0].holdingVariable=p[1].holdingVariable
        

def p_argument_list(p):
    '''argument_list : expression
                    | argument_list COMMA expression'''
    if len(p) == 2:
      newType_1 = list()
      newType_1.append(p[1].dataType)
      newHolding = list()
      newHolding.append(p[1].holdingVariable)

      p[0] = Node("argument_list", [p[1]],newType_1)
      p[0].holdingVariable=newHolding
      
      

    else:
      newType_1 = list(p[1].dataType)
      newType_2 = list()
      newType_2.append(p[3].dataType)


      newHold_1 = list(p[1].holdingVariable)
      newHold_2 = list()
      newHold_2.append(p[3].holdingVariable)


      child1 = create_leaf("COMMA", p[2])
      p[0] = Node("argument_list", [p[1], child1, p[3]],newType_1+newType_2)
      p[0].holdingVariable=newHold_1+newHold_2
    



# object identifier and identifier names for left hand assignment

def p_name(p):
    '''name : simple_name
            | qualified_name'''
    p[0] = Node("name", [p[1]],"Unit",p[1].value,None,None,p[1].holdingVariable)
    p[0].isQualifiedName=p[1].isQualifiedName
    

def p_simple_name(p):
    '''simple_name : IDENTIFIER'''
    child1 = create_leaf("IDENTIFIER", p[1])
    p[0] = Node("simple_name", [child1],"Unit",p[1],None,None,p[1])
    

def p_qualified_name(p):
    '''qualified_name : name DOT simple_name'''
    child1 = create_leaf("DOT", p[2])
    p[0] = Node("qualified_name", [p[1], child1, p[3]])
    p[0].isQualifiedName=True
    p[0].value=p[1].value+"."+p[3].value
    p[0].holdingVariable=p[0].value
   

def p_valid_variable(p):
    '''valid_variable : name'''
    val=""
    # print p[1].value
    oldVal=p[1].value
    p[1].value=Updatep1(p[1])
    # p[1].holdingVariable=Updatehold(p[1])
    if SCOPE.is_present(p[1].value,updateField="symbol"):
      val=SCOPE.get_attribute_value(p[1].value,'Type',"symbol")
    else:
      print "Variable undefined at line ",p.lexer.lineno
      raise Exception("Correct the above Semantics! :P")


    node=SCOPE.get_attribute_append_name(p[1].value,updateField="symbol")
    nodename=node.name+"__"+oldVal
    
    if (node.objName!=None and p[1].isQualifiedName==False):
      offset=SCOPE.get_attribute_value(p[1].value,'Offset',"symbol")

      currScope=SCOPE
      while(currScope!=None and currScope!=node):
          print 
          if (currScope.funcName!=None):
            nodename="*(this+"+str(offset)+")"
            break
          currScope=currScope.prev_env
            
      
      
      

      
    # SCOPE.CheckValidParentObject(nodeName,oldVal.split)

    p[0] = Node("valid_variable", [p[1]],val,None,None,None,nodename)

def p_valid_variable_1(p):
    '''valid_variable : array_access'''
    p[0] = Node("valid_variable", [p[1]],p[1].dataType)  
    p[0].holdingVariable=p[1].holdingVariable


def p_variableliteral(p):
    '''variable_literal : valid_variable
                        | primary'''
    p[0] = Node("variable_literal", [p[1]],p[1].dataType,None,None,None,p[1].holdingVariable)
    p[0].falseList=p[1].falseList
    p[0].trueList=p[1].trueList


# BLOCK STATEMENTS


# def p_block(p):
#       '''block : BLOCK_BEGIN block_statements_opt BLOCK_END '''
#       child1 = create_leaf("BLOCK_BEGIN", p[1])
#       child2 = create_leaf("BLOCK_END", p[3])
#       p[0] = Node("block", [child1, p[2], child2])
       
def p_block(p):
      '''block : start_scope block_statements_opt end_scope'''
      p[0] = Node("block", [p[1], p[2], p[3]])

def p_start_scope(p):
      '''start_scope : BLOCK_BEGIN'''
      global SCOPE
      NEW_SCOPE = Env(SCOPE) 
      PREV_SCOPE=SCOPE
      SCOPE=NEW_SCOPE
      if (PREV_SCOPE.startChildBlock!=None):
        SCOPE.code.append([None,None,PREV_SCOPE.startChildBlock+":",None,None])
        PREV_SCOPE.startChildBlock=None

      child1 = create_leaf("BLOCK_BEGIN", p[1])
      p[0] = Node("start_scope", [child1])


def p_end_scope(p):  
      '''end_scope : BLOCK_END'''
      global SCOPE
      PREV_SCOPE=SCOPE.prev_env

      if (PREV_SCOPE.endChildBlock!=None):
        SCOPE.code.append([None,None,None,"goto",PREV_SCOPE.endChildBlock])
        PREV_SCOPE.endChildBlock=None


      SCOPE=PREV_SCOPE
      
      # SCOPE.subtree()
      child1 = create_leaf("BLOCK_END", p[1]) 
      p[0] = Node("end_scope", [child1])

def p_block_statements_opt(p):
      '''block_statements_opt : block_statements'''
      p[0] = Node("block_statements_opt", [p[1]],p[1].dataType)
      

def p_block_statements_opt2(p):
    '''block_statements_opt : empty'''
    p[0] = Node("block_statements_opt", [p[1]],p[1].dataType)
   

def p_block_statements(p):
      '''block_statements : block_statement
                            | block_statements block_statement'''
      if len(p) == 2:
        p[0] = Node("block_statement", [p[1]])
      else:
        p[0] = Node("block_statement", [p[1], p[2]])
      

def p_block_statement(p):
      '''block_statement : local_variable_declaration_statement
                           | statement
                           | class_declaration
                           | SingletonObject
                           | method_declaration'''
      p[0] = Node("block_statement", [p[1]],p[1].dataType)

# var (a:Int)=(h);
# var (a:Int,b:Int,c:Int)=(1,2,3);
# var (a:Int)=(h)
# var (a:Int,b:Int,c:Int)=(1,2,3)
# supported

def p_modifier_opts(p):
  '''modifier_opts : modifier
                    | empty '''
  p[0] = Node("modifier_opts", [p[1]],p[1].dataType)

def p_declaration_keyword(p):
  '''declaration_keyword : KWRD_VAR
                    | KWRD_VAL '''
  child1 = create_leaf("KWRD VAR/VAL", p[1])
  p[0] = Node("declaration_keyword", [child1])


def p_local_variable_declaration_statement(p):
      '''local_variable_declaration_statement : local_variable_declaration STATE_END '''
      child1 = create_leaf("STATE_END", p[2])
      p[0] = Node("local_variable_declaration_statement", [p[1], child1])

# 
def p_local_variable_declaration(p):
      '''local_variable_declaration : modifier_opts declaration_keyword variable_declaration_body'''
      p[0] = Node("local_variable_declaration", [p[1], p[2], p[3]])
     

def p_variable_declaration_initializer(p):
  '''variable_declaration_initializer : expression
                                      | array_initializer
                                      | class_initializer'''
  p[0] = Node("variable_declaration_initializer", [p[1]],p[1].dataType,p[1].value,p[1].size,p[1].argumentList,p[1].holdingVariable)

def p_variable_arguement_list(p):
  ''' variable_arguement_list : variable_declaration_initializer
                    | variable_arguement_list COMMA variable_declaration_initializer'''
  if len(p) == 2:
    newType_1 = list()
    newType_1.append(p[1].dataType)

    newSize_1 = list()
    newSize_1.append(p[1].size)

    newArg_1 = list()
    newArg_1.append(p[1].argumentList)

    newHold_1 = list()
    newHold_1.append(p[1].holdingVariable)

    # print p[1].dataType
    # print newType_1
    p[0] = Node("variable_arguement_list", [p[1]],newType_1,None,newSize_1,newArg_1,newHold_1)
  else:
    child1 = create_leaf("COMMA", p[2])
    newType_1 = list(p[1].dataType)
    newType_2 = list()
    newType_2.append(p[3].dataType)



    newSize_1 = list(p[1].size)
    newSize_2 = list()
    newSize_2.append(p[3].size)


    newArg_1 = list(p[1].argumentList)
    newArg_2 = list()
    newArg_2.append(p[3].argumentList)


    newHold_1 = list(p[1].holdingVariable)
    newHold_2 = list()
    newHold_2.append(p[3].holdingVariable)



    # print newType_1
    # print newType_2
    p[0] = Node("variable_arguement_list", [p[1], child1, p[3]],newType_1+newType_2,None,newSize_1+newSize_2,newArg_1+newArg_2,newHold_1+newHold_2)

def p_variable_declaration_body_1(p):
      '''variable_declaration_body : variable_declarator ASSIGN  variable_declaration_initializer '''
      
      if (p[1].dataType!=p[3].dataType):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      else:
        # print type(p[3].size)
        # print p[3].size
        if (p[3].size!=None):
          SCOPE.update_entry(p[1].value,'Size',int((p[3].size)),updateField="symbol")
        #SCOPE.print_table()
      # print p[3].holdingVariable
      if ("Array" in p[1].dataType):
        j=0
        for i in p[3].holdingVariable:
          temp= returnTemp()
          SCOPE.code.append([temp,"=","4",None,None])
          temp2=returnTemp()
          SCOPE.code.append([temp2,"=",j,None,None])
          temp1= returnTemp()
          SCOPE.code.append([temp1,"=",temp,"*",temp2])
          SCOPE.code.append([temp,"=",SCOPE.get_attribute_append_name(p[1].value,updateField="symbol").name+"__"+p[1].value,"+",temp1])
          SCOPE.code.append([temp1,"=*","(",temp,")"])
          SCOPE.code.append([temp1,"=",i,None,None])
          freeVar(temp1)
          freeVar(temp)
          freeVar(temp2)
          freeVar(i)
          j=j+1

        
      elif ("Object" in p[1].dataType):
        pass
      else:
        SCOPE.code.append([SCOPE.get_attribute_append_name(p[1].value,updateField="symbol").name+"__"+p[1].value,"=",p[3].holdingVariable,None,None])
        SCOPE.tempvar.add(SCOPE.get_attribute_append_name(p[1].value,updateField="symbol").name+"__"+p[1].value)
        freeVar(p[3].holdingVariable)
      # print p[1].dataType
      # for i123 in range (len(p[1].holdingVariable)):

      child1 = create_leaf("ASSIGN", p[2])
      p[0] = Node("variable_declaration_body", [p[1], child1, p[3]])
        


def p_variable_declaration_body_2(p):
      '''variable_declaration_body : LPAREN variable_declarators RPAREN ASSIGN LPAREN variable_arguement_list RPAREN'''
  
      child1 = create_leaf("LPAREN", p[1])
      child2 = create_leaf("RPAREN", p[3])
      child3 = create_leaf("ASSIGN", p[4])
      child4 = create_leaf("LPAREN", p[5])
      child5 = create_leaf("RPAREN", p[7])
      # print p[2].dataType
      # print p[6].dataType
      if (p[2].dataType!=p[6].dataType):
        print "Type Error at line  ",p.lexer.lineno
        raise Exception("Correct the above Semantics! :P")
      else :

        for i123 in range(len(p[2].value)):
          if ("Array" in (p[2].dataType)[i123]):
            j=0
            for i in (p[6].holdingVariable)[i123]:
              temp= returnTemp()
              SCOPE.code.append([temp,"=","4",None,None])
              temp1= returnTemp()
              temp2=returnTemp()
              SCOPE.code.append([temp2,"=",j,None,None])
              SCOPE.code.append([temp1,"=",temp,"*",temp2])
              SCOPE.code.append([temp,"=",SCOPE.get_attribute_append_name((p[2].value)[i123],updateField="symbol").name+"__"+(p[2].value)[i123],"+",temp1])
              SCOPE.code.append([temp1,"=*","(",temp,")"])
              SCOPE.code.append([temp1,"=",i,None,None])
              freeVar(temp1)
              freeVar(temp)
              freeVar(temp2)
              freeVar(i)
              j=j+1
          elif ("Object" in (p[2].dataType)[i123]):
            pass
          else:
            newName=SCOPE.get_attribute_append_name((p[2].value)[i123],updateField="symbol").name+"__"+(p[2].value)[i123]
            SCOPE.code.append([newName,"=",(p[6].holdingVariable)[i123],None,None])
            SCOPE.tempvar.add(newName)
            freeVar((p[6].holdingVariable)[i123])


          
        for i1 in range(len(p[2].value)):
          if (p[6].size)[i1] != None:
            SCOPE.update_entry((p[2].value)[i1],'Size',int((p[6].size)[i1]),updateField="symbol")
        #SCOPE.print_table()

      p[0] = Node("variable_declaration_body", [child1, p[2], child2, child3, child4, p[6], child5])

#left 
def p_variable_declaration_body_3(p):
  ''' variable_declaration_body : IDENTIFIER ASSIGN LPAREN func_arguement_list_opt RPAREN FUNTYPE expression'''      
  
  child1 = create_leaf("IDENTIFIER", p[1])
  child2 = create_leaf("ASSIGN", p[2])
  child3 = create_leaf("LPAREN", p[3])
  child4 = create_leaf("RPAREN", p[5])
  child5 = create_leaf("FUNTYPE", p[6])
  p[0] = Node("variable_declaration_body", [child1, child2, child3, p[4], child4, child5,p[7]])

def p_variable_declarators(p):
      '''variable_declarators : variable_declarator
                                | variable_declarators COMMA variable_declarator'''
      if len(p) == 2:
        newType_1 = list()
        newType_1.append(p[1].dataType)

        newValue_1 = list()
        newValue_1.append(p[1].value)

        p[0] = Node("variable_declarators", [p[1]],newType_1,newValue_1)
      else:
        newType_1 = list(p[1].dataType)
        newType_2 = list()
        newType_2.append(p[3].dataType)

        newValue_1 = list(p[1].value)
        newValue_2 = list()
        newValue_2.append(p[3].value)


        child1 = create_leaf("COMMA", p[2])
        p[0] = Node("variable_declarators", [p[1], child1, p[3]],newType_1+newType_2,newValue_1+newValue_2)
  

def p_variable_declarator(p):
      '''variable_declarator : variable_declarator_id'''
      p[0] = Node("variable_declarator", [p[1]],p[1].dataType,p[1].value)


def p_variable_declarator_id(p):
      '''variable_declarator_id : IDENTIFIER COLON type'''

      #Insert in symbol table
      attribute=dict()
      attribute['Type']=p[3].value
      # print 'Hello'+p[3].value
      SCOPE.add_entry(p[1],attribute,"symbol")
      child1 = create_leaf("IDENTIFIER", p[1])
      child2 = create_leaf("COLON", p[2])
      p[0] = Node("variable_declarator_id", [child1, child2, p[3]],p[3].value,p[1])
      # p[0] = Variable(p[1], dimensions=p[2])


def p_statement(p):
        '''statement : normal_statement 
                     | if_else_statement
                     | while_statement
                     | do_while_statement
                     | for_statement'''
        p[0] = Node("statement", [p[1]],p[1].dataType)


def p_normal_statement(p):
        '''normal_statement : block 
                             | expression_statement
                             | empty_statement
                             | return_statement
                             | switch_statement'''
 
        p[0] = Node("normal_statement", [p[1]],p[1].dataType)
 


def p_expression_statement(p):
        '''expression_statement : statement_expression STATE_END'''
        child1 = create_leaf("STATE_END", p[2])
        p[0] = Node("expression_statement", [p[1], child1])
                               

def p_statement_expression(p):
        '''statement_expression : assignment
                                | method_invocation'''
            
        p[0] = Node("statement_expression", [p[1]],p[1].dataType)
    

# def p_if_then_statement(p):
#         '''if_then_statement : KWRD_IF LPAREN expression RPAREN block'''
#         child1 = create_leaf("IF", p[1])
#         child2 = create_leaf("LPAREN", p[2])
#         child3 = create_leaf("RPAREN", p[4])
#         if (p[3].dataType!="Boolean"):
#           print "Conditional If only accepts boolean expression at line",p.lexer.lineno
#           raise Exception("Correct the above Semantics! :P")
#         p[0] = Node("if_then_statement", [child1, child2, p[3], child3, p[5]])
        

# def p_if_then_else_statement(p):
#         '''if_then_else_statement : KWRD_IF LPAREN expression RPAREN if_then_else_intermediate KWRD_ELSE block'''
#         child1 = create_leaf("IF", p[1])
#         child2 = create_leaf("LPAREN", p[2])
#         child3 = create_leaf("RPAREN", p[4])
#         child4 = create_leaf("ELSE", p[6])
#         if (p[3].dataType!="Boolean"):
#           print "Conditional If only accepts boolean expression at line",p.lexer.lineno
#           raise Exception("Correct the above Semantics! :P")
#         p[0] = Node("if_then_else_statement", [child1, child2, p[3], child3, p[5], child4, p[7]])
       

# def p_if_then_else_statement_precedence(p):
#         '''if_then_else_statement_precedence : KWRD_IF LPAREN expression RPAREN if_then_else_intermediate KWRD_ELSE if_then_else_intermediate'''
#         child1 = create_leaf("IF", p[1])
#         child2 = create_leaf("LPAREN", p[2])
#         child3 = create_leaf("RPAREN", p[4])
#         child4 = create_leaf("ELSE", p[6])
#         if (p[3].dataType!="Boolean"):
#           print "Conditional If only accepts boolean expression at line",p.lexer.lineno
#           raise Exception("Correct the above Semantics! :P")
#         p[0] = Node("if_then_else_statement_precedence", [child1, child2, p[3], child3, p[5], child4, p[7]])
      

# def p_if_then_else_intermediate(p):
#         '''if_then_else_intermediate : block
#                                               | if_then_else_statement_precedence'''
#         p[0] = Node("if_then_else_intermediate", [p[1]])

def p_start_scope_if(p):
      '''start_scope_if : BLOCK_BEGIN'''
      global SCOPE
      NEW_SCOPE = Env(SCOPE) 
      PREV_SCOPE=SCOPE
      SCOPE=NEW_SCOPE
      if (PREV_SCOPE.startChildBlock!=None):
        SCOPE.code.append([None,None,None,PREV_SCOPE.startChildBlock+":",None])
        PREV_SCOPE.startChildBlock=None
      
      child1 = create_leaf("BLOCK_BEGIN", p[1])
      p[0] = Node("start_scope_if", [child1])


def p_end_scope_if(p):  
      '''end_scope_if : BLOCK_END'''
      global SCOPE
      PREV_SCOPE=SCOPE.prev_env

      if (PREV_SCOPE.endChildBlock!=None):
        SCOPE.code.append([None,None,None,"goto",PREV_SCOPE.endChildBlock])


      SCOPE=PREV_SCOPE
      
      # SCOPE.subtree()
      child1 = create_leaf("BLOCK_END", p[1]) 
      p[0] = Node("end_scope_if", [child1])


def p_MarkIfStart(p):
  '''MarkIfStart : empty'''
  endLabel=returnLabel()
  SCOPE.endChildBlock=endLabel
  p[0] = Node("MarkIfStart", [p[1]])



def p_MarkIfEnd(p):
  '''MarkIfEnd : empty'''
  # global SCOPE
  SCOPE.code.append([None,None,None,SCOPE.endChildBlock+":",None])
  SCOPE.endChildBlock=None
  p[0] = Node("MarkIfEnd", [p[1]])


def p_if_else_block(p):
      '''if_else_block : start_scope_if block_statements_opt end_scope_if'''
      p[0] = Node("block", [p[1], p[2], p[3]])

def p_if_else_statement(p):
        '''if_else_statement : MarkIfStart if_else_begin if_else_intermediate MarkIfEnd'''
        p[0] = Node("if_else_statement", [p[1],p[2]])        

def p_if_else_begin(p):
  '''if_else_begin : if_else_starting if_else_ending'''
  p[0]=Node("if_else_begin",[p[1],p[2]])

  
def p_if_else_starting(p):
  '''if_else_starting : KWRD_IF LPAREN expression RPAREN'''
  child1 = create_leaf("IF", p[1])
  child2 = create_leaf("LPAREN", p[2])
  child3 = create_leaf("RPAREN", p[4])
  if (p[3].dataType!="Boolean"):
    print "Conditional If only accepts boolean expression at line",p.lexer.lineno
    raise Exception("Correct the above Semantics! :P")
  p[0]=Node("if_else_begin",[child1,child2,p[3],child3])

  startLabelChild=returnLabel()
  SCOPE.code.append(["if",p[3].holdingVariable,"== 1","goto",startLabelChild])
  SCOPE.startChildBlock=startLabelChild
  freeVar(p[3].holdingVariable)


  # // BNEQZ 
  # // set label for child block

def p_if_else_ending(p):
  '''if_else_ending : if_else_block'''
  p[0]=Node("if_else_ending",[p[1]])


def p_if_else_intermediate(p):
  '''if_else_intermediate : KWRD_ELSE if_else_end
                          | empty'''
  if (len(p)==2):
    p[0]=Node("if_else_intermediate",[p[1]])
  else:
    child1= create_leaf("ELSE", p[1])
    p[0]=Node("if_else_intermediate",[child1, p[2]])

def p_MarkBeforeElse(p):
  '''MarkBeforeElse : empty'''
  p[0]=Node("MarkBeforeElse",[p[1]])
  startLabelChild=returnLabel()
  SCOPE.code.append([None,None,None,"goto",startLabelChild])
  SCOPE.startChildBlock=startLabelChild


def p_if_else_end(p):
  ''' if_else_end : MarkBeforeElse if_else_block
                  | if_else_begin if_else_intermediate'''
  
  p[0]=Node("if_else_end",[p[1],p[2]])
    
def p_while_statement(p):
  '''while_statement : while_header while_body'''
  p[0] = Node("while_statement", [p[1],p[2]])

def p_while_header(p):
        '''while_header : while_begin LPAREN expression RPAREN'''
        newLabel=returnLabel()
        
        SCOPE.code.append(["if",p[3].holdingVariable,"== 1","goto",newLabel])
        freeVar(p[3].holdingVariable)
        SCOPE.startChildBlock=newLabel

        child2 = create_leaf("LPAREN", p[2])
        child3 = create_leaf("RPAREN", p[4])
        if (p[3].dataType!="Boolean"):
          print "Loop While only accepts boolean expression at line",p.lexer.lineno
          raise Exception("Correct the above Semantics! :P")
        p[0] = Node("while_header", [p[1], child2, p[3], child3])

def p_while_body(p):
    '''while_body : block'''
    p[0] = Node("while_statement_body", [p[1]])


def p_while_begin(p):
  '''while_begin : KWRD_WHILE'''
  child1 = create_leaf("WHILE", p[1])
  label=returnLabel()
  SCOPE.code.append([None,None,label+":",None,None])
  SCOPE.endChildBlock=label
  p[0] = Node("while_begin", [child1])

        

def p_do_while_statement(p):
        '''do_while_statement : do_while_statement_begin block KWRD_WHILE LPAREN expression RPAREN STATE_END '''
        child2 = create_leaf("WHILE", p[3])
        child3 = create_leaf("LPAREN", p[4])
        child4 = create_leaf("RPAREN", p[6])
        child5 = create_leaf("STATE_END", p[7])
        if (p[5].dataType!="Boolean"):
          print "Conditional Do While only accepts boolean expression at line",p.lexer.lineno
          raise Exception("Correct the above Semantics! :P")

        SCOPE.code.append(["if",p[5].holdingVariable,"== 1","goto",p[1].value])
        freeVar(p[5].holdingVariable)

        p[0] = Node("do_while_statement", [p[1], p[2], child2, child3, p[5], child4, child5])
       
def p_do_while_statement_begin(p):
  ''' do_while_statement_begin : KWRD_DO '''
  child1 = create_leaf("DO", p[1])
  label1=returnLabel()
  label2=returnLabel()
  SCOPE.startChildBlock=label1
  SCOPE.endChildBlock=label2
  SCOPE.code.append([None,None,None,"goto",label1])
  SCOPE.code.append([None,None,label2+":",None,None])
 
  p[0]=Node("do_while_statement_begin",[child1],"Unit",label1)


def p_for_statement(p):
  '''for_statement : KWRD_FOR LPAREN for_loop RPAREN block'''
  child1 = create_leaf ("FOR",p[1])
  child2 = create_leaf ("LPAREN",p[2])
  child3 = create_leaf ("RPAREN",p[4])
  p[0] = Node("for_statement",[child1,child2,p[3],child3,p[5]])
  for i in p[3].holdingVariable:
    freeVar(i)


# def p_for_logic(p):
#     ''' for_logic : for_update '''
#     if len(p)==2:
#       p[0]=Node("for_logic",[p[1]])
#     # else:
#     #   child1 = create_leaf("STATE_END",p[2])
#     #   p[0] = Node("for_logic",[p[1],child1,p[3]])

# def p_for_update(p):
#   ''' for_update : for_loop'''
#   p[0]=Node("for_update",[p[1]])

def p_for_loop(p):
  ''' for_loop : IDENTIFIER CHOOSE expression KWRD_UNTIL  expression for_step_opts'''
  
  if SCOPE.is_present(p[1],updateField="symbol"):
    pass
  else:
    print "Undeclared Variable at line",p.lexer.lineno
    raise Exception("Correct the above Semantics! :P")

  if (p[3].dataType==p[5].dataType and p[3].dataType=="Int" and SCOPE.get_attribute_value(p[1],"Type","symbol")=="Int"):
    pass
  else:
    print "Only Integer expressions allowed in For statement at line",p.lexer.lineno
    raise Exception("Correct the above Semantics! :P")

  child1 = create_leaf("IDENTIFIER",p[1])
  child2 = create_leaf("CHOOSE",p[2])
  child3 = create_leaf("UNTIL_TO",p[4])
  p[0] = Node("for_loop_st",[child1,child2,p[3],child3,p[5],p[6]])
  if (p[6].holdingVariable!=None):
    if p[6].dataType=="Int":
      pass 
    else:
      print "Only Integer step allowed at line",p.lexer.lineno
      raise Exception("Correct the above Semantics! :P")

    SCOPE.code.append([SCOPE.get_attribute_append_name(p[1]).name+"__"+p[1],"=",p[3].holdingVariable,None,None])
    freeVar(p[3].holdingVariable)
    for_start_label=returnLabel()
    for_end_label=returnLabel()
    block_start_label=returnLabel()
    block_end_label=returnLabel()
    SCOPE.code.append([None,None,None,for_start_label+":",None])
    SCOPE.code.append(["if",SCOPE.get_attribute_append_name(p[1]).name+"__"+p[1],"<",p[5].holdingVariable+" goto",block_start_label])
    SCOPE.code.append([None,None,None,"goto",for_end_label])
    SCOPE.code.append([None,None,None,block_end_label+":",None])
    SCOPE.code.append([SCOPE.get_attribute_append_name(p[1]).name+"__"+p[1],"=",SCOPE.get_attribute_append_name(p[1]).name+"__"+p[1],"+",p[6].holdingVariable])
    SCOPE.code.append([None,None,None,"goto",for_start_label])
    SCOPE.code.append([None,None,None,for_end_label+":",None])
    SCOPE.startChildBlock=block_start_label
    SCOPE.endChildBlock=block_end_label
    p[0].holdingVariable=[p[5].holdingVariable,p[6].holdingVariable]
  else:
    SCOPE.code.append([SCOPE.get_attribute_append_name(p[1]).name+"__"+p[1],"=",p[3].holdingVariable,None,None])
    freeVar(p[3].holdingVariable)
    for_start_label=returnLabel()
    for_end_label=returnLabel()
    block_start_label=returnLabel()
    block_end_label=returnLabel()
    SCOPE.code.append([None,None,None,for_start_label+":",None])
    SCOPE.code.append(["if",SCOPE.get_attribute_append_name(p[1]).name+"__"+p[1],"< ",p[5].holdingVariable+" goto",block_start_label])
    SCOPE.code.append([None,None,None,"goto",for_end_label])
    SCOPE.code.append([None,None,None,block_end_label+":",None])
    temp=returnTemp()
    SCOPE.code.append([temp,"=","1",None,None])
    SCOPE.code.append([SCOPE.get_attribute_append_name(p[1]).name+"__"+p[1],"=",SCOPE.get_attribute_append_name(p[1]).name+"__"+p[1],"+",temp])
    freeVar(temp)
    SCOPE.code.append([None,None,None,"goto",for_start_label])
    SCOPE.code.append([None,None,None,for_end_label+":",None])
    SCOPE.startChildBlock=block_start_label
    SCOPE.endChildBlock=block_end_label
    p[0].holdingVariable=[p[5].holdingVariable]




# def p_for_untilTo(p):
#   '''for_untilTo : KWRD_UNTIL 
#                   | KWRD_TO'''

#   child1 = create_leaf("UNTIL_TO",p[1])
#   p[0]=Node("for_untilTo",[child1])


def p_for_step_opts(p):
  ''' for_step_opts : KWRD_BY expression
                    | empty'''
  if len(p)==2:
    p[0]=Node("for_step_opts",[p[1]])
  else :
    if (p[2].dataType=="Int"):
      pass
    else:
      print "Only Integer step allowed in For statement at line",p.lexer.lineno
      raise Exception("Correct the above Semantics! :P")
    child1 = create_leaf("BY",p[1])
    p[0]=Node("for_step_opts",[child1,p[2]])
    p[0].holdingVariable=p[2].holdingVariable
    p[0].dataType=p[2].dataType

               
def p_switch_statement(p):
        '''switch_statement : expression KWRD_MATCH switch_block '''
        child1 = create_leaf("MATCH", p[2])
        p[0] = Node("switch_statement", [p[1], child1, p[3]])
        

def p_switch_block(p):
        '''switch_block : BLOCK_BEGIN BLOCK_END '''
        child1 = create_leaf("BLOCK_BEGIN", p[1])
        child2 = create_leaf("BLOCK_END", p[2])
        p[0] = Node("switch_block", [child1, child2])
       

def p_switch_block2(p):
        '''switch_block : BLOCK_BEGIN switch_block_statements BLOCK_END '''
        child1 = create_leaf("BLOCK_BEGIN", p[1])
        child2 = create_leaf("BLOCK_END", p[3])
        p[0] = Node("switch_block", [child1, p[2], child2])
       

def p_switch_block3(p):
        '''switch_block : BLOCK_BEGIN switch_labels BLOCK_END '''
        child1 = create_leaf("BLOCK_BEGIN", p[1])
        child2 = create_leaf("BLOCK_END", p[3])
        p[0] = Node("switch_block", [child1, p[2], child2])
      

def p_switch_block4(p):
        '''switch_block : BLOCK_BEGIN switch_block_statements switch_labels BLOCK_END '''
        child1 = create_leaf("BLOCK_BEGIN", p[1])
        child2 = create_leaf("BLOCK_END", p[4])
        p[0] = Node("switch_block", [child1, p[2], p[3], child2])
       

def p_switch_block_statements(p):
        '''switch_block_statements : switch_block_statement
                                   | switch_block_statements switch_block_statement'''
        if len(p) == 2:
          p[0] = Node("switch_block_statements", [p[1]])
        else:
          p[0] = Node("switch_block_statements", [p[1], p[2]])
    

def p_switch_block_statement(p):
        '''switch_block_statement : switch_labels block_statements'''
        p[0] = Node("switch_block_statement", [p[1], p[2]])
       

def p_switch_labels(p):
        '''switch_labels : switch_label
                         | switch_labels switch_label'''
        if len(p) == 2:
          p[0] = Node("switch_labels", [p[1]])
        else:
          p[0] = Node("switch_labels", [p[1], p[2]])
       

def p_switch_label(p):
        '''switch_label : KWRD_CASE expression FUNTYPE '''
        child1 = create_leaf("CASE", p[1])
        child2 = create_leaf("FUNTYPE", p[3])
        p[0] = Node("switch_label", [child1, p[2], child2])
      


def p_empty_statement(p):
        '''empty_statement : STATE_END '''
        child1 = create_leaf("STATE_END", p[1])
        p[0] = Node("empty_statement", [child1])
    
def p_return_statement(p):
        '''return_statement : KWRD_RETURN expression_optional STATE_END '''
        child1 = create_leaf("RETURN", p[1])
        child2 = create_leaf("STATE_END", p[3])
        p[0] = Node("return_statement", [child1, p[2], child2])
        if (p[2].dataType==SCOPE.funcType):
          pass
        else:
          print ("Return Types not consistent at line",p.lexer.lineno)
          raise Exception("Check the semantics! :P")

        SCOPE.code.append([None,None,None,"Return",p[2].holdingVariable])
      


def p_constructor_arguement_list_opt(p):
  '''constructor_arguement_list_opt : constructor_arguement_list
                            | empty '''
  p[0] = Node("constructor_arguement_list_opt", [p[1]],p[1].dataType)
        

def p_constructor_arguement_list(p):
  '''constructor_arguement_list : constructor_arguement_list_declarator
                         | constructor_arguement_list COMMA constructor_arguement_list_declarator'''
  if len(p) == 2:
    newConst_2=list()
    newConst_2.append(p[1].dataType)
    p[0] = Node("constructor_arguement_list", [p[1]],newConst_2)
  else:
    child1 = create_leaf("COMMA", p[2])

    newConst_1=list(p[1].dataType)
    newConst_2=list()
    newConst_2.append(p[3].dataType)
    # print newConst_1
    # print newConst_2

    p[0] = Node("constructor_arguement_list", [p[1], child1, p[3]],newConst_1+newConst_2)


def p_constructor_arguement_list_declarator(p):
    '''constructor_arguement_list_declarator : declaration_keyword IDENTIFIER COLON type'''
    child1 = create_leaf("IDENTIFIER", p[2])
    child2 = create_leaf("COLON", p[3])
    attribute=dict()
    attribute['Type']=p[4].value
    SCOPE.offset+=4
    attribute['Offset']=SCOPE.offset
    SCOPE.add_entry(p[2],attribute,"symbol")

    
    p[0] = Node("constructor_arguement_list_declarator", [p[1], child1, child2, p[4]],p[4].value) 


def p_func_arguement_list_opt(p):
  '''func_arguement_list_opt : variable_declarators
                            | empty '''
  p[0] = Node("func_arguement_list_opt", [p[1]],p[1].dataType)                       

def p_class_declaration(p):
        '''class_declaration : class_header class_body'''
        p[0] = Node("class_declaration", [p[1], p[2]])
       


def p_class_header(p):
        '''class_header : class_header_name class_header_extends_opt'''
        p[0] = Node("class_header", [p[1], p[2]])
       

def p_class_header_name(p):
        '''class_header_name : class_header_name1 func_args_start constructor_arguement_list_opt RPAREN''' # class_header_name1 type_parameters
                             # | class_header_name1
        # child1 = create_leaf("LPAREN", p[2])
        child2 = create_leaf("RPAREN", p[4])
        #Arguement List : p[3].dataType
        #Name : p[1].value
        attribute=dict()
        attribute['ConstructorList']=p[3].dataType
        SCOPE.prev_env.add_entry(p[1].value,attribute,"object")
        # print p[1].value
        # print
        # SCOPE.print_table()
        p[0] = Node("class_header_name", [p[1], p[2], p[3], child2])
        SCOPE.objName=p[1].value
       

def p_class_header_name1(p):
        '''class_header_name1 : modifier_opts KWRD_CLASS name'''
        child1 = create_leaf("CLASS", p[2])
        p[0] = Node("class_header_name1", [p[1], child1, p[3]],"Unit",p[3].value)

       

def p_class_header_extends_opt(p):
        '''class_header_extends_opt : class_header_extends
                                    | empty'''
        p[0] = Node("class_header_extends_opt", [p[1]])


def p_class_header_extends(p):
        '''class_header_extends : KWRD_EXTNDS name LPAREN func_arguement_list_opt RPAREN'''
        child1 = create_leaf("EXTENDS", p[1])
        child2 = create_leaf("LPAREN", p[3])
        child3 = create_leaf("RPAREN", p[5])
        p[0] = Node("class_header_extends", [child1, p[2], child2, p[4], child3])


def p_class_body(p):
        '''class_body : class_body_start block_statements_opt end_scope ''' 
        
        p[0] = Node("class_body", [p[1], p[2], p[3]])
        # p[0] = Node("class_body", [p[1]])

def p_class_body_start(p):
  '''class_body_start : BLOCK_BEGIN'''
  child1 = create_leaf("BLOCK_BEGIN", p[1])
  p[0] = Node("class_body_start", [child1])





def p_method_declaration(p):
        '''method_declaration : method_header method_body'''
        p[0] = Node("method_declaration", [p[1], p[2]])


def p_method_header(p):
        '''method_header : method_header_name func_args_start func_arguement_list_opt RPAREN COLON method_return_type ASSIGN'''
        # child1 = create_leaf("LPAREN", p[2])
        child2 = create_leaf("RPAREN", p[4])
        child3 = create_leaf("COLON", p[5])
        child4 = create_leaf("ASSIGN", p[7])
        attribute=dict()
        attribute['Type']=p[3].dataType
        attribute['returnType']=p[6].dataType
        SCOPE.prev_env.add_entry(p[1].value,attribute,"function")
        SCOPE.funcName=p[1].value
        SCOPE.funcType=p[6].dataType
        p[0] = Node("method_header", [p[1], p[2], p[3], child2, child3, p[6], child4])

def p_func_args_start(p):
        '''func_args_start : LPAREN'''
        global SCOPE
        NEW_SCOPE = Env(SCOPE) 
        SCOPE=NEW_SCOPE

        child1 = create_leaf("LPAREN", p[1])
        p[0] = Node("func_args_start", [child1])

  
def p_method_return_type(p):
        '''method_return_type : type''' 
        p[0] = Node("method_return_type", [p[1]],p[1].value)

def p_method_return_type1(p):
        '''method_return_type : TYPE_VOID'''
        child1 = create_leaf("VOID", p[1])
        p[0] = Node("method_return_type", [child1],"Unit")

def p_method_header_name(p):
        '''method_header_name : modifier_opts KWRD_DEF IDENTIFIER''' # class_header_name1 type_parameters
                             # | class_header_name1
        child1 = create_leaf("DEF", p[2])
        child2 = create_leaf("IDENTIFIER", p[3])
        p[0] = Node("method_header_name", [p[1], child1, child2],"Unit",p[3])


def p_method_body(p):
        '''method_body : method_start_scope block_statements_opt method_end_scope '''
        
        p[0] = Node("method_body", [p[1], p[2], p[3]])


def p_method_start_scope(p):
  '''method_start_scope : BLOCK_BEGIN'''
  child1 = create_leaf("BLOCK_BEGIN", p[1])
  p[0] = Node("end_scope", [child1])
  SCOPE.code.append([None,None,None,SCOPE.prev_env.name+"__"+SCOPE.funcName+":",None])
  SCOPE.code.append([None,None,None,"BeginFunc",None])

def p_method_end_scope(p):
  '''method_end_scope : BLOCK_END'''
  global SCOPE
  SCOPE.code.append([None,None,None,"EndFunc",None])
  SCOPE.code[1][4]=str(len(SCOPE.tempvar)*4)
  PREV_SCOPE=SCOPE.prev_env
  SCOPE=PREV_SCOPE
  child1 = create_leaf("BLOCK_END", p[1]) 
  p[0] = Node("end_scope", [child1])



def p_modifier(p):
      '''modifier : KWRD_PROTECTED
                  | KWRD_PRIVATE'''
      child1 = create_leaf("ModifierKeyword", p[1])
      p[0] = Node("modifier", [child1])


def p_type(p):
        '''type : primitive_type 
                | reference_type '''
        p[0] = Node("type", [p[1]],p[1].dataType,p[1].value)
        # p[0] = p[1]

def p_primitive_type(p):
    '''primitive_type : TYPE_INT
                      | TYPE_FLOAT
                      | TYPE_CHAR
                      | TYPE_STRING
                      | TYPE_BOOLEAN'''
    child1 = create_leaf("TYPE", p[1])
    p[0] = Node("primitive_type", [child1],"Unit",p[1]) 


def p_reference_type(p):
      '''reference_type : class_data_type
                        | array_data_type'''
      p[0] = Node("reference_type", [p[1]],p[1].dataType,p[1].value)

def p_class_data_type(p):
      '''class_data_type : name'''
      p[0] = Node("class_data_type", [p[1]],"Unit","Object@"+p[1].value)

def p_array_data_type(p):
      '''array_data_type : KWRD_ARRAY LBPAREN type RBPAREN'''
      child1 = create_leaf("ARRAY", p[1])
      child2 = create_leaf("LBPAREN", p[2])
      child3 = create_leaf("RBPAREN", p[4])
      p[0] = Node("array_data_type", [child1, child2, p[3], child3],"Unit","Array,"+p[3].value)

def p_array_initializer(p):
  ''' array_initializer : KWRD_NEW KWRD_ARRAY LBPAREN type RBPAREN LPAREN INT_CONST RPAREN
                        | KWRD_ARRAY LPAREN argument_list_opt RPAREN '''
  if len(p) == 9:
    child1 = create_leaf("NEW", p[1])
    child2 = create_leaf("ARRAY", p[2])
    child3 = create_leaf("LBPAREN", p[3])
    child4 = create_leaf("RBPAREN", p[5])
    child5 = create_leaf("LPAREN", p[6])
    child6 = create_leaf("INT_CONST", p[7])
    child7 = create_leaf("RPAREN", p[8])

    p[0] = Node("array_initializer", [child1, child2, child3, p[4], child4, child5, child6, child7],"Array,"+p[4].value,None,str(int(p[7])))
  else:
    child1 = create_leaf("ARRAY", p[1])
    child2 = create_leaf("LPAREN", p[2])
    child3 = create_leaf("RPAREN", p[4]) 
    currType=p[3].dataType[0]
    # print p[3].dataType
    for i in range(1,len(p[3].dataType)):
      if p[3].dataType[i] != currType:
        print ("Type error: array can only be of same type at line ",p.lexer.lineno)
        raise Exception("Correct the above Semantics! :P")
    p[0] = Node("array_initializer", [child1, child2, p[3], child3],"Array,"+currType,None,str(int(len(p[3].dataType))))
    p[0].holdingVariable=p[3].holdingVariable   

def p_class_initializer(p):
  ''' class_initializer : KWRD_NEW name LPAREN argument_list_opt RPAREN ''' 
  child1 = create_leaf("NEW", p[1])
  child2 = create_leaf("LPAREN", p[3])
  child3 = create_leaf("RPAREN", p[5])
  if SCOPE.is_present(p[2].value,updateField="object"):
    val=SCOPE.get_attribute_value(p[2].value,'ConstructorList',"object")
    if val==p[4].dataType:
      pass
    else:
      print ("Check Constructor Definition , line ",p.lexer.lineno)
      raise Exception("Correct the above Semantics! :P")
  else:
    print ("Undefined Class Definition , line ",p.lexer.lineno)
    raise Exception("Correct the above Semantics! :P")

  p[0] = Node("class_initializer", [child1, p[2], child2, p[4], child3],"Object@"+p[2].value,None,None,p[4].dataType)

def p_empty(p):
    'empty :'
    child1 = create_leaf("Empty", "NOP")
    p[0] = Node("empty", [child1])
    pass

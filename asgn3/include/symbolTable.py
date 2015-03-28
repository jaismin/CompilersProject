#Hashtable Class: it contains the table
#self.table is dictionary with key=name_of_entry & value=list_of_attributes  eg: a=5.. then name='a'(i.e. lexeme) attribute={'value':5} .. note ada is case-insensitive
#list_of_attributes is a dictionary (list is implemented as dictionary) with many entries with key(attribute_name):value(attribute_value) pairs like - {'type': 'Integer', 'value':'Integer', 'isdatatype':True}

#Hash table is a dictionary of dictionary based on the name then based on the attributes value 
#Accessed using .table  and value is table[name][attribute value]
class HashTable:
    def __init__(self):
        self.table={}   # a dictionary

    def add_entry (self, name, list_attributes):
        if name in self.table:
            print 'Error: Entry already present - [' + name + ']'
	    assert(False)
        else:
            #print "Deepak4iii - ",name," - ",list_attributes
            self.table[name]= {}    # a dictionary
            for i_key in list_attributes:   
                self.table[name][i_key]=list_attributes[i_key]
        
    #update if already present else add it.
    def update_entry(self, name, attribute_name, attribute_value):
        try:                        #try catch exception
            self.table[name][attribute_name] = attribute_value
            return True
        except: 
            return False
        
    def get_attribute_value (self, name, attribute_name):
        try:
            return self.table[name][attribute_name]
        except:
            return None         
    
    def is_present(self, name):
        if name in self.table:
            return True
        else: 
            return False
    
    def get_table(self):
        return self.table               
    
    def print_table(self):
        print "Table is : Entry name ==> Attribute_list"
        for name in self.table:
            print name,' ==> ', self.table[name]



class arrayObject:
    def __init__(self,dataType,size):
        self.dataType=dataType   # a dictionary
        self.size=size


# class classObject:
#     def __init__(self):
#         self.table={}   # a dictionary    



#Environment Class: Contains current symbolTable and pointer to parent Environment
class Env:
    static_var = 1   
    def __init__(self, prev=None):
        self.symbolTable = HashTable()  #Creates a new symbol table for a new scope
        self.functionTable = HashTable()  #Creates a new hash table for a new scope
        self.objectTable = HashTable()  #Creates a new hash table for a new scope
        self.name = "node" + str(Env.static_var) 
        self.childs=[]
        self.width = 0                      # overall offset/width of this env
        self.paramwidth = 0
        self.prev_env=prev
        self.code=list()
        if prev==None:
           self.level=0 
           self.parentName=""
        else:
            self.level=prev.level+1
            self.parentName=prev.name
        Env.static_var+=1                 # pointer to the previous hash table     
        if (prev != None):
            prev.childs.append(self)

    def gprev(self):
        return self.prev

    def goto(self,data):
        for child in range(0,len(self.childs)):
            # print self.node[child].name
            if(self.childs[child].name==data):
                return self.node[child]
    
    def subtree(self):
        "Gets the node by name"

        print self.name,":::",self.level,':::',self.parentName
        self.symbolTable.print_table()
        for child in range(0,len(self.childs)):
            # print self.node[child].name

            self.childs[child].subtree()
            # if(self.node[child].name==data):
            #     return self.node[child]

    
    #adds entry in current hashtable
    def add_entry(self,name, list_attributes,updateField="symbol"):
        if updateField=="symbol":
            self.symbolTable.add_entry(name, list_attributes)
        elif updateField=="function":
            self.functionTable.add_entry(name, list_attributes)
        elif updateField == "object":
            self.objectTable.add_entry(name, list_attributes)
        else:
            print "Attribute Missing"


    # update entry in the most recent hash table in case not found in the most recent goes to the parent and then to next parent and 
    # successive goes up till the time entry is found if not found found printf error (Checks if the variable used is previously declared)
    def update_entry(self, name, attribute_name, attribute_value,updateField="symbol"):
        if updateField=="symbol":
            env=self
            while env!=None:
                if env.symbolTable.update_entry(name, attribute_name, attribute_value) == True:
                    return
                env=env.prev_env
            print 'Error: Variable not present for updation - [' + name + ']'
        elif updateField=="function":
            env=self
            while env!=None:
                if env.functionTable.update_entry(name, attribute_name, attribute_value) == True:
                    return
                env=env.prev_env
            print 'Error: Function not present for updation - [' + name + ']'
        elif updateField=="object":
            env=self
            while env!=None:
                if env.objectTable.update_entry(name, attribute_name, attribute_value) == True:
                    return
                env=env.prev_env
            print 'Error: Object not present for updation - [' + name + ']'
        else:
            print "Attribute Missing"




    #Returns list of attributes from most recent hashtable (recent ancestor) corresponding to name. Returns None if entry not found
    def get_attribute_value(self,name, attribute_name,updateField="symbol"):
        if updateField=="symbol":
            env=self
            while env!=None:
                found=env.symbolTable.get_attribute_value(name, attribute_name)
                if found != None:
                    return found
                env=env.prev_env
            return None
        elif updateField=="function":
            env=self
            while env!=None:
                found=env.functionTable.get_attribute_value(name, attribute_name)
                if found != None:
                    return found
                env=env.prev_env
            return None
        elif updateField=="object":
            env=self
            while env!=None:
                found=env.objectTable.get_attribute_value(name, attribute_name)
                if found != None:
                    return found
                env=env.prev_env
            return None
        else:
            print "Attribute not found"

    
    #returns table only in current scope, not ancestral ones
    def getCurrentSymbolTable(self):
        return self.symbolTable.get_table()
    
    #is_present in the current scope only
    # def is_present_current_block(self, name,updateField="sybmol"):
    #     if (updateField=="symbol"):
    #         return self.symbolTable.is_present(name)
    #     elif (updateField=="function"):
    #         return self.functionTable.is_present(name)
    #     elif (updateField=="object"):
    #         return self.objectTable.is_present(name)
        
    def is_present(self,name,updateField="symbol"):
        if updateField=="symbol":
            env=self
            while env!=None:
                if env.symbolTable.is_present(name):
                    return True
                env = env.prev_env
            return False
        elif updateField=="function":
            env=self
            while env!=None:
                if env.functionTable.is_present(name):
                    return True
                env = env.prev_env
            return False

        elif updateField=="object":
            env=self
            while env!=None:
                if env.objectTable.is_present(name):
                    return True
                env = env.prev_env
            return False
        
    def print_table(self):
        env=self
        i=0
        while env!=None:
            print "Ancestor - ",i
            env.objectTable.print_table()
            env = env.prev_env
            i=i+1
    
    # ==========================================Dont know the use of the last four functions 
    def get_width(self):
        return self.width

    def increment_width(self, inc):     #similar to addwidth() in lecture notes
        self.width += inc

    def get_paramwidth(self):
        return self.paramwidth
        
    def increment_paramwidth(self, inc):
        self.paramwidth += inc
        
    # get_entry(self,name)      #return full attribute list.
    # get_entryheight(self,name)        #how many levles abov it was found

if __name__ == '__main__':
    OBJ = Env(None)
    # print Env.static_var
    dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
    OBJ.add_entry('Hello',dict)
    print OBJ.get_attribute_value('Hello','Beth')
    dict = {'Alice': '323', 'Beth': '91223', 'Cecil': '3223'}
    OBJ.add_entry('Hel',dict)
    print OBJ.is_present('Hel')

    OBJ1 = Env(OBJ)
    dict = {'Alice': '22', 'Beth': '91', 'Cecil': '32'}
    OBJ1.add_entry('Hello1',dict)
    print OBJ.get_attribute_value('Hello','Beth')
    print OBJ.get_attribute_value('Hello1','Beth')
    dict = {'Alice': '32', 'Beth': '923', 'Cecil': '23'}
    OBJ1.add_entry('Hel',dict)
    print OBJ1.is_present('Hel')
    print OBJ1.get_attribute_value('Hel','Beth')

    OBJ2 = Env(OBJ1)
    dict = {'Alice': '2', 'Beth': '1', 'Cecil': '2'}
    OBJ2.add_entry('Hell1',dict)
    print OBJ2.get_attribute_value('Hell1','Beth')


    OBJ3 = Env(OBJ)
    dict = {'Alice': '2', 'Beth': '1', 'Cecil': '2'}
    OBJ3.add_entry('Hell1',dict)
    # print OBJ3.get_attribute_value('Hell1','Beth')

    OBJ.subtree()
    #SymbolTable Class: Just abstraction layer over the Environment Class





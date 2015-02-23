def printLexer(lexer,code_full):
	# track the line numbers of the code and the parsed output
	newlineno=lexer.lineno
	parsed_output=[]
	temp_code=code_full
	temp_code=temp_code.split("\n")

	# loop over the output obtained from lexer
	for tok in lexer:
	        if (tok.lineno!=newlineno) :
	            print temp_code[newlineno-1],"\t","//",
	            for item in parsed_output:
	                print item,
	            parsed_output=[]
	            print '\n',
	            for i in xrange(newlineno,tok.lineno-1):
	                print temp_code[i]
	            parsed_output.append(tok.type)
	            newlineno=tok.lineno
	        else :
	            parsed_output.append(tok.type)
	print temp_code[newlineno-1],"\t","//",
	for item in parsed_output:
	    print item,
	parsed_output=[]

    
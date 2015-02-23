from tokensDefination import *
# regular expression for simple tokens
t_PLUS = r'\+'
t_PLUSEQ = r'\+='
t_MINUS = r'-'
t_MINUSEQ = r'\-='
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BLOCK_BEGIN = r'{'
t_BLOCK_END = r'}'
t_STATE_END = r';'
t_COLON = r':'
t_ASSIGN = r'='
t_EQUAL = r'=='
t_NEQUAL = r'!='
t_GREATER = r'>'
t_GEQ = r'>='
t_LESS = r'<'
t_LEQ = r'<='
t_DOT = r'\.'
t_LBPAREN = r'\['
t_RBPAREN = r'\]'
t_CHOOSE = r'<-'
t_EXACTEQ = r'=:='
t_SUBTYPE = r'<:<'
t_VIEWABLE = r'<%<'
t_STRING_CONST = r'"(?:\\.|[^"\\])*"'
t_CHARACTER = r'\'([^\\\'\r\n]|\\[^\r\n]|\\u[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f])(\'|\\)'
t_TILDA = r'\~'
t_NOT = r'!'
t_COMMA = r','
t_UNDER = r'_'
t_AND = r'&&'
t_OR = r'\|\|'
t_AND_BITWISE = r'&'
t_OR_BITWISE = r'\|'
t_FUNTYPE = r'=>'
t_LOWER_BOUND = r'>:'
t_UPPER_BOUND = r'<:'
t_VIEW = r'<%'
t_INNER_CLASS = r'\#'
t_AT = r'@'
t_QUESTION = r'\?'
t_COMM = r'::'

# Floating literal
def t_FLOAT_CONST(t):
    r'((\d+)(\.)(\d+)([Ee][+-]?(\d+))?([FfDd])?)|((\.)(\d+)([Ee][+-]?(\d+))?([FfDd])?)|((\d+)([Ee][+-]?(\d+))([FfDd])?)|((\d+)([Ee][+-]?(\d+))?([FfDd]))'    #r'((\d+)(\.\d+)(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))([lL]|[fF])?'
    # print 
    if (t.value[-1]=='F' or t.value[-1]=='f' or t.value[-1]=='D' or t.value[-1]=='d'):
        t.value=t.value[:-1]
    # print t.value
    t.value = float(t.value)
    return t

# Integer literal
def t_INT_CONST(t):
    r'(((((0x)|(0X))[0-9a-fA-F]+)|(\d+))([uU]|[lL]|[uU][lL]|[lL][uU])?)'
    t.value = int(t.value)
    return t
    
# Identifier will match itself as well as the other keywords
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')    # check for reserved values
    return t

# track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # return t
    pass

# a string for ignored characters
t_ignore = ' \t'

# error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)
    pass
def t_MULTIPLE_COMMENT(t):
    r'(/\*(.|\n)*?\*/)'
    t.lexer.lineno += t.value.count('\n')

def t_SINGLE_COMMENT(t):
    r'(//.*?\n)'
    t.lexer.lineno += t.value.count('\n')
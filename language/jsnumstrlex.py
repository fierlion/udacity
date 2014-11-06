# JavaScript: Numbers & Strings
# 
# In this exercise you will finish out the token definitions for JavaScript 
# by handling Numbers, Identifiers and Strings. 
#
# For this assignment, a JavaScript IDENTIFIER must start with an upper- or
# lower-case character. It can then contain any number of upper- or
# lower-case characters or underscores. Its token.value is the textual
# string of the identifier. 
#       Yes:    my_age
#       Yes:    cRaZy
#       No:     _starts_with_underscore
#
# For this assignment, a JavaScript NUMBER is one or more digits. A NUMBER
# can start with an optional negative sign. A NUMBER can contain a decimal
# point, which can then be followed by zero or more additional digits. Do
# not worry about hexadecimal (only base 10 is allowed in this problem).
# The token.value of a NUMBER is its floating point value (NOT a string).
#       Yes:    123
#       Yes:    -456
#       Yes:    78.9
#       Yes:    10.
#       No:     +5
#       No:     1.2.3
#
# For this assignment, a JavaScript STRING is zero or more characters
# contained in double quotes. A STRING may contain escaped characters.
# Notably, \" does not end a string. The token.value of a STRING is
# its contents (not including the outer double quotes). 
#       Yes:    "hello world"
#       Yes:    "this has \"escaped quotes\""
#       No:     "no"t one string" 
#
# Hint: float("2.3") = 2.3

import ply.lex as lex

tokens = (
    'IDENTIFIER',   
    'NUMBER',       
    'STRING',       
)

def t_NUMBER(token):
    r'-?[0-9]+\.?[0-9]+'
    token.value = float(token.value)
    token.type = 'NUMBER'
    return token

def t_STRING(token):
    r'([\w ]*\\"*[A-Za-z ]*)+'
    token.value = token.value
    token.type = 'STRING'
    return token

def t_IDENTIFIER(token):
    r'[A_Za-z][A-Za-z_]*'
    token.value = str(token.value)
    token.type = 'IDENTIFIER'
    return token


t_ignore = ' \t\v\r' # whitespace 

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex() 

def test_lexer(input_string):
    lexer.input(input_string)
    result = [ ] 
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [tok.type,tok.value]
    return result

#test cases
input1 = 'some_identifier -12.34 "a \\"escape\\" b"'
output1 = ['IDENTIFIER', 'some_identifier', 'NUMBER', -12.34, 'STRING', 
'a \\"escape\\" b']
print test_lexer(input1) == output1
print test_lexer(input1)

input2 = '-12x34' 
output2 = ['NUMBER', -12.0, 'IDENTIFIER', 'x', 'NUMBER', 34.0]
print test_lexer(input2) == output2
print test_lexer(input2)

#why does this return IDENTIFIER 'ello' as the value??
input3 = "Hello"
print test_lexer(input3)
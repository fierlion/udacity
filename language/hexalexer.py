#requires python-ply (Python Lex-Yac)
#from http://www.dabeaz.com/ply/

import ply.lex as lex
import string
import math

tokens = ('NUM', 'HEX', 'ID', 'STR')

def t_NUM_hex(token):
    r'0x[A-Fa-f0-9]+'    
    token.value = hexToDec(str(token.value))
    token.type = 'NUM'
    return token

def t_ID(token):
    r'[A-Za-z]+'
    token.value = str(token.value)
    token.type = 'ID'
    return token
    
def t_NUM_decimal(token):
    r'[0-9]+'
    token.value = int(token.value)
    token.type = 'NUM'
    return token

t_ignore = ' \t\v\r'

def t_error(t):
    print "Lexer: unexpected character " + t.value[0]
    t.lexer.skip(1) 

lexer = lex.lex() 

#function to manually change string formatted hex ('0x###') to decimal 
def hexToDec(input_string):
    #input '0x19' = 25 decimal
    decimal = 0
    hexChars = list('abcdef')
    hexStr = string.lower(input_string[2:])
    for i in range(len(hexStr)):
        if hexStr[i] in hexChars:
            #there's got to be a better way!
            #int(math.pow(16, (len(hexStr)-1)-i)) gives us
            #16 ^ (left to right numeric index)
            decimal += (hexChars.index(hexStr[i]) + 10) * int(math.pow(16, (len(hexStr)-1)-i))
        else:
            decimal += int(hexStr[i]) * int(math.pow(16, (len(hexStr)-1)-i))
    return decimal
    

def test_lexer(input_string):
    lexer.input(input_string)
    result = [ ] 
    while True:
      tok = lexer.token()
      if not tok: break
      result = result + [(tok.type, tok.value)]
    return result

question1 = "0x19 equals 25" # 0x19 = (1*16) + 9
answer1 = [('NUM', 25), ('ID', 'equals'), ('NUM', 25) ]

question2 = "0xfeed MY 0xface" 
answer2 = [('NUM', 65261), ('ID', 'MY'), ('NUM', 64206) ]

print test_lexer(question2)
print test_lexer(question2) == answer2

question3 = "tricky 0x0x0x" 
answer3 = [('ID', 'tricky'), ('NUM', 0), ('ID', 'x'), ('NUM', 0), ('ID', 'x')]

print test_lexer(question3) == answer3

question4 = "in 0xdeed"

print test_lexer(question4)

question5 = "where is the 0xbeef"

print test_lexer(question5)

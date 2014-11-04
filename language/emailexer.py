

import ply.lex as lex
import re 

tokens = ('EMAIL',)

def t_EMAIL(token):
    r'\w+@(\w+\.)+\w+'
    token.value = str(token.value)
    token.type = 'EMAIL'
    return token

t_ignore = ' \t\v\r'

def t_error(t):
    t.lexer.skip(1) 

lexer = lex.lex()

def addresses(haystack): 
    lexer.input(haystack)
    result = [ ] 
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [re.sub(r"NOSPAM", "", str(tok.value))]
    return result

input1 = """louiseNOSPAMaston@germany.de (1814-1871) was an advocate for
democracy. irmgardNOSPAMkeun@NOSPAMweimar.NOSPAMde (1905-1982) wrote about
the early nazi era. rahelNOSPAMvarnhagen@berlin.de was honored with a 1994
deutsche bundespost stamp. seti@home is not actually an email address."""

output1 = ['louiseaston@germany.de', 'irmgardkeun@weimar.de', 'rahelvarnhagen@berlin.de']
print addresses(input1)
print addresses(input1) == output1

#not my code!
#lightly modified from Peter Norvig's 'Design of Computer Programs'
def search(pattern, text):
    "return True if patetrn appears anywhere in text"
    if pattern.startswith('^'):
        return match(pattern[1:], text)
    else:
        return match('.*' + pattern, text)

def match(pattern, text):
    "return True if pattern appears at the start of the text"
    if pattern == '':
        #pattern is blank
        return True
    elif pattern == '$':
        #text should be empty, we have reached the end
        return (text == '')
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, oper, pat = pattern[0], pattern[1], pattern[2:]
        if oper == '*':
            return match_star(p, pat, text)
        elif oper == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and
                match(pattern[1:], text[1:])) 

def match1(p, text):
    "Return True inf first char of text matches pattern char p"
    if not text: return False
    return p == '.' or p == text[0]

def match_star(p, pattern, text):
    "Return True if any number of char p folllowed by pattern matches text"
    return (match(pattern, text) or
    (match1(p, text) and
    #recursive call to match_star()
    match_star(p, pattern, text[1:])))

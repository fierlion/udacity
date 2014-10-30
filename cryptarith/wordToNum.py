# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    splWord = list(word.upper())
    retWord = []
    for i in range(len(splWord)):
        retWord.append(str(10**i) + '*' + splWord[(len(splWord)-1)-i])
    return '('+ ('+'.join(retWord)) + ')'

#test word
print compile_word("trying")
print compile_word("lower")

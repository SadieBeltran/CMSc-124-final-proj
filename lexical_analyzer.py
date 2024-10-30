# this contains the lexical analyzer
import re

def tokenizer(lexeme):
    # receive lexeme
    # run match case
    match lexeme:
        case re.match("$HAI^"):
            return (lexeme, "START")
        case _:
            raise RuntimeError("Lexeme doesn't match!")
            return None

def lexicalAnalysis(line):
    # split the line into lexemes by splitting with space
    lexemes = line.strip() # remove front and trailing whitespace
    # then split by regex?
    lexemes = re.split('(BTW .*$|\"[^\"]*\"|HAI|WAZZUP|I HAS A|[a-zA-Z]\w+|ITZ|BUHBYE|VISIBLE|OBTW|TLDR|KTHXBYE)', lexemes) 
    lexemes = [name for name in lexemes if name.strip()] #this filters out the strings containing only whitespace
    print(lexemes)
    
    # then run it through tokenizer?
    # tokenizer(lexemes)
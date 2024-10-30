# this contains the lexical analyzer
import re


def raiseError(code):
    match code:
        case 1:
            raise RuntimeError("Error in code cleaning, no end found")
        case 2:
            raise RuntimeError("Error in lexical analyzer, string has no match")

#this function removes whitespace and comments
def cleanCode(lines, lineLen):
    cleanedLines = []
    tldrFlag = 0
    for num in range(0, lineLen):
        #the succeeding if statements deal with multiline comments
        lines[num] = lines[num].strip()
        # if line contains comment, remove comment
        if re.search(r'^TLDR', lines[num]):
            print("TLDR found")
            tldrFlag = 0
            lines[num] = re.sub(r'^TLDR', '', lines[num]) #remove TLDR from the line and extract the instruction if there is
            cleanedLines.append(lines[num])
            continue
        
        if num > lineLen: #encountered EOF while looking for TLDR
            raiseError(1)

        if tldrFlag == 1:
            continue
        
        if re.search(r'BTW [^\n]*$', lines[num]):
            lines[num] = re.sub(r'BTW .*$', '', lines[num]) #this removes the trailing BTWs or the whole BTWs
        elif re.search(r'^OBTW', lines[num]):
            tldrFlag = 1
            continue
        cleanedLines.append(lines[num])

    return [name for name in cleanedLines if name.strip()]

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
    # then split by regex?
    lexemes = re.split('(BTW .*$|\"[^\"]*\"|HAI|WAZZUP|I HAS A|[a-zA-Z]\w+|ITZ|BUHBYE|VISIBLE|OBTW|TLDR|KTHXBYE)', lexemes) 
    lexemes = [name for name in lexemes if name.strip()] #this filters out the strings containing only whitespace
    print(lexemes)
    
    # then run it through tokenizer?
    # tokenizer(lexemes)
import lexical_analyzer
import re
# This file reads the sample file per line and feeds it to the interpreter


file = open('sample_lolcodes/01_variables.lol', 'r')
lines = file.read() #splits the file into separate lines
#might want to implement a way to deal with comments (like removing them)\
file.close() #make sure to close the file you open

lines = lines.splitlines()
lineLen = len(lines)
lines = lexical_analyzer.cleanCode(lines, lineLen)
lineLen = len(lines) #update linelenght
# print(lines)

# put the code that's been cleaned of here
# this parses each line and runs it
symbolTable = []
for num in range(0, lineLen):
    # print(lines[num])

    lexical_analyzer.lexicalAnalysis(lines[num])
    # lexical analyzer here
    # syntax analyzer here
    # semantic analyzer here
    # do what the line says
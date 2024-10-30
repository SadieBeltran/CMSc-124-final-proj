import lexical_analyzer
import re
# This file reads the sample file per line and feeds it to the interpreter


file = open('sample_lolcodes/hello_world.lol', 'r')
lines = file.read() #splits the file into separate lines
#might want to implement a way to deal with comments (like removing them)\
file.close() #make sure to close the file you open

lines = lines.splitlines()
lineLen = len(lines)
lines = lexical_analyzer.cleanCode(lines, lineLen)
print(lines)
# # put the code that's been cleaned of 
# for num in range(0, len(lines)):
#     # print(lines[num])

#     lexical_analyzer.lexicalAnalysis(lines[num])
#     # lexical analyzer here
#     # syntax analyzer here
#     # semantic analyzer here
#     # do what the line says
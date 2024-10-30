import lexical_analyzer
# This file reads the sample file per line and feeds it to the interpreter

file = open('sample_lolcodes/hello_world.lol', 'r')
lines = file.read().splitlines() #splits the file into separate lines
file.close() #make sure to close the file you open

for num in range(0, len(lines)):
    # print(lines[num])
    #might want to remove the OBTW -- TLDR before putting into lexical analyzer
    lexical_analyzer.lexicalAnalysis(lines[num])
    # lexical analyzer here
    # syntax analyzer here
    # semantic analyzer here
    # do what the line says
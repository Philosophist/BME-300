# CalculateDistancePatternDna.py
#
# Written by: Steven Parker and Lynn Bui
#
#
#########################################
# Upload the Dna file
def readFile(file_name):
    data = []
    file = open(file_name, "r")    
    for line in file:
       data.append(line.strip("\n")) 
    return data

# Hamming Distance function
def HammingDistance(pat1,pat2):
    count=0
    for i in range(len(pat1)): # Check for differences in patterns
        if pat1[i] != pat2[i]:
            count += 1
    return count # Return the hamming distance

# Calculate Distance Pattern Dna function
def CDPD(data,pattern,d):
    scoreDict={}
    for line in data:
        scoreDict[line]=HammingDistance(line,pattern)
    bestPattern=
    output=[] #create a list for an output
    # Row loop
    for i in range
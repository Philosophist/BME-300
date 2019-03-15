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
def CDPD(data,pattern):
    mot=[]
    k=len(pattern)
    for line in data:
        dict={}
        for i in range(len(line)-k):
            nPat=line[i:k+i]
            dict[nPat]=HammingDistance(nPat,pattern)
        bestPattern=min(dict)
        mot.append(dict[bestPattern])
    print(sum(mot))

CDPD(readFile('Dna.txt'),"AAA")
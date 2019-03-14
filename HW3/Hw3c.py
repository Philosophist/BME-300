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
    dist_score=len(pattern) # The maximum dist_score
    bestPattern=""
    motif=[]
    for i in range(len(data)+1):
        for j in range(len(data[i])-len(pattern)+1):
            possiblePattern=data[j:j+len(pattern)]
            ds=HammingDistance(pattern,possiblePattern)
            if ds < dist_score:
                dist_score = ds #update the dist_score
                bestPattern = possiblePattern
        motif.append((bestPattern))
    return motif

pattern = "AAA"
DNA_data = readFile("Dna.txt")
printFreqsDict(frequencies_dict)


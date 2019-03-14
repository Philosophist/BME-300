# CalculateDistancePatternDna.py
#
# Written by: Steven Parker and Lynn Bui
#
#
#########################################
# Upload the Dna file
def readFile(file_name):
    data = ""
    file = open(file_name, "r")
    return data

# Hamming Distance function
def HammingDistance(pat1,pat2,d):
    count=0
    for i in range(len(pat1)): # Check for differences in patterns
        if pat1[i] != pat2[i]:
            count += 1
        if d < count:
            return False # return False if over hamming distance
    return True # return True if at or under hamming distance

# Calculate Distance Pattern Dna function
def CDPD(data,pattern,d):
    distScore=d
    bestPattern=""
    output=[] #create a list for an output
    # Row loop
    for i in range
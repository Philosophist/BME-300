# MotifFastFinder.py
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

# Motifs function
def make_motif(k,Dna):
    motif=[]
    for i in range(len(Dna)):
        rand = Random () #edit later
        if rand >=(n-k) & (rand <= n): #n is len(row)
            start = rand -k
            end = rand
        else:
            start = rand
            end = rand + k
        motif(i)=Dna(i)[start,end]
        motif.append(motif(i))
    return motif
# Profile function

# Motifs Update function

# Score function

# GibbsSampler function
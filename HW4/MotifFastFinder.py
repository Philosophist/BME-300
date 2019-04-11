# MotifFastFinder.py
#
# Written by: Steven Parker and Lynn Bui
#
#
#########################################

import random
# Upload the Dna file
def readFile(file_name):
    data = []
    file = open(file_name, "r")
    for line in file:
       data.append(line.strip("\n"))
    return data

# Motifs function
def make_motif(dna,k,t,n):
    motif=[]
    for i in range(t):
        rand = random.randint(0,n-k-1)
        start = rand
        end = rand + k
        motif.append(dna(i)[start,end])
    return motif
# Profile function

# Motifs Update function

# Score function

# GibbsSampler function
def GibbsSampler(dna, k, t, n, N):
    make_motif(dna, k, n)


mlen = 3
iteration = 10
DNA = readFile("Dna1")
dnalen = len(DNA)
linlen = len(DNA(0))
GibbsSampler(DNA, mlen, dnalen, linlen, iteration)

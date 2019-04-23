# MotifFastFinder.py
#
# Written by: Steven Parker and Lynn Bui
#
#
#########################################
import math
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
    motif_mat=[]
    for i in range(t):
        rand = random.randint(0,n-k-1)
        start = rand
        end = rand + k
        motif_mat.append(dna(i)[start,end])
    return motif_mat

# This function creates profile matrix from given motifs matrix.
# The i_th row of the motifs matrix should not be considered. 
# The value of i is a random number generated outside of this fucntion.
def make_profile(motifs, i):
    # profile = []
	# insert your code here ... 
	# return profile
    pass  	# after inserting your code, this line needs to be removed 
	

# This function profiles randomly generated k-mer in the i_th sequence
# The index i was chosen randomly
# Also after profiling all k-mers one k-mer will be selected randomly proportional
# to its probability value calculated from profile matrix 
def profile_motif(profile, Dna, i):
    # motif_i = ""
	# insert your code here ... 
	# retrun motif_i
    pass   # after inserting your code, this line needs to be removed 
    
# Motifs Update function

def motif_score(motifs):
    #score = 0
	# insert your code here ... 
	#return score
    pass # after inserting your code, this line needs to be removed 

# GibbsSampler function
def GibbsSampler(dna, k, t, n, N):
    motif_mat = make_motif(dna, k, t, n)
    



mlen = 3
iteration = 10
DNA = readFile("Dna1")
dnalen = len(DNA)
linlen = len(DNA(0))
GibbsSampler(DNA, mlen, dnalen, linlen, iteration)

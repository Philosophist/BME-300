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

# This is a helper function that returns count and profile matrixes
def make_countmatrix(matrix):

    m = len(matrix) 
    n = len(matrix[0])
	
    hasZero = False
    seq = "" 
    A = C = G = T = 0
    sum = m
    column_count = []
    count_matrix = []
    profile_calc = []	
    profile_matrix = []     
	
    for column in range(n):
        for row in range(m):
            seq = seq + matrix[row][column]
		
        seq = seq.lower()
        A = seq.count("a")
        C = seq.count("c")
        G = seq.count("g")
        T = seq.count("t")
		
        if ((A == 0) or (C == 0) or (G == 0) or (T == 0)):
            hasZero = True
            sum = 2 * m

        column_count.append(A)
        column_count.append(C)
        column_count.append(G)	 
        column_count.append(T)
	
        seq = ""
        count_matrix.append(column_count)
        column_count = [] 
       
    for column in range(n):
        for nt in range(4):
            if (hasZero == True):
                count_matrix[column][nt]  = count_matrix[column][nt]  + 1          
            profile_calc.append(round((count_matrix[column][nt] / sum), 2))
  				
        profile_matrix.append(profile_calc)
        profile_calc = []        
		
    return (count_matrix, profile_matrix)

def make_profile(motifs, i):
	# remove row i from motifs
    new_motifs = []
    for row in range(len(motifs)):
        if (row != i):
            new_motifs.append(motifs[row])
    count_matrix, profile_matrix = make_countmatrix(new_motifs)
    return (profile_matrix)

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

	# remove row i from motifs
    new_motifs = []
    for row in range(len(motifs)):
        if (row != i):
            new_motifs.append(motifs[row])
			
    count_matrix, profile_matrix = make_countmatrix(new_motifs)
    return (profile_matrix)	

# This function profiles randomly generated k-mer in the i_th sequence
# The index i was chosen randomly
# Also after profiling all k-mers one k-mer will be selected randomly proportional
# to its probability value calculated from profile matrix 
def profile_motif(profile, dna, k, i):
    motif_i = dna(i)
    prof_i = []
    nt = {"A":0,"C":1,"G":2,"T":3}
    for start to range(len(motif_i)-k+1):
        prob = 1
        for index to range(k):
            prob = prob * profile[start+index][nt[motif_i[start+index]]]
        }
    

        prof_i.append()
	retrun motif_i
    
# This function returns the score of the updated motifs matrix
def motif_score(motifs):
    m = len(motifs) 
    n = len(motifs[0])
	
    hasZero = False
    seq = "" 
    A = 0
    C = 0
    G = 0
    T = 0
    sum_count = 0
    max_num = 0
    column_count = []
    score_vector = []
    score = 0
	
    for column in range(n):
        for row in range(m):
            seq = seq + motifs[row][column]
        #print (seq)
        seq = seq.lower()
        A = seq.count("a")
        C = seq.count("c")
        G = seq.count("g")
        T = seq.count("t")
			
        column_count.append(A)
        column_count.append(C)
        column_count.append(G)	 
        column_count.append(T)
        sum_count =  A+C+G+T
        max_num = max(column_count)
        score_vector.append(sum_count - max_num )
        seq = ""
        column_count = []
		
    score = sum(score_vector)			
    return (score, score_vector)



# GibbsSampler function
def GibbsSampler(dna, k, t, n, N):
    motif_mat = make_motif(dna, k, t, n)
    randLine = random.randint(0,range(len(motif_mat))
    new_profile = make_profile(motif_mat, randLine)
    profile_motif(new_profile, dna, k, randLine)


mlen = 3
iteration = 10
DNA = readFile("Dna1")
dnalen = len(DNA)
linlen = len(DNA(0))
GibbsSampler(DNA, mlen, dnalen, linlen, iteration)

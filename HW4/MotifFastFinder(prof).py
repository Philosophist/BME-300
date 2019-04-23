import math

"""
Description: This module solves the gibbs sampling problem
             for finding a set of best motifs in a set of 
			 given sequences.
			 
Written by: Arjang Fahim
Bugs:
Last update date: April, 16, 2019
Updates:
        1- make_countmatrix problem for zero values is fixed 
        2- make_countmatrix is added
		3- make_profile function is completed
		
Version: 1.1.0   
"""


def readFile(file_name):
    data = []
    file = open(file_name, "r")
    for line in file:
        data.append(line.strip("\n")) 
    return data
	
# This function returns a motif (t by k) matrix.
# The output format in python is a list of length t.
# for example:  motifs = [ "actg" , "cgta" , ...] k = 4   
def make_motif(Dna, k):
    # motifs = [] 
	# insert your code here ...
	# return motifs
    pass    # after inserting your code, this line needs to be removed 

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
       
    for row in range(m):
        for column in range(n):
            if (hasZero == True):
                count_matrix[row][column] = count_matrix[row][column] + 1          
            profile_calc.append (round((count_matrix[row][column] / sum), 2))
  				
        profile_matrix.append(profile_calc)
        profile_calc = []        
		
    return (count_matrix, profile_matrix)



	
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
def profile_motif(profile, Dna, i):
    # motif_i = ""
	# insert your code here ... 
	# retrun motif_i
    pass   # after inserting your code, this line needs to be removed 

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

def GibbsSampler(Dna, k, t, N):
    motifs = []
    motifs = make_motif(Dna, k)
	
	
    return ""
	

k = 3
N = 10

Dna = readFile("FilePath")
t = len(Dna)

GibbsSampler(Dna, k, t, N) 
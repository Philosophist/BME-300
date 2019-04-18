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
    # motif = [] 
	# insert your code here ...
	# return motifs
    pass    # after inserting your code, this line needs to be removed 
	
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

# This function returns the score of the updated motifs matrix
def motif_score(motifs):
    #score = 0
	# insert your code here ... 
	#return score
    pass # after inserting your code, this line needs to be removed 

def GibbsSampler(Dna, k, t, N):
    motifs=[]
    motifs=make_motif(Dna, k)
    pass
	

k = 3
N = 10
Dna = readFile("FilePath")
t = len(Dna)

GibbsSampler(Dna, k, t, N)

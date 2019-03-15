mots = [
    'ACCAGCTA',
    'TGCAGAAT',
    'AGGCCAAA',
    'AGCGGCTA',
    'CCGTGCCA',
    'AGCTGCTA',
    'TTCTGATT',
    'AGCTCCTG',
    'AGCTCCTC',
    'AGCATACG'
    ]

def consensus(motArr):
    for i in range(len(motArr(0))): # length of each string 
        dict = {'G':0,'C':0,'A':0,'T':0}
        for j in range(len(motArr)): # the number of strings 
            dict(motArr[j][i]) += 1
        
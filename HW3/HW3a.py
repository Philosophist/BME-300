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
    dict = {}
    for i in range(len(motArr(0))): # length of each string 
        for j in range(len(motArr)): # the number of strings 

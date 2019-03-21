import math

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
    cons=[]
    for i in range(len(motArr[0])): # length of each string 
        dict = {'G':0,'C':0,'A':0,'T':0}
        for j in range(len(motArr)): # the number of strings 
            dict[motArr[j][i]] += 1
        m=max(dict.values())
        for j in dict:
            if dict[j] == m:
                cons.append(j)
    return cons

def countDict(motArr):
    count={'G':[],'C':[],'A':[],'T':[]}
    for i in range(len(motArr[0])): # length of each string 
        dict = {'G':0,'C':0,'A':0,'T':0}
        for j in range(len(motArr)): # the number of strings 
            dict[motArr[j][i]] += 1
        for j in dict:
            count[j].append(dict[j])
    return count

def score(motArr):
    count=[]
    cols=len(motArr[0])
    for i in range(cols): # length of each string 
        dict = {'G':0,'C':0,'A':0,'T':0}
        rows=len(motArr)
        for j in range(rows): # the number of strings 
            dict[motArr[j][i]] += 1
        m=max(dict.values())
        count.append(rows-m)
    return sum(count)

def profile(count):
    prof={'G':[],'C':[],'A':[],'T':[]}
    for i in range(len(count['A'])): # every column
        tot=count['G'][i]+count['C'][i]+count['T'][i]+count['A'][i]
        for j in count:  # every nucleotide
            prof[j].append(count[j][i]/tot)
    return prof

def entropy(prof):
    ent=[]
    for i in range(len(prof['A'])): # every column
        col=[]
        for j in prof:  # every nucleotide
            p = prof[j][i]
            if p == 0:
                col.append(0)
            else:
                col.append(p*math.log(p,2))  
        ent.append(round(-1*sum(col), 2))
    return ent


Cons = consensus(mots)
Score = score(mots)
Count = countDict(mots)
Profile = profile(Count)
Entropy = entropy(Profile)
print("Consensus Sequence: "+ str(Cons))
print("Score: "+ str(Score))   
print("Count Matrix: G "+ str(Count['G']))
print("              C "+ str(Count['C']))
print("              T "+ str(Count['T']))
print("              A "+ str(Count['A']))
print("Profile Matrix: G "+ str(Profile['G']))
print("                C "+ str(Profile['C']))
print("                T "+ str(Profile['T']))
print("                A "+ str(Profile['A']))
print("Entropy Vector: " + str(Entropy))
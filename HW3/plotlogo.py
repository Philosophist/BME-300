import matplotlib.pyplot as plt
import gact

# This function creates logo plot in python
def plot(data):
    fig, ax = plt.subplots(figsize=(10,3))
    all_scores = data
    x = 1
    maxi = 0
    for scores in all_scores:
        y = 0
        for base, score in scores:
            gact.letterAt(base, x,y, score, ax)
            y += score
        x += 1
        maxi = max(maxi, y)
    plt.xticks(range(1,x))
    plt.xlim((0, x)) 
    plt.ylim((0, maxi)) 
    plt.tight_layout()      
    plt.show()

	

def readFile(file_name):
    data = []
    file = open(file_name, "r")    
    for line in file:
       data.append(line.strip("\n").replace(" ","")) 
    return data

def profile(motArr):
    prof=[]
    cols=len(motArr[0])
    for i in range(cols): # length of each string 
        dict = {'G':0,'C':0,'A':0,'T':0}
        rows=len(motArr)
        for j in range(rows): # the number of strings 
            dict[motArr[j][i]] += 1
        tot=sum(dict.values())
        colProf=[]
        for j in dict:
            colProf.append((j,dict[j]/tot))
        prof.append(colProf)
    return prof
        

# data is in the "list of list" format 	
dat = readFile("motifs.txt")


# [[('C', 0.022), ('T', 0.058), ('A', 0.104), ('G', 0.248)],
# [('T', 0.046), ('G', 0.048), ('A', 0.084), ('C', 0.929)]]

plot(profile(dat))		
		  
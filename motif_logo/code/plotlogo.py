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

	
	
# data is in the "list of list" format 	
data = [[('C', 0.022), ('T', 0.058), ('A', 0.104), ('G', 0.248)],
        [('T', 0.046), ('G', 0.048), ('A', 0.084), ('C', 0.929)]]

plot(data)		
		  
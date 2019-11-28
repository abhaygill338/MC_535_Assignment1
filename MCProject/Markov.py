import numpy as np
#the code below take the 'current position' of the user, and time duration in hours as input.
#it return the probability of the user being at the grocery store after 'hours' time duration. 
def prob_grocery(current_location, hours,npM):
    time_transition_m = np.linalg.matrix_power(npM,hours)
    print(time_transition_m)
    return(time_transition_m[mapping[current_location]][3])
#the following code takes a list such as
#[1,1,2,6,8,5,5,7,8,8,1,1,4,5,5,0,0,0,1,1,4,4,5,1,3,3,4,5,4,1,1]
#with states labeled as successive integers starting with 0
#and returns a transition matrix, M,
#where M[i][j] is the probability of transitioning from i to j
def transition_matrix(transitions):
    n = 1+ max(transitions) #number of states

    M = [[0]*n for _ in range(n)]

    for (i,j) in zip(transitions,transitions[1:]):
        M[i][j] += 1

    #now convert to probabilities:
    for row in M:
        s = sum(row)
        if s > 0:
            row[:] = [f/s for f in row]
    return M

#test:





f=open('location')
lines=f.read().splitlines()
trans=[]
lines = list(filter(None, lines))
trans=[0]*(len(lines)-24)
split_list=[8*x for x in range(1,24)]
res = [lines[i : j] for i, j in zip([0] + 
          split_list, split_list + [None])]


ar=np.array(res)
ar1=ar[:,1:]
ar1=ar1.transpose()
ar2=ar1.flatten()
transition=ar2.tolist()
mapping={'Home':0,'Office':1,'Park':2,'Grocery':3,'Restaurant':4,'Movie':5}
t=list(map(mapping.get, transition))

m = transition_matrix(t)
for row in m: print(' '.join('{0:.2f}'.format(x) for x in row))
npM=np.array(m)
print(prob_grocery('Home',3,npM))





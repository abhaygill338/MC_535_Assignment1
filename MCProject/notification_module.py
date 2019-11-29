import numpy as np
import smtplib
import ssl
#the code below take the current position 'c_l' of the user, time duration 'h' in hours and transition matrix 'npM' 
# and returns the probability of the user being at the grocery store after h hours
def prob_grocery(c_l, h,npM):
    time_transition_m = np.linalg.matrix_power(npM,h)
    print('\nTransition Matrix after ',h,'hours')
    for row in time_transition_m: print(' '.join('{0:.2f}'.format(x) for x in row))
    # print(time_transition_m)
    return(time_transition_m[mapping[c_l]][3])

#the code below takes the history of location in the form of a list in the form of [0,1,2,1,3]
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

# The function mails the items in missing_list to the user at user_email. Or informs the user about a stocked fridge, if no items are missing.
def send_mail(user_email, missing_list):
    port = 465  # For SSL
    system_email = "mc.project.23.xyz@gmail.com"
    password = "asdf1@34"
    if len(missing_list)==0:
        message = 'Your fridge is stocked up. Have a good day!'
    else :
        message = "Hi there, \n Please buy the following items"+'\n'.join(missing_list)
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("mc.project.23.xyz@gmail.com", password)
        server.sendmail(system_email, user_email, message)
    print('\n Mail to ',user_email,'sent regarding',', '.join(missing_list))


#mapping of location as integers
mapping={'Home':0,'Office':1,'Park':2,'Grocery':3,'Restaurant':4,'Movie':5}

#reading history of user location in a list 'res' and converting it to the required list form (states labeled as successive integers starting with 0).
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
t=list(map(mapping.get, transition))

#Generating transition matrix
m = transition_matrix(t)
print('Transition Matrix')
for row in m: print(' '.join('{0:.2f}'.format(x) for x in row))
npM=np.array(m)

#input from the missing item module.
missing_list=['cereal']
if (prob_grocery('Home',3,npM))>0.01:
    send_mail('testmail@gmail.com',missing_list)







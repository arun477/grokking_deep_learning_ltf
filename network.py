import numpy as np

def neural_network(inputs, weights):
    hidden = inputs.dot(weights[0])
    prediction = hidden.dot(weights[1])
    return prediction

#hidden network weight
ih_wgt = np.array([ [0.1, 0.2, -0.1],
           [-0.1,0.1, 0.9], 
           [0.1, 0.4, 0.1] ] )

#output network weight
hp_wgt = np.array([ [0.3, 1.1, -0.3], 
           [0.1, 0.2, 0.0], 
           [0.0, 1.3, 0.1] ])

weights = [ih_wgt, hp_wgt]

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

inputs = np.array([toes[0], wlrec[0], nfans[0]])
prediction = neural_network(inputs, weights)
print(prediction)

[0.21350000000000002, 0.14500000000000002, 0.5065]

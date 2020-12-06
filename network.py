import numpy as np

def neural_network(weights, inputs):
    prediction  = inputs.dot(weights)
    return prediction

toes = np.array([8.5, 9.5, 10, 9])
wins_loss = np.array([0.65, 0.8, 0.75, 0.6])
num_fans = np.array([1.2 , 1.1, 1.4, 5.3])
weights = np.array([0.1, 0.2, 0])
inputs = np.array([toes[0], wins_loss[0], num_fans[0]])
prediction = neural_network(weights, inputs)
print(prediction)
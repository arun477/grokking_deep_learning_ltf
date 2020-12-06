def w_sum(weights, inputs):
    assert(len(weights) == len(inputs))
    output = 0
    for i in range(len(inputs)):
        output += weights[i] * inputs[i]
    return output
    
def neural_network(weights, inputs):
    prediction  = w_sum(weights, inputs)
    return prediction

toes = [8.5, 9.5, 10, 9]
wins_loss = [0.65, 0.8, 0.75, 0.6]
num_fans = [1.2 , 1.1, 1.4, 5.3]

weights = [0.1, 0.2, 0]
inputs = [toes[0], wins_loss[0], num_fans[0]]
prediction = neural_network(weights, inputs)
print(prediction)
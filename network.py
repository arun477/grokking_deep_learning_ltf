def w_sum(input, weights):
    assert(len(input) == len(weights))
    output = 0
    for i in range(len(input)):
        output += input[i] * weights[i]
    return output

def neural_network(input, weights):
    prediction = w_sum(input, weights)
    return prediction

def elementwise_multiplication(number, vector):
    output = []
    for i in range(len(vector)):
        output.append(vector[i]* number)
    return output

weights = [0.1, 0.2, -.1]
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]
win_or_lose_binary = [1, 1, 0, 1]
true = win_or_lose_binary[0]
input = [toes[0], wlrec[0], nfans[0]]

for iteration in range(100000):
    prediction = neural_network(input, weights)
    error = (prediction - true)**2
    delta = prediction - true
    weight_deltas = elementwise_multiplication(delta, weights)
    alpha = 0.01

    for i in range(len(weight_deltas)):
        weights[i] -= alpha * weight_deltas[i]

    print('-------\nError', str(error), "Prediction", prediction)
    print("Weights", weights)
    print("Weight Deltas", weight_deltas)
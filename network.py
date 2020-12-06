def w_sum(input, weights):
    assert(len(input) == len(weights))
    output = 0
    for i in range(len(input)):
        output += input[i] * weights[i]
    return output

def elementwise_multiplication(number, vector):
    output = []
    for i in range(len(vector)):
        output.append(vector[i]* number)
    return output

def neural_network(input, weights):
    prediction = elementwise_multiplication(input, weights)
    return prediction

weights = [0.3, 0.2, 0.9,]
alpha = 0.1
wlrec = [0.65, 1.0, 1.0, 0.9]

hurt = [0.1, 0.0, 0.0, 0.1]
win = [ 1, 1, 0, 1]
sad = [0.1, 0.0, 0.1, 0.2]

true = [hurt[0], win[0], sad[0]]
input = wlrec[0]
for iteration in range(100):
    prediction = neural_network(input, weights)
    deltas = []
    errors = []
    for i in range(len(true)):
        errors.append((prediction[i] - true[i])**2)
        deltas.append(prediction[i] - true[i])

    weight_deltas = elementwise_multiplication(input, deltas)

    for i in range(len(weights)):
        weights[i] -= weight_deltas[i] * alpha

    print('--------\nErrors', errors, 'Prediction', prediction)
    # print(deltas)
    print('weight_deltas', weight_deltas)
    # print(weights)
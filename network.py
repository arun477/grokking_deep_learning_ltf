def elementwise_multiplication(number, vector):
    output = []
    for i in range(len(vector)):
        output.append(number * vector[i])
    return output

def neural_network(weights, input):
    prediction  = elementwise_multiplication(input, weights)
    return prediction

weights = [0.3, 0.2, 0.9]
wins_loss = [0.65, 0.8, 0.8, 0.9]

input = wins_loss[0]
prediction = neural_network(weights, input)
print(prediction)
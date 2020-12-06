weight = 0.1
inputs = [8.5, 4.5, 6.5, 9.5]
def neural_network(weight, input):
    prediction = input * weight
    return prediction

input = inputs[0]
prediction = neural_network(weight, input)
print(prediction)
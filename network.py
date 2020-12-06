def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output


def vector_matrix_multiplictation(vect, matrix):
    assert(len(vect) == len(matrix))
    output = []
    for i in range(len(matrix)):
        output.append(w_sum(vect, matrix[i]))
    return output

def neural_network(inputs, weights):
    prediction = vector_matrix_multiplictation(inputs, weights)
    return prediction

# mxn = 3*3
weights = [[0.1, 0.1, -0.3],
           [0.1, 0.2, 0.0],
           [0.0, 1.3, 0.1]]

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

# mxn = 1*3
inputs = [toes[0], wlrec[0], nfans[0]]
prediction = neural_network(inputs, weights)
print(prediction)

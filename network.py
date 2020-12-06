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
    hidden = vector_matrix_multiplictation(inputs, weights[0])
    prediction = vector_matrix_multiplictation(hidden, weights[1])
    return prediction

#hidden network weight
ih_wgt = [ [0.1, 0.2, -0.1],
           [-0.1,0.1, 0.9], 
           [0.1, 0.4, 0.1] ] 

#output network weight
hp_wgt = [ [0.3, 1.1, -0.3], 
           [0.1, 0.2, 0.0], 
           [0.0, 1.3, 0.1] ] 

weights = [ih_wgt, hp_wgt]

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

inputs = [toes[0], wlrec[0], nfans[0]]
prediction = neural_network(inputs, weights)
print(prediction)

def w_sum(input, weights):
    assert(len(input) == len(weights))
    output = 0
    for i in range(len(input)):
        output += input[i] * weights[i]
    return output

def vect_mat_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    output = []
    for i in range(len(vect)):
        output.append(w_sum(vect, matrix[i]))
    return output

def elementwise_multiplication(number, vector):
    output = []
    for i in range(len(vector)):
        output.append(number * vector[i])
    return output

def create_zero_matrix(num_row, num_col):
    output = []
    for i in range(num_row):
        row = []
        for j in range(num_col):
            row.append(0)
        output.append(row)
    return output
        
def outer_product(vec_a, vec_b):
    output = create_zero_matrix(len(vec_a), len(vec_b))
    for i in range(len(vec_a)):
        for j in range(len(vec_b)):
            output[i][j] = vec_a[i] * vec_b[j]
    return output

def neural_network(input, weights):
    prediction = vect_mat_mul(input, weights)
    return prediction

weights = [[0.1, 0.1, -0.3],
            [0.1, 0.2, 0.0],
            [0.0, 1.3, 0.1] ]

alpha = 0.001

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65,0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

hurt = [0.1, 0.0, 0.0, 0.1]
win = [1, 1, 0, 1]
sad = [0.1, 0.0, 0.1, 0.2]

true = [hurt[0], win[0], sad[0]]
input = [toes[0], wlrec[0], nfans[0]]
for iteration in range(5):
        prediction = neural_network(input, weights)
        errors = []
        deltas = []
        for i in range(len(true)):
            errors.append((prediction[i] - true[i])**2)
            deltas.append(prediction[i] - true[i])

        weight_deltas = outer_product(input, deltas)

        for i in range(len(weights)):
            for j in range(len(weights[0])):
                weights[i][j] -= weight_deltas[i][j] * alpha
        print('---------\nError', str(errors), 'Prediction', prediction)
        # print(weights)

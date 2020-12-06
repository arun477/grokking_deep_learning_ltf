def elementwise_multiplication(vec_a, vec_b):
    output = 0
    for i in range(len(vec_a)):
        output += vec_a[i] * vec_b[i]
    return output

def elementwise_additon(vec_a, vec_b):
    output = []
    for i in range(len(vec_a)):
        output.append(vec_a[i] + vec_b[i])
    return output

def vector_sum(vec_a):
    output = 0
    for i in range(len(vec_a)):
        output += vec_a[i]
    return output

def vector_average(vec_a):
    output = []
    vector_length = len(vec_a)
    for i in range(len(vec_a)):
        output.append((vec_a[i]/vector_length))
    return output


vec_a = [1, 3, 4, 5]
vec_b = [2, 3, 1, 4]

print("elementwise_multiplication expected output 35 =>", elementwise_multiplication(vec_a, vec_b))
print("elementwise_additon expected output [3, 6, 5, 9] =>", elementwise_additon(vec_a, vec_b))
print("vector_sum expected output 13 =>", vector_sum(vec_a))
print("vector_average expected output [1, 3, 4, 5] =>", vector_average(vec_a))



weight = 0.5
input = 0.5
correct_prediction = 0.8
lr = 0.01

def neural_network(input, weight):
    prediction  = input * weight
    return prediction
prediction = neural_network(input, weight)   
error = (prediction - correct_prediction)**2



p_up = neural_network(input, weight+lr)
e_up = (p_up - correct_prediction)**2

p_down = neural_network(input, weight-lr)
e_down = (p_down - correct_prediction)**2


print('error up', e_up)
print('error down', e_down)
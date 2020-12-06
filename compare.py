weight = 0.1
alpha = 0.01


num_of_toes = [8.5]
win_or_lose_binary = [1]

input = num_of_toes[0]
goal_prediction = win_or_lose_binary[0]

for iteration in range(100):
    prediction = input * weight
    error = (prediction - goal_prediction)**2
    print('Error', str(error), 'Prediction', prediction)
    delta = prediction - goal_prediction
    weight_delta = delta * input
    weight -= weight_delta * alpha

weight, goal_of_prediction, input = (0.0, 0.8, 2)
alpha = 0.1

for iteration in range(20):
    print('----------\nWeight', weight)
    prediction = weight * input
    error = (prediction - goal_of_prediction)**2
    delta = prediction - goal_of_prediction
    weight_delta = delta * input
    weight = weight - weight_delta * alpha
    print('Error', error, ' Prediction', prediction)
    print('Delta', str(delta), ' Weight Delta', weight_delta)
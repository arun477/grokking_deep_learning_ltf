import numpy as np 
streetlights = np.array([
    [ 1, 0, 1 ],
[ 0, 1, 1 ],
[ 0, 0, 1 ],
[ 1, 1, 1 ],
[ 0, 1, 1 ],
[ 1, 0, 1 ]
])

walk_vs_stop = np.array([
    0, 1, 0, 1, 1, 0
])


alpha = 0.1
weights = np.array([0.5,0.48,-0.7])

for iteration in range(20):
    total_error = 0
    for row_index in range(len(streetlights)):
        inputs = streetlights[row_index]
        goal_of_prediction = walk_vs_stop[row_index]
        prediction = inputs.dot(weights)
        error = (prediction - goal_of_prediction) ** 2
        total_error += error
        delta = prediction - goal_of_prediction
        weights_delta = inputs * delta
        weights = weights - (weights_delta * alpha)
    print('-----\nError Total', total_error)
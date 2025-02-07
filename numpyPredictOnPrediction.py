import numpy as np

ih_wgt = np.array([[0.1, 0.2, -0.1], [-0.1, 0.1, 0.9], [0.1, 0.4, 0.1]]).T
hp_wgt = np.array([[0.3, 1.1, -0.3], [0.1, 0.2, 0.0], [0.0, 1.3, 0.1]]).T

weights = [ih_wgt, hp_wgt]

def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred
    
toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 8.5, 8.5, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wlrec[0], nfans[0]])
pred = neural_network(input, weights)
print(pred)

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]

biases = [2.0, 3.0, 0.5]


layer_outputs = []

for neuron_bias, neuron_weights in zip(biases, weights):
    neuron_ouput = 0
    for neuron_input, weight in zip(inputs, neuron_weights):
        neuron_ouput += neuron_input * weight
    neuron_ouput += neuron_bias
    layer_outputs.append(neuron_ouput)

print(layer_outputs)

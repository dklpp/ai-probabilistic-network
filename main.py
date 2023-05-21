from bayes import *
from weighting import *
from process_input import *

input_file = 'input.txt'
node_specs = convert_input_to_list(input_file)

print("\nNode specifications:\n", node_specs, sep="\n")
network = BayesNet(node_specs)
print('')
print("Current network:\n", network, sep='\n')
# print(likelihood_weighting('B', dict(A=True), network, 20000).show_approx())

print('\nWhat probability you want to calculate?\nWrite in this format: A|B, -C')
input_string = input()
print('\nHow many iterations you want to run?\n')
iter_input = int(input())

X, values_dict = process_input(input_string)

print(likelihood_weighting(X, dict(values_dict), network, iter_input).show_approx())
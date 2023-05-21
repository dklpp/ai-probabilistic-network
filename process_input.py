import itertools
import re


def convert_input_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    result = []

    for line in lines:
        line = line.strip().split()
        variable = line[0]
        num_parents = int(line[1])

        if num_parents == 0:
            probability = float(line[2])
            result.append((variable, '', probability))
        else:
            parents = ' '.join(line[2:2 + num_parents])
            probabilities = list(map(float, line[2 + num_parents:]))
            cpt = {}

            num_values = 2 ** num_parents
            value_combinations = itertools.product([False, True], repeat=num_parents)

            for i, values in enumerate(value_combinations):
                cpt[values] = probabilities[i]

            result.append((variable, parents, cpt))

    return result


def process_input(input_string):
    # Extracting everything before "|"
    split_parts = input_string.split("|")

    X = split_parts[0]
    input_string = input_string[2:]
    print(input_string)

    # Extracting letters and their truth values using regex pattern matching
    pattern_false = r"(?<=-)(\w)"
    matches_false = re.findall(pattern_false, input_string)

    pattern_true = r"(?<!-)(\w)"
    matches_true = re.findall(pattern_true, input_string)

    values_dict = {}

    for match in matches_true:
        letter = match[0]
        values_dict[letter] = True

    for match in matches_false:
        letter = match[0]
        values_dict[letter] = False

    return X, values_dict

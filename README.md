# ai-probabilistic-network

To calculate the probability write in this format: A|B, -C

Task.

A probabilistic network is given in external memory file input.txt. The probabilistic network in a file is represented based on these principles:

- A single line of file is dedicated to a single network node (variable);
- The order of nodes representation is from "Parents" to "Children". If an ordinary node is represented in a line of the file, it means, that all of the parents of this node are already represented in previous lines of the file;
- The line of the file, that represents the network root node has this structure: variable name, number of its parents, its parents indexes in the file, a list of conditional probabilities, starting with FF...FF, FF...FT, FF...TF, FF...TT and ending with the TT...TT case.

<img width="353" alt="image" src="https://github.com/dklpp/ai-probabilistic-network/assets/74605425/fb31f2a7-9a19-4db0-9e10-740c10df7706">

E.g., the probabilistic network displayed above would be represented in a file this way:

A 0       0.7  
B 1 0     0.1 0.4
C 1 0     0.6 0.8
D 2 2 1   0.6 0.7 0.1 0.2

Required: Write a program, that would:
- Read a given probabilistic network from a file to computer memory;
- Inquire what probability is of interest to the user (e.g. P(D), P(A|C,-B) or similar);
- Calculate the probability of interest to the user, gained using the stochastic likelihood weighting method;
- Present the answer to the user.

The program must be able to calculate the probability of a single variable, i.e examples like P(A,D|C,-B) are not required.

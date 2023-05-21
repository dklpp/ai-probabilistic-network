from probdistribution import *


def event_values(event, variables):
    """Return a tuple of the values of variables in event.
    >>> event_values ({'A': 10, 'B': 9, 'C': 8}, ['C', 'A'])
    (8, 10)
    >>> event_values ((1, 2), ['C', 'A'])
    (1, 2)
    """
    if isinstance(event, tuple) and len(event) == len(variables):
        return event
    else:
        return tuple([event[var] for var in variables])


def weighted_sample(bn, e):
    """Sample an event from bn that's consistent with the evidence e;
    return the event and its weight, the likelihood that the event
    accords to the evidence."""
    w = 1 # initial weight
    event = dict(e)  # an event with elements initialized from e
    for node in bn.nodes:
        Xi = node.variable
        if Xi in e: # Xi is an evidence variable, e[Xi] = xi
            w *= node.p(e[Xi], event) # P(Xi = xi | parents(Xi))
        else:
            event[Xi] = node.sample(event) # random sample from P(Xi | parents(Xi))
    return event, w # event, weight


def likelihood_weighting(X, e, bn, N=10000):
    """Estimate the probability distribution of variable X given
    evidence e in BayesNet bn.
    X - the query variable
    e - observed values from evidence
    bn - a Bayesian network specifying joint distribution P(X1,..,Xn)
    N - the total num of samples to be generated
    >>> random.seed(1017)
    >>> likelihood_weighting('Burglary', dict(JohnCalls=T, MaryCalls=T),
    ...   burglary, 10000).show_approx()
    'False: 0.702, True: 0.298'
    """
    W = {x: 0 for x in bn.variable_values(X)} # W, a vector of weighed counts for each value of X, initially 0

    for j in range(N):
        sample, weight = weighted_sample(bn, e)
        W[sample[X]] += weight
    return ProbDistribution(X, W) # with normalization
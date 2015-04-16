#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from math import *
import scipy.stats


def BOPF(data):

    # Initial value
    S = data['S']
    X = data['X']
    t = data['t']
    n = data['n']
    s = data['s'] / 100  # convert from percentage to decimal
    r = data['r'] / 100
    u = exp(s * sqrt(t / n))
    d = 1 / u   # d = exp(-s * sqrt(t / n))
    r_ = r * t / n
    R = exp(r_)
    a = ceil(log(X / (S * (d ** n))) / log(u / d))  # Smallest int S_T >= X
    p = (R - d) / (u - d)  # Risk-neutral P

    # European Options
    CallSum1 = CallSum2 = 0
    PutSum1 = PutSum2 = 0

    for _ in range(int(a), n):
        CallSum1 += scipy.stats.binom.pmf(_, n, p * u / R)
        CallSum2 += scipy.stats.binom.pmf(_, n, p)

    for _ in range(int(a)):
        PutSum1 += scipy.stats.binom.pmf(_, n, p * u / R)
        PutSum2 += scipy.stats.binom.pmf(_, n, p)

    EuroCall = S * CallSum1 - X * exp(-r_ * n) * CallSum2
    EuroPut = X * exp(-r_ * n) * PutSum2 - S * PutSum1

    # America put
    # Initialize Value at time t
    ValueFlow = [max(X - (S * (u ** (n-i)) * (d ** i)), 0) for i in range(n+1)]
    callValueFlow = [max((S * (u ** (n-i)) * (d ** i)) - X, 0) for i in range(n+1)]

    # Run backward to time 0
    for time in reversed(range(n)):
        # Payoff of early exercise
        EarlyExercise = [max(X - (S * (u ** (time-i)) * (d ** i)), 0) for
                         i in range(time+1)]

        #callEarlyExercise = [max((S * (u ** (time-i)) * (d ** i)) - X, 0) for
        #                 i in range(time+1)]
        # Continuation value
        ValueFlow = [((p * ValueFlow[i] + (1-p) * ValueFlow[i+1]) / R) for
                     i in range(time+1)]

        #callValueFlow = [((p * callValueFlow[i] + (1-p) * callValueFlow[i+1]) / R) for
        #             i in range(time+1)]

        # Find the larger value
        ValueFlow = [max(EarlyExercise[i], ValueFlow[i]) for
                     i in range(len(ValueFlow))]

        #callValueFlow = [max(callEarlyExercise[i], callValueFlow[i]) for
        #             i in range(len(callValueFlow))]

    # Output Information

    outputs = [('European Call', str(EuroCall)),
               #('European Put', str(EuroPut)),
               ('American Call', str(EuroCall)),
               ('American Call', str(callValueFlow[0])),
               ('American Put', str(ValueFlow[0]))]

    # Aligned output
    print "S=%r, X=%r, s=%r%%, t=%r, n=%r, r=%r %%:" % (S, X, data['s'],
                                                        t, n, data['r'])
    for output in outputs:
        print "- {item:13}: {value[0]:>4}.{value[1]:<12}".format(
              item=output[0], value=output[1].split('.') if
              '.' in output[1] else (output[1], '0'))


import sys
import json
if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location) as data_file:
            data = json.load(data_file)
        for test in data:
            BOPF(test)
        print "~~ end ~~"
    else:
        print 'This requires an input file.  Please select one from the data \
               directory. (e.g. python HW2.py ./data)'

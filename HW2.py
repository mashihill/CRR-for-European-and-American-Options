#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from math import *
import scipy.stats

def BOPF(S, X, s, t, n, r):
    # European Options
    u = exp(s * sqrt(t / n))
    d = 1 / u
    #d = exp(-s * sqrt(t / n))
    r_ = r * t / n
    R = exp(r_)
    a = ceil(log(X / (S * (d ** n))) / log(u / d))
    p = (R - d) / (u - d)
    CallSum1 = CallSum2 = 0
    PutSum1 = PutSum2 = 0

    for _ in range(int(a),n):
        CallSum1 += scipy.stats.binom.pmf(_, n, p * u / R)
        CallSum2 += scipy.stats.binom.pmf(_, n, p)

    for _ in range(int(a)):
        PutSum1 += scipy.stats.binom.pmf(_, n, p * u / R)
        PutSum2 += scipy.stats.binom.pmf(_, n, p)

    EuroCall = S * CallSum1 - X * exp(-r_ * n) * CallSum2
    EuroPut = X * exp(-r_ * n) * PutSum2 - S * PutSum1

    print "European Call: ", EuroCall
    print "European Put: ", EuroPut

    # America put
    # Initialize Value at time t
    ValueFlow = [ max(X - (S * (u ** (n-i)) * (d ** i)), 0) for i in range(n+1) ]

    # Run back to time 0
    for time in reversed(range(n)):
        # Payoff of early exercise 
        EarlyExercise = [ max(X - (S * (u ** (time-i)) * (d ** i)), 0) for i in range(time+1) ]
        # Continuation value
        ValueFlow = [ ((p * ValueFlow[i] + (1-p) * ValueFlow[i+1]) / R) for i in range(time+1) ]
        # Find the larger value
        ValueFlow = [ max(EarlyExercise[i], ValueFlow[i]) for i in range(len(ValueFlow)) ]

    print "American Call: ", EuroCall # Same as European call
    print "American Put: ", ValueFlow[0]

    return 


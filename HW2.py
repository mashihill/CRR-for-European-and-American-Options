#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *
import scipy.stats


def BOPF(S, X, s, t, n, r):
    u = exp(s * sqrt(float(t) / n))
    d = exp(-s * sqrt(float(t) / n))
    r_ = r * float(t) / n
    a = ceil(log(float(X) / (S * (d ** n))) / log(float(u) / d))
    p = (exp(r_) - d) / (u - d)
    sum1 = sum2 = 0
    
    for _ in range(int(a),n):
        sum1 += scipy.stats.binom.pmf(_, n, p * float(u) / (exp(r_)))
        sum2 += scipy.stats.binom.pmf(_, n, p)

    return (S * sum1 - X * exp(-r_ * n) * sum2)


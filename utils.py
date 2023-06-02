import math
import numpy as np

colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00']

c0 = ['#377eb8', '#76abd6', '#c4dbed']
c1 = ['#ff7f00', '#ffb366', '#ffe6cc']


# Utility functions and their derivatives: 
def u_unif(t, k0): # Uniform
    if t < k0:
        return 1 - t / k0
    else:
        return 0

def uinv_unif(u, k0): # Uniform inverse 
    return k0 * (1 - u)

def u_exp(t, k0): # Exponential 
    return math.exp(- t / k0)

def uinv_exp(u, k0): # Exponential inverse 
    return -k0 * math.log(u)

# def uprime_exp(t, k0):
#     return - math.exp(- t / k0) / k0

def u_pareto(t, k0, a): # Pareto 
    if t < k0:
        return 1
    else:
        return (k0 / t) ** a

def uprime_pareto(t, k0, a): # Pareto derivative 
    if t < k0:
        return 0
    else:
        return - a * k0**a / t**(a + 1)

def uinv_pareto(u, k0, a): # Pareto inverse 
    return k0 / u**(1 / a)

def u_ll(t, k0, a): # Log-Laplace
    if  t < k0:
        return 1 - (t / k0) ** a / 2
    else:
        return (k0 / t) ** a / 2

# Uniform
def pdf_uniform(t, t0):
    if t < t0:
        return 1 / t0
    else:
        return 0


def cdf_uniform(t, t0):
    if t < t0:
        return t / t0
    else:
        return 1


# Exponential
def pdf_exponential(t, t0):
    return math.exp(- t / t0) / t0


def cdf_exponential(t, t0):
    return 1 - math.exp(- t / t0)


# Pareto
def pdf_pareto(t, t0, a):
    if t < t0:
        return 0
    else:
        return a * t0 ** a / t ** (a + 1)


def cdf_pareto(t, t0, a):
    if t < t0:
        return 0
    else:
        return 1 - (t0 / t) ** a


# (gen) log Laplace
def pdf_genlogLaplace(t, t0, a, b):
    if t < t0:
        return a * b * (t / t0) ** (b - 1) / (a + b) / t0
    else:
        return a * b * (t0 / t) ** (a + 1) / (a + b) / t0


def cdf_genlogLaplace(t, t0, a, b):
    if t < t0:
        return a / (a + b) * (t / t0) ** b
    else:
        return 1 - b / (a + b) * (t0 / t) ** a


# log Normal
def pdf_logNormal(t, t0, sigma, eps=.0001):
    t = t + eps
    return math.exp(- math.log(t / t0) ** 2 / 2 / sigma ** 2) / t / sigma / math.sqrt(2 * math.pi)


def cdf_logNormal(t, t0, sigma, eps=.0001):
    t = t + eps
    return 1 / 2 + math.erf(math.log(t / t0) / math.sqrt(2) / sigma) / 2


# Piecewise
def pdf_piecewise(t, t0, t1, delta):
    if t < t0:
        if t < t1:
            return delta / t1
        else:
            return (1 - delta) / (t0 - t1)
    else:
        return 0


def cdf_piecewise(t, t0, t1, delta):
    if t < t0:
        if t < t1:
            return delta * t / t1
        else:
            return delta + (1 - delta) * (t - t1) / (t0 - t1)
    else:
        return 1


# Cost
def cost_constant(t, a=1.0):
    return a


def cost_linear(t, a=1.0):
    return a * t


def cost_log(t, a=1.0):
    return a * math.log(1 + t)


def cost_step(t, ts, cs, b):
    for i in range(len(ts)):
        if t >= ts[-i-1]:
            return b + cs[-i-1]
    return b


# Misc
def integrate(fn, x0, x1, steps=None):
    """ If fn has discontinuities at points in <steps>, breaks integral up into pieces """
    if steps is None:
        steps = []
    val = 0
    errors = []
    _x0 = x0
    for i, x in enumerate(steps):
        val += _integrate.quad(fn, _x0, x)[0]
        errors.append(_integrate.quad(fn, _x0, x)[1])
        _x0 = x
    val += _integrate.quad(fn, _x0, x1)[0]
    errors.append(_integrate.quad(fn, _x0, x1)[1])
    return (val, errors)

    
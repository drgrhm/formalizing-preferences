import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as _integrate

from utils import *

fontsize_title = 20
fontsize_title_small = 8
fontsize_ylabel = 10
linewidth_thick = 8
linewidth_main = 5
linewidth_slim = 2
linewidth_skinny = .75

# Plotting functions
def plot_pdf(pdf, k0, tmax, title, savepath, colour):
    ts = np.linspace(0, tmax, 1000)
    plt.axvline(k0, c='grey', linestyle='--')
    plt.plot(ts, [pdf(t) for t in ts], linewidth=linewidth_main, c=colour)
    plt.xlim(0, tmax)
    plt.ylim(-.0002, .062)
    plt.title(title, fontsize=fontsize_title)
    plt.savefig(savepath, bbox_inches='tight')
    plt.clf()


def plot_util(cdf, k0, tmax, title, savepath, colour):
    ts = np.linspace(0, tmax, 1000)
    plt.axvline(k0, c='grey', linestyle='--')
    plt.plot(ts, [1 - cdf(t) for t in ts], linewidth=linewidth_main, c=colour)
    plt.xlim(0, tmax)
    plt.ylim(-.005, 1.005)
    plt.title(title, fontsize=fontsize_title)
    plt.savefig(savepath, bbox_inches='tight')
    plt.clf()


def plot_pdfs(dists, k0, tmax):
    for k in dists.keys():
        plot_pdf(dists[k]['pdf'], k0, tmax, "pdf (" + dists[k]['paramstring'] + ")", "img/pdf_{}.pdf".format(k), dists[k]['color'])


def plot_utils(dists, k0, tmax):
    for k in dists.keys():
        plot_util(dists[k]['cdf'], k0, tmax, "utility (" +  dists[k]['paramstring'] + ")", "img/util_{}.pdf".format(k), dists[k]['color'])


def plot_utils_on_grid(dists, k0, tmax, figscale=1):
    fig, ax = plt.subplots(1, len(dists.keys()), figsize=[figscale * len(dists.keys()), figscale])
    ts = np.linspace(0, tmax, 1000)
    
    for j, dist in enumerate(dists.keys()):
        ax[j].plot(ts, [1 - dists[dist]['cdf'](t) for t in ts], linewidth=linewidth_thick, c=dists[dist]['color'])
        ax[j].set_title(dists[dist]['title'], fontsize=12)

    for a in ax.flat:        
        a.set(xlim=(0, tmax), 
              ylim=(-.01, 1.01),
              xticks=[0, 24, 48],
              yticks=[0, .5, 1],
              aspect=tmax)
    
    for a in ax.flat:
        a.label_outer()

    plt.savefig("img/maxent_grid.pdf", bbox_inches='tight')
    plt.clf()


if __name__ == '__main__':

    _k0 = 24
    _tmax = 65
    _alpha_pareto = 1
    _alpha_ll = 2
    _beta_ll = 5
    _sigma = .5
    _delta = .3
    _k1 = 12

    dists = {
             'uni': {'pdf': lambda t: pdf_uniform(t, _k0),
                     'cdf': lambda t: cdf_uniform(t, _k0),
                     'title': "Uniform(0,{})".format(_k0),
                     'paramstring': r"$\kappa_0 = {}$".format(_k0),
                     'color': "red"},
             'exp': {'pdf': lambda t: pdf_exponential(t, _k0),
                     'cdf': lambda t: cdf_exponential(t, _k0),
                     'title': "Exponential({})".format(_k0),
                     'paramstring': r"$\kappa_0 = {}$".format(_k0),
                     'color': "darkorange"},
             'par': {'pdf': lambda t: pdf_pareto(t, _k0, _alpha_pareto),
                     'cdf': lambda t: cdf_pareto(t, _k0, _alpha_pareto),
                     'title': "Pareto({},{})".format(_k0, _alpha_pareto),
                     'paramstring': r"$\kappa_0 = {}$, $\alpha = {}$".format(_k0, _alpha_pareto),
                     'color': "gold"},
             'llp': {'pdf': lambda t: pdf_genlogLaplace(t, _k0, _alpha_ll, _alpha_ll),
                     'cdf': lambda t: cdf_genlogLaplace(t, _k0, _alpha_ll, _alpha_ll),
                     'title': "logLaplace({},{})".format(_k0, _alpha_ll),
                     'paramstring': r"$\kappa_0 = {}$, $\alpha = {}$".format(_k0, _alpha_ll),
                     'color': "green"},
             'gll': {'pdf': lambda t: pdf_genlogLaplace(t, _k0, _alpha_ll, _beta_ll),
                     'cdf': lambda t: cdf_genlogLaplace(t, _k0, _alpha_ll, _beta_ll),
                     'title': "genlogLaplace({},{},{})".format(_k0, _alpha_ll, _beta_ll),
                     'paramstring': r"$\kappa_0 = {}$, $\alpha = {}$, $\beta = {}$".format(_k0, _alpha_ll, _beta_ll),
                     'color': "blue"},
             'lno': {'pdf': lambda t: pdf_logNormal(t, _k0, _sigma),
                     'cdf': lambda t: cdf_logNormal(t, _k0, _sigma),
                     'title': "logNormal({},{})".format(_k0, _sigma),
                     'paramstring': r"$\kappa_0 = {}$, $\sigma = {}$".format(_k0, _sigma),
                     'color': "indigo"},
             'pwi': {'pdf': lambda t: pdf_piecewise(t, _k0, _k1, _delta),
                     'cdf': lambda t: cdf_piecewise(t, _k0, _k1, _delta),
                     'title': "Piecewise({},{},{})".format(_k1, _k0, _delta),
                     'paramstring': r"$\kappa_0 = {}$, $\kappa_1 = {}$, $\delta = {}$".format(_k0, _k1, _delta),
                     'color': "violet"}
    }

    plot_pdfs(dists, _k0, _tmax)
    plot_utils(dists, _k0, _tmax)
    
    plot_utils_on_grid(dists, _k0, _tmax, figscale=2.2)







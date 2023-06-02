import math
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from utils import u_unif, u_exp, u_pareto, u_ll


fontsize_main = 18
fontsize_subtitle = 11
fontsize_title = 16

def plot_dist_cdfs(dists, t_max, title):
    ts = np.linspace(0, t_max, 100)
    for dist in dists:
        us = [dist['u'](t, **dist['params']) for t in ts]
        plt.plot(ts, us, label=dist['name'])
    plt.legend()
    plt.savefig(title, bbox_inches='tight')
    plt.clf()


# https://stackoverflow.com/questions/18926031/how-to-extract-a-subset-of-a-colormap-as-a-new-colormap-in-matplotlib
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


if __name__ == "__main__":

    np.random.seed(986)
    data_file = "leaps-and-bounds/measurements.dump" 
    data = pickle.load(open(data_file, 'rb'))
    t_max = 900 # this data was generated with a 900s timeout     

    configs = list(data.keys())
    m = len(data[configs[0]])
    config_ids = {}
    for i, config in enumerate(configs):
        config_ids[config] = i

    dists = [
         {'name': "Uniform({})",        'params':{'k0': 5},          'u': u_unif},
         {'name': "Exp({})",            'params':{'k0': .1},         'u': u_exp},
         {'name': "Pareto({}, {})",     'params':{'k0': 1,  'a': 5}, 'u': u_pareto},
         {'name': "LogLaplace({}, {})", 'params':{'k0': .1, 'a': 5}, 'u': u_ll},
         ]

    for dist in dists:        
        scores = []
        for config in configs:
            score = np.mean([dist['u'](t, **dist['params']) for t in data[config]])
            scores.append((score, config))
        dist['scores'] = sorted(scores, reverse=True)

    cross_scores = np.zeros((len(dists), len(dists)))
    for j, train_dist in enumerate(dists): 
        runtimes = data[train_dist['scores'][0][1]] # runtimes of the best configuration according to train_dist utility finction 
        for i, test_dist in enumerate(reversed(dists)): # reversed .... 
            cross_scores[i, j] = np.mean([test_dist['u'](t, **test_dist['params']) for t in runtimes])
    
    cross_scores = cross_scores / np.amax(cross_scores, axis=1)[:,None]

    plt.pcolormesh(cross_scores, cmap=truncate_colormap(plt.get_cmap('Reds_r'), 0.4, 1))

    for y in range(cross_scores.shape[0]):
        for x in range(cross_scores.shape[1]):
            plt.text(x + 0.5, y + 0.5, '{:.3f}'.format(cross_scores[y, x]), horizontalalignment='center', verticalalignment='center', fontsize=fontsize_main)

    plt.xticks([i + .5 for i, _ in enumerate(dists)], [d['name'].format(*d['params'].values()) for d in dists], fontsize=fontsize_subtitle)
    plt.yticks([i + .5 for i, _ in enumerate(reversed(dists))], reversed([d['name'].format(*d['params'].values()) for d in dists]), fontsize=fontsize_subtitle)
    ax = plt.gca()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.tick_params(axis='x', which='both',length=0)
    ax.tick_params(axis='y', which='both',length=0)

    fig = plt.gcf()
    fig.set_size_inches((9, 3))

    plt.xlabel("Optimized utility function", fontsize=fontsize_title)
    plt.ylabel("True utility function", fontsize=fontsize_title)

    plt.savefig('img/util_table.pdf', bbox_inches='tight')
    plt.clf()












    


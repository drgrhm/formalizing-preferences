import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils import u_pareto, u_unif, u_exp

if __name__ == "__main__":    

    # df = pd.read_csv("dat/r_main.csv")
    df = pd.read_csv("dat/r_parallel.csv")    
    solvers = sorted(df.columns[3:])
    runtimes = dict([(s, []) for s in solvers])

    solver_color = dict([(s, len(solvers) - i) for i, s in enumerate(solvers)])
    color_data = []
    solver_labels = []

    k0_unif1 = 20
    k0_unif2 = 500
    k0_par1 = 5
    a_par1 = 3
    k0_par2 = 5
    a_par2 = 1
    k0_exp = 1

    utils = {'Uniform({})'.format(k0_unif1): [], 
             'Uniform({})'.format(k0_unif2): [], 
             'Pareto({}, {})'.format(k0_par1, a_par1): [], 
             'Pareto({}, {})'.format(k0_par2, a_par2): [], 
             'Exp({})'.format(k0_exp): []}

    for solver in solvers:
        for outcome in df[solver]:
            if outcome == 'timeout' or outcome == 'memout' or outcome == 'unverified':
                runtimes[solver].append(float('inf'))
            else:
                runtimes[solver].append(float(outcome))

        for u_func in utils.keys():            
            if u_func == 'Uniform({})'.format(k0_unif1):
                lb = np.mean([u_unif(t, k0_unif1) for t in runtimes[solver]])
            if u_func == 'Uniform({})'.format(k0_unif2):
                lb = np.mean([u_unif(t, k0_unif2) for t in runtimes[solver]])
            elif u_func == 'Pareto({}, {})'.format(k0_par1, a_par1):
                lb = np.mean([u_pareto(t, k0_par1, a_par1) for t in runtimes[solver]])
            elif u_func == 'Pareto({}, {})'.format(k0_par2, a_par2):
                lb = np.mean([u_pareto(t, k0_par2, a_par2) for t in runtimes[solver]])
            elif u_func == 'Exp({})'.format(k0_exp):
                lb = np.mean([u_exp(t, k0_exp) for t in runtimes[solver]])
            utils[u_func].append((lb, solver))

    for u_func in utils.keys():
        utils[u_func] = sorted(utils[u_func])
        color_data.append([solver_color[res[1]] for res in utils[u_func]]) # append ranking for colormap
        solver_labels.append([res[1] for res in utils[u_func]]) # append ranking for colormap)
    color_data = np.transpose(color_data)
    solver_labels = np.transpose(solver_labels) 
    
    plt.pcolormesh(color_data, cmap='tab20')

    for y in range(color_data.shape[0]):
        for x in range(color_data.shape[1]):
            plt.text(x + 0.5, y + 0.5, solver_labels[y, x], horizontalalignment='center', verticalalignment='center', fontsize=6)

    plt.xticks([i + .5 for i, _ in enumerate(utils.keys())], utils.keys(), fontsize=8)
    plt.yticks([len(solvers) - .5, len(solvers) - 1.5, len(solvers) - 2.5], ["1st", "2nd", "3rd"], fontsize=8)
    ax = plt.gca()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.tick_params(axis='x', which='both',length=0)

    plt.xlabel("Utility Function")
    plt.ylabel("Ranking")

    fig = plt.gcf()
    fig.set_size_inches((7, 3))
    plt.savefig('img/sat_comp_table.pdf', bbox_inches='tight')







    
    
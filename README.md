# Formalizing Preferences Over Runtime Distributions

Experiments from the paper Formalizing Preferences Over Runtime Distributions, found [here](...url...). 

### Abstract

When trying to solve a computational problem, we are often faced with a choice between algorithms that are guaranteed to return the right answer but differ in their runtime distributions (e.g., SAT solvers, sorting algorithms). This paper aims to lay theoretical foundations for such choices by formalizing preferences over runtime distributions. It might seem that we should simply prefer the algorithm that minimizes expected runtime. However, such preferences would be driven by exactly how slow our algorithm is on bad inputs, whereas in practice we are typically willing to cut off occasional, sufficiently long runs before they finish. We propose a principled alternative, taking a utility-theoretic approach to characterize the scoring functions that describe preferences over algorithms. These functions depend on the way our value for solving our problem decreases with time and on the distribution from which captimes are drawn. We describe examples of realistic utility functions and show how to leverage a maximum-entropy approach for modeling underspecified captime distributions. Finally, we show how to efficiently estimate an algorithm's expected utility from runtime samples.

### Setup
```
mkdir dat img
```

### Maximum-Entropy Utility Functions
```
python generate_maxent_plots.py
```


### Automated Algorithm Configuration

Get data:
```
git clone https://github.com/deepmind/leaps-and-bounds.git
gzip -d ./leaps-and-bounds/measurements.dump.gz
```

Generate table:
```
python generate_utility_table.py
```


### 2021 International SAT Comptetiton

Get data (parallel track):
```
wget https://satcompetition.github.io/2021/results/r_parallel.csv -P ./dat
```

Generate table:
```
python generate_sat_comp_table.py
```

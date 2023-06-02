# Formalizing Preferences Over Runtime Distributions




Setup:
```
mkdir dat img
```

### Maximum-Entropy Utility Functions
```
python generate_maxent_plots.py
```


## Automted Algorithm Configuration

Get data:
```
git clone https://github.com/deepmind/leaps-and-bounds.git
gzip -d ./leaps-and-bounds/measurements.dump.gz
```

Generate table:
```
python generate_utility_table.py
```


## 2021 International SAT Comptetiton

Get data (parallel track):
```
wget https://satcompetition.github.io/2021/results/r_parallel.csv -P ./dat
```

Generate table:
```
python generate_sat_comp_table.py
```

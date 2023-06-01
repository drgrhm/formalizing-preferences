# Formalizing Preferences Over Runtime Distributions

## Setup
```
mkdir dat img
```

## 2021 International SAT Comptetiton

Get parallel track data
```
wget https://satcompetition.github.io/2021/results/r_parallel.csv -P ./dat
```

Get main track data
```
wget https://satcompetition.github.io/2021/results/r_main.csv -P ./dat
```


```
python generate_sat_comp_table.py
```

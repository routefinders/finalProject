## [learning] attempts at solving the TSP
- - -

currently implemented:
- greedy algorithms
    - hill climbing
    - simulated annealing

### usage:
    python tsp.py [-o <output image file>] [-v] [-m reversed_sections|swapped_cities]\ 
                   -n <max iterations> [-a hillclimb|anneal] [--cooling start_temp:alpha] <city file>

######sample city file is provided:
    city100.txt


read more about TSP at [wikipedia](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

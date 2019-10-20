## Tabu search algorithm for travelling salesman problem

Program includes two classes:
* datasets
* tabu search

Datasets used in experiments are avaliable [here](https://wwwproxy.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/STSP.html).

Usage of algorithm:

`TS = TabooSearch(data, name)`

`stats = TS(taboo_list_size=30, count_of_neighbours=30, mutation_ratio=0.5, epochs=200)`

This is an implementation oh heuristic described [here](https://en.wikipedia.org/wiki/Tabu_search)

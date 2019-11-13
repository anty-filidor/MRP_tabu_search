from datasets import Datasets
from taboo_search import TabooSearch

path = '/Users/michal/PycharmProjects/MRP/datasets/*.tsp'
data = Datasets(path)

# name = 'ali535'
# name = 'berlin11_modified'
# name = 'berlin52'
# name = 'fl417'
name = 'gr666'
# name = 'kroA100'
# name = 'kroA150'
# name = 'nrw1379'
# name = 'pr2392'

TS = TabooSearch(data, name)
stats = TS(taboo_list_size=30, count_of_neighbours=30, mutation_ratio=0.5, epochs=200)

for iterator, log in enumerate(stats.items()):
    print('EPOCH {}'.format(iterator))
    print('\t\tbest distance - {}'.format(log[0]))
    print('\t\tbest route - {}'.format(log[1]))
    print('\n')



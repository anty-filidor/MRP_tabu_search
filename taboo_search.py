import operator
import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt
from tqdm import tqdm


class TabooSearch:
    def __init__(self, datasets, name):
        self.datasets = datasets
        self.name = name

    def _generate_individual(self):
        return self.datasets.get_permutation(self.name)

    @staticmethod
    def _mutation(individual, ratio):
        individual_copy = list(individual)
        for gene_index in range(len(individual_copy)):
            if random.random() < ratio:
                swap_with = int(random.random() * len(individual))
                gene1 = individual_copy[gene_index]

                individual_copy[gene_index] = individual_copy[swap_with]
                individual_copy[swap_with] = gene1
        return individual_copy

    def _rank_population(self, population):
        fitness_results = {}
        for i in range(0, len(population)):
            fitness_results[i] = self.datasets.distance_permutation(self.name, population[i])
        ranked_population = np.array(sorted(fitness_results.items(), key=operator.itemgetter(1), reverse=False))
        # return dataframe with rows sorted by shortest distance and index of permutation
        return pd.DataFrame(ranked_population, columns=['index', 'fitness'])

    def __call__(self, taboo_list_size, count_of_neighbours, mutation_ratio, epochs):
        # initialise containers for best individual at all
        individual_best = self._generate_individual()
        individual_best_fitness = self._rank_population([individual_best]).iloc[0]['fitness']

        # initialise containers for individual from epoch which can become best individual at all
        individual_candidate = individual_best
        individual_candidate_fitness = individual_best_fitness

        #  initialise taboo list
        taboo_list = [individual_best]

        # initialise containers to plot experiment
        best_distances = [individual_best_fitness]
        best_routes = [individual_best]

        #  iterate to given epoch limit
        for epoch in tqdm(range(0, epochs)):

            # select neighbourhood of current individual
            neighbourhood = []
            while len(neighbourhood) < count_of_neighbours:
                neighbour = self._mutation(individual_candidate, mutation_ratio)
                if neighbour not in neighbourhood and neighbour not in taboo_list:
                    neighbourhood.append(neighbour)

            # rank neighbourhood
            ranked_neighbours = self._rank_population(neighbourhood)

            #  find the best candidate in current epoch
            if ranked_neighbours.iloc[0]['fitness'] < individual_candidate_fitness:
                individual_candidate = neighbourhood[int(ranked_neighbours.iloc[0]['index'])]
                individual_candidate_fitness = ranked_neighbours.iloc[0]['fitness']

            #  check if the best candidate is the best individual. if so, replace it
            if individual_candidate_fitness < individual_best_fitness:
                individual_best_fitness = individual_candidate_fitness
                individual_best = individual_candidate

            #  update taboo list
            taboo_list.append(individual_candidate)
            if len(taboo_list) > taboo_list_size:
                del taboo_list[0]

            #  update container to make plot
            best_distances.append(individual_best_fitness)
            best_routes.append(individual_best)

        #  plot figure
        plt.plot(best_distances)
        plt.ylabel('Distance')
        plt.xlabel('Epoch')
        plt.show()

        return dict(zip(best_distances, best_routes))

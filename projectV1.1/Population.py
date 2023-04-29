import Individual
import random


class Population:

    def __init__(self, populationSize, spatial_rel, object_list, lemma_dict):
        self.populationSize = populationSize
        self.population = []
        self.populationFitness = -1
        self.spatial_rel = spatial_rel
        self.object_list = object_list
        self.lemma_dict = lemma_dict
        for x in range(0, self.populationSize):
            self.population.append(Individual.Individual(
                self.spatial_rel, self.object_list, self.lemma_dict))

    def getIndividuals(self):
        return self.population

    def getFittest(self, offset):
        self.population.sort(key=lambda x: x.fitness, reverse=True)
        return self.population[offset]

    def setPopulationFitness(self, fitness):
        self.populationFitness = fitness

    def getPopulationFitness(self):
        return self.populationFitness

    def size(self):
        return len(self.population)

    def setIndividual(self, offset, individual):
        self.population[offset] = individual
        return self.population[offset]

    def getIndividual(self, offset):
        return self.population[offset]

    def shuffle(self):
        for i in range(len(self.population)-1, 0, -1):
            j = random.randint(0, i + 1)
            self.population[i], self.population[j] = self.population[j], self.population[i]

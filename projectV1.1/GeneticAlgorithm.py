import Population
import Individual
import random


class GeneticAlgorithm:
    def __init__(self, populationSize, mutationRate, crossoverRate, elitismCount, maxGeneration, spatial_rel, object_list, lemma_dict):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.crossoverRate = crossoverRate
        self.elitismCount = elitismCount
        self.maxGeneration = maxGeneration
        self.spatial_rel = spatial_rel
        self.object_list = object_list
        self.lemma_dict = lemma_dict

    def initPopulation(self):
        population = Population.Population(
            self.populationSize, self.spatial_rel, self.object_list, self.lemma_dict)
        return population

    def calcFitness(self, individual):
        individual.calc_fitness()
        return individual.getFitness()

    def evalPopulation(self, population):
        populationFitness = 0
        pop = population.getIndividuals()
        for individual in pop:
            populationFitness += self.calcFitness(individual)
        population.setPopulationFitness(populationFitness)

    def isTerminationConditionMet(self, population, generationNum):
        pop = population.getIndividuals()
        if generationNum >= self.maxGeneration:
            return True
        for individual in pop:
            if individual.getFitness() == 1:
                return True
        return False

    def selectParent(self, population):
        individuals = population.getIndividuals()
        populationFitness = population.getPopulationFitness()
        rouletteWheelPosition = random.random() * populationFitness
        spinWheel = 0
        for individual in individuals:
            spinWheel += individual.getFitness()
            if spinWheel >= rouletteWheelPosition:
                return individual
        return individuals[population.size()-1]

    def crossoverPopulation(self, population):
        population.getFittest(0)
        newPopulation = Population.Population(
            population.size(), self.spatial_rel, self.object_list, self.lemma_dict)
        for populationIndex in range(0, population.size()):
            parent1 = population.getIndividual(populationIndex)
            if self.crossoverRate > random.random() and populationIndex >= self.elitismCount:
                offspring = Individual.Individual(
                    self.spatial_rel, self.object_list, self.lemma_dict)
                parent2 = self.selectParent(population)
                for geneIndex in range(0, parent1.getChromosomeLength()):
                    cord1 = parent1.getGene(geneIndex)
                    cord2 = parent2.getGene(geneIndex)
                    cordx1 = cord1[0]
                    cordy1 = cord1[1]
                    cordz1 = cord1[2]
                    cordx2 = cord2[0]
                    cordy2 = cord2[1]
                    cordz2 = cord2[2]
                    if cordx1 > cordx2:
                        temp = cordx1
                        cordx1 = cordx2
                        cordx2 = temp
                    if cordy1 > cordy2:
                        temp = cordy1
                        cordy1 = cordy2
                        cordy2 = temp
                    if cordz1 > cordz2:
                        temp = cordz1
                        cordz1 = cordz2
                        cordz2 = temp
                    newGene = random.randrange(cordx1, cordx2+1, 1), random.randrange(
                        cordy1, cordy2+1, 1), random.randrange(cordz1, cordz2+1, 1)
                    offspring.setGene(geneIndex, newGene)
                newPopulation.setIndividual(populationIndex, offspring)
        else:
            newPopulation.setIndividual(populationIndex, parent1)
        return newPopulation

    def mutatePopulation(self, population):
        population.getFittest(0)
        newPopulation = Population.Population(
            population.size(), self.spatial_rel, self.object_list, self.lemma_dict)
        for populationIndex in range(0, population.size()):
            individual = population.getIndividual(populationIndex)
            for geneIndex in range(0, individual.getChromosomeLength()):
                if populationIndex >= self.elitismCount:
                    if self.mutationRate > random.random():
                        newGene = random.randrange(2, individual.max_x+1, 1), random.randrange(
                            2, individual.max_y+1, 1), random.randrange(1, individual.max_z+1, 1)
                        individual.setGene(geneIndex, newGene)
            newPopulation.setIndividual(populationIndex, individual)
        return newPopulation

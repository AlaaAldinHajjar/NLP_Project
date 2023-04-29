import random
import json
import math
json_file = open("sample_file.json", "r")
json_object = json.load(json_file)


class Individual:
    def __init__(self, spatial_rel, object_list, lemma_dict):
        self.spatial_rel = spatial_rel
        self.object_list = object_list
        self.lemma_dict = lemma_dict
        self.fitness = -1
        self.chromosome = []
        self.max_x = 1780
        self.max_y = 1010
        self.max_z = 50
        self.object_dict = {"": ""}
        self.createChromosome()

    def createChromosome(self):
        for x in range(0, len(self.object_list)):
            self.object_dict[self.object_list[x]] = x
            obj_cor = random.randrange(1, self.max_x+1, 1), random.randrange(
                1, self.max_y+1, 1), random.randrange(1, self.max_z+1, 1)
            self.chromosome.append(obj_cor)

    def calc_fitness(self):
        objects = json_object['objects']
        relative_distances = json_object['relative_distances']
        self.fitness = 0
        best_fitness = 0
        null = -1, -1
        for rel in self.spatial_rel:
            a_lemma = self.lemma_dict[rel[0]]
            b_lemma = self.lemma_dict[rel[1]]
            rel_dist = relative_distances[rel[2]]
            if rel_dist != '$' and rel[0] != null and rel[1] != null:
                best_fitness += rel_dist[6]
                a = objects[a_lemma]
                b = objects[b_lemma]
                a_c = self.chromosome[self.object_dict[rel[0]]]
                b_c = self.chromosome[self.object_dict[rel[1]]]
                x1 = a_c[0]-(a['margene'][0])*100
                y1 = a_c[1]-(a['margene'][1])*100
                x1b = a_c[0]+(a['margene'][0])*100
                y1b = a_c[1]+(a['margene'][1])*100
                x2 = b_c[0]-(b['margene'][0])*100
                y2 = b_c[1]-(b['margene'][1])*100
                x2b = b_c[0]+(b['margene'][0])*100
                y2b = b_c[1]+(b['margene'][1])*100
                dist_f, dist_out, dist_xy = self.dist_calc(
                    x1, y1, x1b, y1b, x2, y2, x2b, y2b)
                dist = 0
                if rel_dist[0] == '1':
                    dist = dist_f
                elif rel_dist[0] == '2':
                    dist = dist_out
                else:
                    dist = dist_xy
                bool_dist = False
                bool_x_to_x = False
                bool_y_to_y = False
                bool_z = False
                if dist >= rel_dist[1]*100 and dist <= rel_dist[2]*100:
                    bool_dist = True
                if rel_dist[3] == '0':
                    bool_x_to_x = True
                elif a_c[0] >= x2 and a_c[0] <= x2b:
                    bool_x_to_x = True
                if rel_dist[4] == '0':
                    bool_y_to_y = True
                elif rel_dist[4] == '1':
                    if a_c[1] > b_c[1]:
                        bool_y_to_y = True
                else:
                    if a_c[1] < b_c[1]:
                        bool_y_to_y = True
                if rel_dist[5] == '0':
                    bool_z = True
                elif rel_dist[5] == '+':
                    if a_c[2] > b_c[2]:
                        bool_z = True
                else:
                    if a_c[2] < b_c[2]:
                        bool_z = True
                if bool_dist and bool_x_to_x and bool_y_to_y and bool_z:
                    self.fitness += rel_dist[6]
        for obj in self.object_list:
            obj_lemma = self.lemma_dict[obj]
            obj_class = objects[obj_lemma]['class']
            obj_margene = objects[obj_lemma]['margene']
            obj_c = self.chromosome[self.object_dict[obj]]
            x1 = obj_c[0]-(obj_margene[0])*100
            y1 = obj_c[1]-(obj_margene[1])*100
            x1b = obj_c[0]+(obj_margene[0])*100
            y1b = obj_c[1]+(obj_margene[1])*100
            z = obj_c[2]
            best_fitness += 2
            if x1 >= obj_class[0]*100 and x1 <= obj_class[1]*100 and y1 >= obj_class[2]*100 and y1 <= obj_class[3]*100 and x1b >= obj_class[0]*100 and x1b <= obj_class[1]*100 and y1b >= obj_class[2]*100 and y1b <= obj_class[3]*100 and z >= obj_class[4] and z <= obj_class[5]:
                self.fitness += 2
        if best_fitness != 0:
            self.fitness = self.fitness/best_fitness
        else:
            self.fitness = 1

    def dist_calc(self, x1, y1, x1b, y1b, x2, y2, x2b, y2b):
        xc1 = (x1+x1b)/2
        yc1 = (y1+y1b)/2
        xc2 = (x2+x2b)/2
        yc2 = (y2+y2b)/2
        interP1x = 0
        interP2x = 0
        interP1y = 0
        interP2y = 0
        dist_iner1 = 0
        dist_iner2 = 0
        dist_f = 0
        dist_out = -1
        if xc1-xc2 == 0:
            dist_xy = abs(yc1-yc2)
            dist_iner1 = abs(yc1-y1)
            dist_iner2 = abs(yc2-y2)
        elif yc1-yc2 == 0:
            dist_xy = abs(xc1-xc2)
            dist_iner1 = abs(xc1-x1)
            dist_iner2 = abs(xc2-x2)
        else:
            mc = (yc1-yc2)/(xc1-xc2)
            mr1 = (y1-y1b)/(x1-x1b)
            mr2 = (y2-y2b)/(x2-x2b)
            if abs(mc) > abs(mr1):
                interP1x = (y1-yc1)/mc+xc1
                interP1y = y1
            else:
                interP1y = (x1-xc1)*mc+yc1
                interP1x = x1
            if abs(mc) > abs(mr2):
                interP2x = (y2-yc1)/mc+xc1
                interP2y = y2
            else:
                interP2y = (x2-xc1)*mc+yc1
                interP2x = x2
            dist_xy = math.sqrt(math.pow((xc1-xc2), 2)+math.pow((yc1-yc2), 2))
            dist_iner1 = math.sqrt(
                math.pow((interP1x-xc1), 2)+math.pow((interP1y-yc1), 2))
            dist_iner2 = math.sqrt(
                math.pow((interP2x-xc2), 2)+math.pow((interP2y-yc2), 2))
        dist_f = dist_xy-dist_iner1-dist_iner2
        if dist_f > 0:
            dist_out = dist_f
        else:
            dist_f *= -1
        return dist_f, dist_out, dist_xy

    def getChromosome(self):
        return self.chromosome

    def getChromosomeLength(self):
        return len(self.chromosome)

    def setGene(self, offset, gene):
        self.chromosome[offset] = gene

    def getGene(self, offset):
        return self.chromosome[offset]

    def setFitness(self, fitness):
        self.fitness = fitness

    def getFitness(self):
        return self.fitness

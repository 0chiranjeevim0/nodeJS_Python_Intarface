
import numpy as np
from numpy import random



POPULATION_SIZE = 200

SUBJECTS = [['DP-2:NAC:5', 'GP-2:RUK:5', 'PS-1:SRS:5', 'TAM-1:LANG-1:6', 'ENG-1:LANG-2:6', 'LAB:EP-1:VAO:3'], ['AP-1:KRT:5', 'RM:NAC:5', 'LAP:SRS:5', 'TAM-2:LANG-1:5', 'LANG-2:LANG-2:5', 'LAB:EP-3:KAN:3', 'EDC:IS:EDC:2'], ['FMCS:RUK:5', 'FC:ANU:5', 'FHP:KAA:5', 'PEC:KAN:5', 'RP:VAO:5', 'LAB:EP-5:KRT:5'], ['OB:ANU:5', 'CP:RUK:5', 'PTD:KAA:5', 'BM:VAO:5', 'LAB:PA:SRS:5', 'EDC:CS:EDC:5'], ['OB-2:NAC:5', 'MCB:KAN:5', 'CS:KRT:5', 'HP:ANU:4', 'LAB:CA:KAA:3', 'EDC:PS:EDC:4', 'EDC:HRM:EDC:4']]


class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome

        self.fitness = self.cal_fitness()
        

    


    @classmethod
    def create_gnome(self):
        sub=SUBJECTS
        j=1
    
        d={}
        for i in sub:
            l=np.array([j for j in i for _ in range(int(j[-1]))])
            np.random.shuffle(l)
            k=l.reshape(6,5)

            d[j]=np.sort(k)
            j+=1
    
    
    
        return d

    def cal_fitness(self):
        fit=0

        for i in range(1,6):
            lst=[]
            for j in self.chromosome[i]:
                k=[l.split(':')[0]for l in j]
                a=sum([+1 for z in k if z=='LAB'])
                if a!=0:lst.append(a)
            if i !=4 and sorted(lst)!=[1,2]:
                fit+=1
            elif i == 4 and sorted(lst)!=[1,2,2]:
                fit+=1

        return fit

    def mate(self,par2):
        l={}
        for i in range(1,6):
            lst=[]
            for j,p in zip(self.chromosome[i],par2.chromosome[i]):
                prob=random.random()
                if prob<0.50:
                    lst.append(j)
                elif prob<1.0:
                    lst.append(p)
                else:
                    # lst.append(self.mutated_genes(i))
                    print('mooooooooooooooooooooooooooooooooooooooooooooooo')
            l[i]=np.array(lst)
        
        return Individual(l)





def main():
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))


    while not found:

      # sort the population in increasing order of fitness score
        population = sorted(population, key = lambda x:x.fitness)
        if population[0].fitness <= 0:
            found = True
            # break
            # break
            # Otherwise generate new offsprings for new generation
        new_generation = []

      # Perform Elitism, that mean 10% of fittest population
      # goes to the next generation
        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])

        # From 50% of fittest population, Individuals
      # will mate to produce offspring
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
        population = new_generation


        generation += 1

    return population[0].chromosome


def invoke():
    d = main()
    return d
    

        
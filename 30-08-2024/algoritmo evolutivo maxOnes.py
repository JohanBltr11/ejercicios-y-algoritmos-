import random

def maxOnes(solution:list) -> int:
    return solution.count(1)

def createPopulation(popSize:int, solSize:int):
    population=[]
    for i in range(popSize):
        temp=[random.randint(0,1) for i in range(solSize)]
        population.append(temp)
    return population

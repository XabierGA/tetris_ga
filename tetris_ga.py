import numpy as np

class genome():

	def __init__(self , len):

		self.genomes = np.zeros(len)

	def sort(self):


class ga_solver():


	def __init__(self, popsize):

		self.popSize = popsize
		self.currentgenome = 0
		self.gen = genome()

	def create_initial_population(self):

		genomes = []
		for i in range(self.popSize):
			genome = {"id":i*np.random.rand(),"rowsCleared":np.random.rand()-0.5,"}
			genomes.append(genome)

	def evaluatenextgenome(self):

		self.currentgenome += 1
		if (self.currentgenome == self.genome_length):


	def evolve(self):

		self.total_fitness = np.sum(genomes.fitness)


	def make_child(self  , mum , dad):

		child = {"id":i*np.random.rand(),"rowsCleared":np.random.choice(mum.rowsCleared,dad.rowsCleared)}


	def evolve(self, ):

		self.fittest = genome.fittest()
		self.second_fittest = genome.second_fittest()


	def mutation(self , ):

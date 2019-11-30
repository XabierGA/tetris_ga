import numpy as np
from tetris import BOARD_DATA, Shape

ROTATIONS = 4
class Genome():

	def __init__(self , ID):
		
		self.id = ID
		self.rows_cleared = np.random.rand() - 0.5
		self.weighted_height = np.random.rand() - 0.5
		self.cumulative_height = np.random.rand() - 0.5
		self.relative_height = np.random.rand() - 0.5
		self.holes = np.random.rand() - 0.5 
		self.roughness = np.random.rand() - 0.5
		self.fitness = -1
		self.moves_taken = 0



class ga_solver():

	def __init__(self, pop_size , mut_rate):
		
		self.pop_size = pop_size
		self.current_genome = 0
		self.id_index = 0
		self.generation = 0
		self.gen = genome()
		self.mut_rate = mut_rate
		self.elites = []
		BOARD_DATA.width 
	def create_initial_population(self):

		self.genomes = [Genome(self.id_index) for x in range(self.pop_size)]

	def evaluatenextgenome(self):

		self.current_genome += 1
		if (self.current_genome == self.genome_length):
				evolve()
        

		
	def make_child(self, genomes):
		mum , dad = np.random.choice(genomes , 2)
		child = Genome()
		child = set_random_att(child , mum ,dad)
		child = mutate(child)

		return child 

	def set_random_att(self, child, mum, dad):
		child.rows_cleared = np.random.choice(mum.rows_cleared , dad.rows_cleared)
		child.weighted_height = np.random.choice(mum.weighted_height , dad.weighted_height)
		child.cumulative_height = np.random.choice(mum.cumulative_height , dad.cumulative_height)
		child.relative_height = np.random.choice(mum.relative_height , dad.relative_height)
		child.holes = np.random.choice(mum.holes , dad.holes)
		child.roughness = np.random.choice(mum.roughness , dad.roughness)
		child.fitness = -1

		return child
	
	def mutate(self , child):
		if (np.random.rand() < self.mut_rate):
			child.rows_cleared += np.random.rand() * self.mut_rate * 2 - self.mut_rate

		if (np.random.rand() < self.mut_rate):
			child.weighted_height += np.random.rand() * self.mut_rate * 2 - self.mut_rate

		if (np.random.rand() < self.mut_rate):
			child.cumulative_height += np.random.rand() * self.mut_rate * 2 - self.mut_rate

		if (np.random.rand() < self.mut_rate):
			child.relative_height += np.random.rand() * self.mut_rate * 2 - self.mut_rate

		if (np.random.rand() < self.mut_rate):
			child.holes += np.random.rand() * self.mut_rate * 2 - self.mut_rate
		
		if (np.random.rand() < self.mut_rate):
			child.roughness += np.random.rand() * self.mut_rate * 2 - self.mut_rate

		return child

	def evolve(self):

		self.generation += 1
		self.genomes = self.genomes.sort(key=lambda x: x.fitness,reverse=True)
		self.elites.append(self.genomes[0])

		self.genomes = self.genomes[:int(len(self.genomes)/2)]
		self.total_fitness = np.sum([x.fitness for x in self.genomes])

		self.children = [make_child(self.genomes) for x in range(len(self.pop_size))]
		
		self.genomes = self.children


    def update(self):

        if (self.current_genome != -1):

            results = move_down()

            if (!results.moved):
                
                if results.lose:

                    self.genomes[self.current_genome].fitness = self.score

                    evaluate_next_genome()

                else:

                    make_next_move():
            else:

                move_down()

    def get_possible_moves(self):

        last_state = get_state()
        iterations = 0
        possible_moves = []
        for rot in range(ROTATIONS):

            for t in range(-5,5):
                iterations += 1 
                load_state(last_state)
                for j in range(rot):
                    rotate_shape()
                if t<0:
                    for k in range(int(np.abs(t))):
                        move_left()
                elif t>0:
                    for k in range(t):
                        move_right()
                if moved_:

                    move_down = move_down()
                    while move_down.moved():
                        move_down_results = move_down()
                
                algo = {"rows_cleared":move_down_results.rows_cleared , "weighted_height":(get_height())**(1.5),"cumulative_height":get_cumulative_height(),"relative_height":get_relative_height() , "holes":get_holes() , "roughness":get_roughness()}
                rating = 0
     			rating += algorithm["rows_cleared"] * self.genomes[self.current_genome].rows_cleared
                rating += algorithm["weighted_height"] * self.genomes[self.current_genome].weighted_height
                rating += algorithm["cumulative_height"] * self.genomes[self.current_genome].cumulative_height
                rating += algorithm["relative_height"] * self.genomes[self.current_genome].relative_height
                rating += algorithm["holes"] * self.genomes[self.current_genome].holes
                rating += algorithm["roughness"] * self.genomes[self.current_genome].roughness
                if move_down_results.lose():
                    rating -= 500
                
                possible_moves.append({"rotations":rot , "translations":t , "rating":rating , "algorithm":algo})

        load_state(last_state)

        return possible_moves


    def next_move(self):

        self.moves_taken += 1 
        if (self.moves_taken > self.move_limit):
            self.genomes[self.current_genome].fitness = self.score
            evaluate_next_genome()

        else:
            old_draw = self.old_draw
            possible_moves = get_possible_moves()
            last_state = get_state()
            next_shape()

            next_move = [get_highest_rated(get_all_possible_moves) for x in range(len(possible_moves))]

            possible_moves = [possible_moves[x].rating += next_move.rating for x in range(len(possible_moves))]

            load_state(last_state)
        
            move = get_highest_rated(possible_moves)

            for rot in move.rotations:
                rotate_shape()

            if move.translation<0:
                for trans in move.translation:
                    move_left()

            elif move.translation>0:
                for trans in move.translation:
                    move_right()

        draw = old_draw
        output()
        update_score()

    def move_down(self):

        resul

    def get_highest_rated(self):

        max_rating = -10000000
        max_move = -1 
        ties = []
        for i,move in enumerate(moves):

            if move.rating >max_rating:
                max_move = i
                ties = [i]
            elif move.rating == max_rating:
                ties.append(i)

        move = moves[ties[0]]
        move.algorithm.ties = len(ties)
        return move 
        
	def get_height(self):
		
		remove_new_shape()

		max_height = np.max(np.count_nonzero(X,axis=0))

		apply_new_shape()

		return max_height

	def get_relative_height(self):

		remove_new_shape()

		relative_height = np.max(np.count_nonzero(X,axis=0)) - np.min(np.count_nonzero(X,axis=0))

		apply_new_shape()

		return relative_height

	def get_cumulative_height(self):

		remove_new_shape()

		cumulative_height = np.sum(np.count_nonzero(X , axis = 0))

		apply_new_shape()

		return cumulative_height

    def get_holes(self):

        remove_new_shape()

        holes = BOARD_DATA.width*BOARD_DATA.height - np.sum(np.count_nonzero(X , axis = 0))

        apply_new_shape()
	
        return holes 

    def get_roughness(self):

        remove_new_shape()

        roughness = np.diff(np.count_nonzero(X , axis = 0)).sum()

        apply_new_shape()

        return roughness 


class Move(object):

    def __init__(self):

        self.lost = False
        self.moved = True
        self.rows_cleared = 0
    def move_down(self):

        remove_shape()
        self.current_shape 
    def move_left(self):




from tetris_model import BOARD_DATA, Shape
import math
from datetime import datetime
import numpy as np


class TetrisAI(object):

    def nextMove(self):
        t1 = datetime.now()
        if BOARD_DATA.currentShape == Shape.shapeNone:
            return None

        currentDirection = BOARD_DATA.currentDirection
        currentY = BOARD_DATA.currentY
        _, _, minY, _ = BOARD_DATA.nextShape.getBoundingOffsets(0)
        nextY = -minY

        # print("=======")
        strategy = None
        if BOARD_DATA.currentShape.shape in (Shape.shapeI, Shape.shapeZ, Shape.shapeS):
            d0Range = (0, 1)
        elif BOARD_DATA.currentShape.shape == Shape.shapeO:
            d0Range = (0,)
        else:
            d0Range = (0, 1, 2, 3)

        if BOARD_DATA.nextShape.shape in (Shape.shapeI, Shape.shapeZ, Shape.shapeS):
            d1Range = (0, 1)
        elif BOARD_DATA.nextShape.shape == Shape.shapeO:
            d1Range = (0,)
        else:
            d1Range = (0, 1, 2, 3)

        for d0 in d0Range:
            minX, maxX, _, _ = BOARD_DATA.currentShape.getBoundingOffsets(d0)
            for x0 in range(-minX, BOARD_DATA.width - maxX):
                board = self.calcStep1Board(d0, x0)
                for d1 in d1Range:
                    minX, maxX, _, _ = BOARD_DATA.nextShape.getBoundingOffsets(d1)
                    dropDist = self.calcNextDropDist(board, d1, range(-minX, BOARD_DATA.width - maxX))
                    for x1 in range(-minX, BOARD_DATA.width - maxX):
                        score = self.calculateScore(np.copy(board), d1, x1, dropDist)
                        if not strategy or strategy[2] < score:
                            strategy = (d0, x0, score)
        print("===", datetime.now() - t1)
        return strategy

    def calcNextDropDist(self, data, d0, xRange):
        res = {}
        for x0 in xRange:
            if x0 not in res:
                res[x0] = BOARD_DATA.height - 1
            for x, y in BOARD_DATA.nextShape.getCoords(d0, x0, 0):
                yy = 0
                while yy + y < BOARD_DATA.height and (yy + y < 0 or data[(y + yy), x] == Shape.shapeNone):
                    yy += 1
                yy -= 1
                if yy < res[x0]:
                    res[x0] = yy
        return res

    def calcStep1Board(self, d0, x0):
        board = np.array(BOARD_DATA.getData()).reshape((BOARD_DATA.height, BOARD_DATA.width))
        self.dropDown(board, BOARD_DATA.currentShape, d0, x0)
        return board

    def dropDown(self, data, shape, direction, x0):
        dy = BOARD_DATA.height - 1
        for x, y in shape.getCoords(direction, x0, 0):
            yy = 0
            while yy + y < BOARD_DATA.height and (yy + y < 0 or data[(y + yy), x] == Shape.shapeNone):
                yy += 1
            yy -= 1
            if yy < dy:
                dy = yy
        # print("dropDown: shape {0}, direction {1}, x0 {2}, dy {3}".format(shape.shape, direction, x0, dy))
        self.dropDownByDist(data, shape, direction, x0, dy)

    def dropDownByDist(self, data, shape, direction, x0, dist):
        for x, y in shape.getCoords(direction, x0, 0):
            data[y + dist, x] = shape.shape

    def calculateScore(self, step1Board, d1, x1, dropDist):
        # print("calculateScore")
        t1 = datetime.now()
        width = BOARD_DATA.width
        height = BOARD_DATA.height

        self.dropDownByDist(step1Board, BOARD_DATA.nextShape, d1, x1, dropDist[x1])
        # print(datetime.now() - t1)

        # Term 1: lines to be removed
        fullLines, nearFullLines = 0, 0
        roofY = [0] * width
        holeCandidates = [0] * width
        holeConfirm = [0] * width
        vHoles, vBlocks = 0, 0
        for y in range(height - 1, -1, -1):
            hasHole = False
            hasBlock = False
            for x in range(width):
                if step1Board[y, x] == Shape.shapeNone:
                    hasHole = True
                    holeCandidates[x] += 1
                else:
                    hasBlock = True
                    roofY[x] = height - y
                    if holeCandidates[x] > 0:
                        holeConfirm[x] += holeCandidates[x]
                        holeCandidates[x] = 0
                    if holeConfirm[x] > 0:
                        vBlocks += 1
            if not hasBlock:
                break
            if not hasHole and hasBlock:
                fullLines += 1
        vHoles = sum([x ** .7 for x in holeConfirm])
        maxHeight = max(roofY) - fullLines
        # print(datetime.now() - t1)

        roofDy = [roofY[i] - roofY[i+1] for i in range(len(roofY) - 1)]

        if len(roofY) <= 0:
            stdY = 0
        else:
            stdY = math.sqrt(sum([y ** 2 for y in roofY]) / len(roofY) - (sum(roofY) / len(roofY)) ** 2)
        if len(roofDy) <= 0:
            stdDY = 0
        else:
            stdDY = math.sqrt(sum([y ** 2 for y in roofDy]) / len(roofDy) - (sum(roofDy) / len(roofDy)) ** 2)

        absDy = sum([abs(x) for x in roofDy])
        maxDy = max(roofY) - min(roofY)
        # print(datetime.now() - t1)

        score = fullLines * 1.8 - vHoles * 1.0 - vBlocks * 0.5 - maxHeight ** 1.5 * 0.02 \
            - stdY * 0.0 - stdDY * 0.01 - absDy * 0.2 - maxDy * 0.3
        # print(score, fullLines, vHoles, vBlocks, maxHeight, stdY, stdDY, absDy, roofY, d0, x0, d1, x1)
        return score


TETRIS_AI = TetrisAI()
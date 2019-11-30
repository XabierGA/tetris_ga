import random

class Shape(object):
    shape_none = 0
    shape_I = 1
    shape_L = 2
    shape_J = 3
    shape_T = 4
    shape_O = 5
    shape_S = 6
    shape_Z = 7

    shape_coord = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((0, -1), (0, 0), (0, 1), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (-1, 1)),
        ((0, -1), (0, 0), (0, 1), (1, 0)),
        ((0, 0), (0, -1), (1, 0), (1, -1)),
        ((0, 0), (0, -1), (-1, 0), (1, -1)),
        ((0, 0), (0, -1), (1, 0), (-1, -1))
    )

    def __init__(self, shape=0):
        self.shape = shape

    def get_rotated_offsets(self, direction):
        tmp_coords = Shape.shape_coord[self.shape]
        if direction == 0 or self.shape == Shape.shape_O:
            return ((x, y) for x, y in tmp_coords)

        if direction == 1:
            return ((-y, x) for x, y in tmp_coords)

        if direction == 2:
            if self.shape in (Shape.shape_I, shape.shape_Z, Shape.shape_S):
                return ((x, y) for x, y in tmp_coords)
            else:
                return ((-x, -y) for x, y in tmp_coords)

        if direction == 3:
            if self.shape in (Shape.shape_I, Shape.shape_Z, Shape.shape_S):
                return ((-y, x) for x, y in tmp_coords)
            else:
                return ((y, -x) for x, y in tmp_coords)

    def get_coords(self, direction, x, y):
        return ((x + xx, y + yy) for xx, yy in self.get_rotated_offsets(direction))

    def getBoundingOffsets(self, direction):
        tmp_coords = self.get_rotated_offsets(direction)
        minX, maxX, minY, maxY = 0, 0, 0, 0
        for x, y in tmp_coords:
            if minX > x:
                minX = x
            if maxX < x:
                maxX = x
            if minY > y:
                minY = y
            if maxY < y:
                maxY = y
        return (minX, maxX, minY, maxY)


class BoardData(object):
    width = 10
    height = 22

    def __init__(self):
        self.backBoard = [0] * BoardData.width * BoardData.height

        self.current_X = -1
        self.current_Y = -1
        self.current_direction = 0
        self.current_shape = Shape()
        self.next_shape = Shape(random.randint(1, 7))

        self.shape_stat = [0] * 8

    def getData(self):
        return self.back_board[:]

    def getValue(self, x, y):
        return self.back_board[x + y * BoardData.width]

    def getCurrentShapeCoord(self):
        return self.current_shape.get_coords(self.current_direction, self.current_X, self.current_Y)

    def create_new_piece(self):
        minX, maxX, minY, maxY = self.next_shape.getBoundingOffsets(0)
        result = False
        if self.try_move_current(0, 5, -minY):
            self.current_X = 5
            self.currentY = -minY
            self.current_direction = 0
            self.current_shape = self.next_shape
            self.next_shape = Shape(random.randint(1, 7))
            result = True
        else:
            self.current_shape = Shape()
            self.current_X = -1
            self.current_Y = -1
            self.current_direction = 0
            result = False
        self.shape_stat[self.current_shape.shape] += 1
        return result

    def try_move_current(self, direction, x, y):
        return self.try_move(self.current_shape, direction, x, y)

    def try_move(self, shape, direction, x, y):
        for x, y in shape.get_coords(direction, x, y):
            if x >= BoardData.width or x < 0 or y >= BoardData.height or y < 0:
                return False
            if self.back_board[x + y * BoardData.width] > 0:
                return False
        return True

    def moveDown(self):
        lines = 0
        if self.try_move_current(self.current_direction, self.current_X, self.current_Y + 1):
            self.current_Y += 1
        else:
            self.merge_piece()
            lines = self.remove_full_lines()
            self.create_new_piece()
        return lines

    def dropDown(self):
        while self.try_move_current(self.current_direction, self.current_X, self.current_Y + 1):
            self.current_Y += 1
        self.merge_piece()
        lines = self.remove_full_lines()
        self.create_new_piece()
        return lines

    def moveLeft(self):
        if self.try_move_current(self.current_direction, self.current_X - 1, self.current_Y):
            self.current_X -= 1

    def moveRight(self):
        if self.try_move_current(self.current_direction, self.current_X + 1, self.current_Y):
            self.current_X += 1

    def rotateRight(self):
        if self.try_move_current((self.current_direction + 1) % 4, self.current_X, self.current_Y):
            self.current_direction += 1
            self.current_direction %= 4

    def rotateLeft(self):
        if self.try_move_current((self.current_direction - 1) % 4, self.current_X, self.current_Y):
            self.current_direction -= 1
            self.current_direction %= 4

    def remove_full_lines(self):
        new_back_board = [0] * BoardData.width * BoardData.height
        newY = BoardData.height - 1
        lines = 0
        for y in range(BoardData.height - 1, -1, -1):
            blockCount = sum([1 if self.back_board[x + y * BoardData.width] > 0 else 0 for x in range(BoardData.width)])
            if blockCount < BoardData.width:
                for x in range(BoardData.width):
                    new_back_board[x + newY * BoardData.width] = self.back_board[x + y * BoardData.width]
                newY -= 1
            else:
                lines += 1
        if lines > 0:
            self.back_board = new_back_board
        return lines

    def merge_piece(self):
        for x, y in self.current_shape.get_coords(self.current_direction, self.current_X, self.current_Y):
            self.back_board[x + y * BoardData.width] = self.current_shape.shape

        self.current_X = -1
        self.current_Y = -1
        self.current_direction = 0
        self.current_shape = Shape()

    def clear(self):
        self.current_X = -1
        self.current_Y = -1
        self.current_direction = 0
        self.current_shape = Shape()
        self.back_board = [0] * BoardData.width * BoardData.height


BOARD_DATA = BoardData()
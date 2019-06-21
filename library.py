# library for game module
# Aadil Islam
# June 20, 2019

from cs1lib import *

# holds information specific to a specific cell
class Cell:
    # constructor
    def __init__(self, size):
        self.size = size
        self.isAlive = False

    # changes cell from alive->dead OR dead->alive
    def toggleState(self):
        self.isAlive = not self.isAlive

    # display cell to user
    def draw(self, x, y):
        set_fill_color(1,1,1) if self.isAlive else set_fill_color(0,0,0)
        draw_rectangle(x, y, self.size, self.size)

# holds array of cell objects
class Grid:
    # constructor
    def __init__(self, numCols, numRows, cellSize):
        self.numCols = numCols
        self.numRows = numRows
        self.cellSize = cellSize  
        self.board = [[Cell(cellSize) for i in range(numCols)] for j in range(numRows)]

    # toggle selected cell
    def handlePress(self, mx, my):
        row = int(my // self.cellSize)
        col = int(mx // self.cellSize)
        self.board[row][col].toggleState()

    # simulate one step in unit time in world
    def step(self):
        cellsToToggle = []  # to store locations of cells that must change state
        # iterate through each cell in grid
        for row in range(self.numRows):
            for col in range(self.numCols):
                # counter for number of live, surrounding cells
                aliveNeighbors = 0
                cell = self.board[row][col]
                # iterate through each neighbor of current cell
                for delta1 in range(-1, 2, 1):
                    for delta2 in range(-1, 2, 1):
                        if not (delta1 == 0 and delta2 == 0) \
                            and (row+delta1) >= 0 and (row+delta1) < self.numRows \
                            and (col+delta2) >= 0 and (col+delta2) < self.numCols:
                            # increment counter if living cell found
                            if self.board[row+delta1][col+delta2].isAlive:
                                aliveNeighbors += 1
                # save locations of cells that must change state
                if cell.isAlive and aliveNeighbors < 2:
                    # death by underpopulation
                    cellsToToggle.append((row, col))
                elif cell.isAlive and aliveNeighbors > 3:
                    # death by overpopulation
                    cellsToToggle.append((row, col))
                elif not cell.isAlive and aliveNeighbors == 3:
                    # life by reproduction
                    cellsToToggle.append((row, col))
        # change state of identified cells
        for row, col in cellsToToggle:
            self.board[row][col].toggleState()
    
    # kill all cells in grid
    def reset(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                self.board[row][col].aliveNeighbors = 0
                self.board[row][col].isAlive = False

    # display grid to user
    def draw(self):
        set_stroke_color(0.3, 0.3, 0.3) # gray gridlines
        for row in range(self.numRows):
            for col in range(self.numCols):
                self.board[row][col].draw(col*self.cellSize, row*self.cellSize)
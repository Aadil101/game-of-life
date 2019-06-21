# GUI for Conway's Game of Life
# Aadil Islam
# June 21, 2019

from cs1lib import *
from library import Grid

# constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CELL_SIZE = 20
refresh = True  # initializes display prior to game starting
gameStart = False   # indicates game has begun (simulation may not have)
simulationStart = False   # indicates simulation has started

# structure containing all cells in game
grid = Grid(int(WINDOW_WIDTH/CELL_SIZE), int(WINDOW_HEIGHT/CELL_SIZE), int(CELL_SIZE))

# handle mouse press so user can select living cells
def mouse_press(mx, my):
    if gameStart and not simulationStart:
        grid.handlePress(mx, my)

# handle key press during game
def key_press(key):
    global gameStart, simulationStart
    if key == " ":
        # user wants to leave prompt screen
        if not gameStart:
            gameStart = True
            print("Select living cells...")
        # user wants to begin simulation
        elif not simulationStart:
            simulationStart = True
            print("Simulation begins...")
        # user wants to replay game
        else:
            grid.reset()
            simulationStart = False
            print("Restarting game. Select living cells...")
    elif key == "q":
        print("Quitting game.")
        cs1_quit()

# method to be passed into graphics loop
def main():
    global refresh
    # show prompt screen
    if refresh and not gameStart:
        set_clear_color(0.9, 0.9, 0.9)  # gray background
        clear()
        set_stroke_color(0, 0, 0)   # black stroke color
        draw_text("Click on a cell to make it ALIVE", WINDOW_WIDTH//2 - 185, WINDOW_HEIGHT//2 - 50)
        draw_text("WHITE cells are ALIVE / BLACK cells are DEAD", WINDOW_WIDTH//2 - 185, WINDOW_HEIGHT//2 - 30)
        draw_text("Press SPACE to leave prompt / begin simulation / restart game", WINDOW_WIDTH//2 - 185, WINDOW_HEIGHT//2 -10)
        draw_text("Press 'q' anytime to quit", WINDOW_WIDTH//2 - 185, WINDOW_HEIGHT//2 + 10)
        draw_text("Enjoy! :)", WINDOW_WIDTH//2 - 185, WINDOW_HEIGHT//2 + 30)
        refresh = False
    # show cell-selection screen
    elif refresh:
        set_clear_color(0, 0, 0)    # black background
        clear()
        refresh = False
    # during game
    elif gameStart:
        # update grid during each step of simulation
        if simulationStart:
            grid.step()
        # redraw grid
        grid.draw()

start_graphics(main, framerate=10, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=mouse_press, key_press=key_press)
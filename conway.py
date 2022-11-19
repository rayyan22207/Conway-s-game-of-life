#conway's Game of Life
import random, time, copy
width = 60
height = 20
# create a list of list for the cells:
nextCells = []
for x in range(width):
    column = [] # create a new column
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#') # add a living cell
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column) # nextCells is a list of column lists.
while True: # main program loop
    print('\n\n\n\n\n') # separate each step with newlines
    currentCells = copy.deepcopy(nextCells)
    # print currentCells on the screen:
    for y in range(height):
        print(currentCells[x][y], end='') #print the # or space
    print() #print a newline at the end of the row
    # calculate the next  step's cells based on current step's cells:
    for x in range(width):
        for y in range(height):
            # get neighboring coordinates:
            # '% width' ensures leftCoord is always between 0 and width - 1
            leftCoord = (x - 1) % width
            rigthCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height
            #count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # top-left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # top neighbor is alive
            if currentCells[rigthCoord][aboveCoord] == '#':
                numNeighbors += 1 # top-right neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rigthCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rigthCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.
                
                # set cell based on Conway's Game of Life rules:
                if currentCells[x][y] == '#' and (numNeighbors == 2 or
    numNeighbors == 3):
                    # living cells with 2 or 3 neighbors stay alive:
                    nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.
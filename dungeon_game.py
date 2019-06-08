import random



# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw the player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),]

monster = None
door = None
player = None


def get_locations(arg):
    arg = random.randint(0,4), random.randint(0,4)
    return arg


def move_player():
    # get player's location
    # if move == LEFT, x-1
    # if move == RIGHT, x+1
    # if move == UP, y-1
    # if move == DOWN, y+1
    return player

def get_moves(player):
    moves = {"LEFT", "RIGHT", "UP", "DOWN"}
    # if player's y == 0, they can't move up
    if player[1] == 0:
        return moves - {"UP"}
    # if player's y == 4, they can't move down
    if player[1] == 4:
        return moves - {"DOWN"}
    # if player's x == 0, they can't move left
    if player[0] == 0:
        return moves - {"LEFT"}
    # if player's x == 4, they can't move right
    if player[0] == 4:
        return moves - {"RIGHT"}
    else:
        return moves 





while True:
    print("Welcome to the dungeon!")
    player = get_locations(player)
    print("You're currently in room {}".format(player))
    moves = get_moves(player)
    print("You can move {}".format(moves)) # fill with available moves
    print(player[1])
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == "QUIT":
        break

    # good move? change players position
    # bad move? Don't change anything
    # On the door? They win!
    # On the monster? They lose!
    # Otherwise, loop back around

    

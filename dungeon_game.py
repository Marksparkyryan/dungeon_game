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
move = None


def get_locations(CELLS, arg):
    taken = [] 
    not_taken = CELLS 
    location = random.choice(not_taken)
    not_taken.remove(location)
    taken.append(location)
    arg = location
    return arg

def check_move(move, moves, player):
    while True:
        move = input("> ")
        move = move.upper()
        try:
            if move == "QUIT":
                exit()
            if move in moves:
                return move
                break
            else:
                raise ValueError("Invalid move! Please try again.")               
        except ValueError as err:
            print("Uh oh! {}".format(err))
            continue



def move_player(player, move):
    # get player's location
    # if move == LEFT, x-1
    if move == "LEFT":
        player_x = player[0] - 1
        player = player_x, player[1]
        print(player)
        return player    
    # if move == RIGHT, x+1
    if move == "RIGHT":
        player_x = player[0] + 1
        player = player_x, player[1]
        print(player)
        return player 
    # if move == UP, y-1
    if move == "UP":
        player_y = player[1] - 1
        player = player[0], player_y
        print(player)
        return player 
    # if move == DOWN, y+1
    if move == "DOWN":
        player_y = player[1] + 1
        player = player[0], player_y
        print(player)
        return player 
    

def get_moves(player):
    moves = {"LEFT", "RIGHT", "UP", "DOWN"}
    # if player's y == 0, they can't move up
    if player[1] <= 0:
        moves = moves - {"UP"}
    # if player's y == 4, they can't move down
    if player[1] >= 4:
        moves = moves - {"DOWN"}
    # if player's x == 0, they can't move left
    if player[0] <= 0:
        moves = moves - {"LEFT"}
    # if player's x == 4, they can't move right
    if player[0] >= 4:
        moves = moves - {"RIGHT"}
    return moves





player = get_locations(CELLS, player)
door = get_locations(CELLS, door)
monster = get_locations(CELLS, monster)

while True:
    print(player)
    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player))
    moves = get_moves(player)
    print("You can move {}".format(moves)) # fill with available moves
    print("Enter QUIT to quit")

    move = check_move(move, moves, player)


    player = move_player(player, move)
    continue


    # good move? change players position
    # bad move? Don't change anything
    # bad move? Don't change anything
    # On the door? They win!
    # On the monster? They lose!
    # Otherwise, loop back around
    




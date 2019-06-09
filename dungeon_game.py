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
    if move == "LEFT":
        player_x = player[0] - 1
        player = player_x, player[1]
        return player    
    if move == "RIGHT":
        player_x = player[0] + 1
        player = player_x, player[1]
        return player 
    if move == "UP":
        player_y = player[1] - 1
        player = player[0], player_y
        return player 
    if move == "DOWN":
        player_y = player[1] + 1
        player = player[0], player_y
        return player 
    

def get_moves(player):
    moves = {"LEFT", "RIGHT", "UP", "DOWN"}
    if player[1] <= 0:
        moves = moves - {"UP"}
    if player[1] >= 4:
        moves = moves - {"DOWN"}
    if player[0] <= 0:
        moves = moves - {"LEFT"}
    if player[0] >= 4:
        moves = moves - {"RIGHT"}
    return moves


def end_game(outcome):
    if outcome is True:
        print("You have reached the door! You won!")
        exit()
    if outcome is False:
        print("The monster got you! You lost!")
        exit()


player = get_locations(CELLS, player)
door = get_locations(CELLS, door)
monster = get_locations(CELLS, monster)
print("Welcome to the dungeon!")
print("Enter QUIT to quit")


while True:
    print("You're currently in room {}".format(player))
    moves = get_moves(player)
    print("You can move {}".format(moves))
    move = check_move(move, moves, player)
    player = move_player(player, move)
    if player == door:
        outcome = True
        end_game(True)
    elif player == monster:
        outcome = False
        end_game(False)
    else:
        continue


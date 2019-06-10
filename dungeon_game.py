import random
import os
from dungeon_graphics import monster_graphic, door_graphic




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
history = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def draw_grid(CELLS, player):
    for row in range(5):
        for col in range(5):
            if (col,row) == player:
                print("[@]", end=" ")
            elif (col, row) in history:
                print("[.]", end=" ")
            else:
                print("[ ]", end=" ")
        print("\n")
        
    

def get_locations():
    return random.sample(CELLS, 3)


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
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1 
    if move == "DOWN":
        y += 1
    return x, y  
    

def get_moves(player):
    moves = {"LEFT", "RIGHT", "UP", "DOWN"}
    x, y = player
    if y == 0:
        moves = moves - {"UP"}
    if y == 4:
        moves = moves - {"DOWN"}
    if x == 0:
        moves = moves - {"LEFT"}
    if x == 4:
        moves = moves - {"RIGHT"}
    return moves


def end_game(outcome, graphic):
    if outcome is True:
        os.system("clear")
        print(door_graphic)
        print("You have reached the door! You won!")
        exit()
    if outcome is False:
        os.system("clear")
        print(monster_graphic)
        print("The monster got you! You lost!")
        exit()


player, door, monster = get_locations()
clear_screen()
print("player: ", player)
print("monster: ", monster)
print("door: ", door)
print("Welcome to the dungeon! Try to escape without getting caught by " 
      "the monster!")
print("Enter QUIT to quit")


while True:
    draw_grid(CELLS, player)
    print("You're currently in room {}".format(player))
    history.append(player)
    moves = get_moves(player)
    print("You can move {}".format(moves))
    move = check_move(move, moves, player)
    print("move checked succes")
    player = move_player(player, move)
    history.append(player)
    if player == door:
        outcome = True
        end_game(True, door_graphic)
    elif player == monster:
        outcome = False
        end_game(False, monster_graphic)
    else:
        clear_screen()
        continue


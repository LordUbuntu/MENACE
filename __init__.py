import json  # for persistent memory
import os





# what square "colors" are open on the current board state
open_tiles = [*range(9)]
# constants representing each player occupancy with a number
NO_ONE = 0
MENACE = 1
PLAYER = 2
# which tile is occupied by which player
board_state = [NO_ONE] * 9
# constants representing the number of beads added/removed in learning
REWARD = 2
TIE = 1
PUNISH = 1
# which bead was picked for which board state represented as a list of tuples of (bead_number, board_state), for learning
actions = []
# the "neural network" of MENACE. Represents each board state as a hashable string with a corresponding list reprensenting the matchbox of beads
matchboxes = { "         ": [0, 1, 2, 3, 4, 5, 6, 7, 8] }
# the current generation of MENACE
generation = 0
# interesting note: move order doesn't need to be remembered, only the choice for each board state


def save(filename, generation, matchboxes):
    """
    save(filename, generation, matchboxes)

    Serialize [generation, matchboxes] for persistent storage.
    """
    with open(filename, "w") as file:
        try:
            json.dump([generation, matchboxes], file)
        except:
            print("failed to save to {}".format(filename))


def load(filename):
    """
    load(filename)

    Deserialize a json file and return [generation, matchboxes]
        stored within it. For persistent memory of MENACE.
    """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            generation, matchboxes = json.load(file)
    else:
    return [generation, matchboxes]


def learn(matchboxes, winner):
    """
    learn(matchboxes, winner)

    Backpropogate and reinforce winning/tie beads to help MENACE
        learn what moves work well for it and what moves do not.
    """
    pass

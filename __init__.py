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

    Serialize current [generation, matchboxes] for persistent storage.
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
    If no file exists, return default struct definitions instead.
    """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            generation, matchboxes = json.load(file)
    else:
        generation = 0
        matchboxes = { "         ": [0, 1, 2, 3, 4, 5, 6, 7, 8] }
    return [generation, matchboxes]


def learn(matchboxes, winner, actions):
    """
    learn(matchboxes, winner, actions)

    Backpropogates learned information into matchboxes based on who
        the winner is using move informtion from actions.
    """
    # punish MENACE for losing against the player by taking some
    #   beads from the matchboxes used during the game.
    if winner == PLAYER:
        for bead, state in actions:
            for _ in range(PUNISH):
                matchboxes[state].remove(bead)
        # # punish MENACE for losing (remove beads from matchboxes)
        # win = winner(board_state)
        # if win == PLAYER:
        #     # show the board state
        #     show_board(generation, board_state)
        #     # remove PUNISH beads in the states that realized the loss
        #     for bead, state in actions:
        #         for _ in range(PUNISH):
        #             matchboxes[state].remove(bead)
        #     # show player win
        #     print("===== YOU WIN =====")
        #     break
        # # reward MENACE for winning (more of the same beads)
        # if win == MENACE:
        #     # show the board state
        #     show_board(generation, board_state)
        #     # add REWARD beads in the states that realized the win
        #     for bead, state in actions:
        #         for _ in range(REWARD):
        #             matchboxes[state].append(bead)
        #     # show MENACE win
        #     print("===== MENACE WINS =====")
        #     break
        # # add a random bead for a tie
        # if len(open_tiles) <= 0:
        #     # show the board state
        #     show_board(generation, board_state)
        #     # add TIE beads to everything anyways
        #     for bead, state in actions:
        #         for _ in range(TIE):
        #             matchboxes[state].append(bead)
        #     # show tie
        #     print("===== TIE =====")
        #     break
    pass

import json  # for persistent memory
import os


def save(filename, matchboxes, generation):
    """
    save(filename, matchboxes, generation)

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
        generation = 0
        matchboxes = { "         ": [0, 1, 2, 3, 4, 5, 6, 7, 8] }
    return [generation, matchboxes]


def learn(matchboxes, winner):
    """
    learn(matchboxes, winner)

    Backpropogate and reinforce winning/tie beads to help MENACE
        learn what moves work well for it and what moves do not.
    """
    pass

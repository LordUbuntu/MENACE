import json  # for persistent memory


def save(filename, matchboxes, generation):
    """
    save(filename, matchboxes, generation)

    Serialize the matchboxes and generation number to enable
        persistent memory of MENACE.
    """
    with open(filename, "w") as file:
        try:
            json.dump([generation, matchboxes], file)
        except:
            print("failed to save to {}".format(filename))


def load(file):
    """
    load(file)

    Deserialize a json file and return the matchboxes and generation
        stored within it. For persistent memory of MENACE.
    """
    pass


def learn(matchboxes, winner):
    """
    learn(matchboxes, winner)

    Backpropogate and reinforce winning/tie beads to help MENACE
        learn what moves work well for it and what moves do not.
    """
    pass

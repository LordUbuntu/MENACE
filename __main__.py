def main():
    # retrieve any memory if it exists
    matchboxes = load_memory()
    # start the game
    game_running = True
    while game_running:
        # CHECK FOR A TIE

        # add a random bead for a tie
        if len(open_tiles) <= 0:
            # show the board state
            clear()
            show_board(board_state)
            # add TIE beads to everything anyways
            for bead, state in actions:
                for _ in range(TIE):
                    matchboxes[state].append(bead)
            # show tie
            print("===== TIE =====")
            break

        # MENACE TAKES ITS TURN

        # show board state before
        clear()
        show_board(board_state)
        sleep(DELAY)
        # generate a matchbox if it doesn't exist for this board state
        if board_string(board_state) not in matchboxes:
            matchboxes.update({
                board_string(board_state): [*open_tiles]
            })
        # generate a random bead if a matchbox is empty
        if not matchboxes[board_string(board_state)]:
            matchboxes.update({
                board_string(board_state): [choice(open_tiles)]
            })
        # menace picks a bead from the matchbox for the current state
        # and action is recorded for later backpropogation
        bead = choice(matchboxes[board_string(board_state)])
        actions.append((bead, board_string(board_state)))
        # remove from open_tiles
        open_tiles.remove(bead)
        # menace updates board state with its move
        board_state[bead] = MENACE
        # show decision
        clear()
        show_board(board_state)

        # CHECK FOR MENACE WIN

        # determine winners and train MENACE based on that
        win = winner(board_state)
        # reward MENACE for winning (more of the same beads)
        if win == MENACE:
            # show the board state
            clear()
            show_board(board_state)
            # add REWARD beads in the states that realized the win
            for bead, state in actions:
                for _ in range(REWARD):
                    matchboxes[state].append(bead)
            print(board_state, winner(board_state), open_tiles)
            # show MENACE win
            print("===== MENACE WINS =====")
            break

        # CHECK FOR A TIE

        # add a random bead for a tie
        if len(open_tiles) <= 0:
            # show the board state
            clear()
            show_board(board_state)
            # add TIE beads to everything anyways
            for bead, state in actions:
                for _ in range(TIE):
                    matchboxes[state].append(bead)
            # show tie
            print("===== TIE =====")
            break

        # PLAYER TAKES THEIR TURN

        # validate and retrieve player input
        # (must be int and in open_tiles)
        valid_input = False
        while not valid_input:
            # display board state after MENACE move before player move
            clear()
            show_board(board_state)
            try:
                X = int(input("""
                1|2|3
                -+-+-
                4|5|6
                -+-+-
                7|8|9
                """))
                X -= 1  # correct offset
            except:
                exit()
            if X not in open_tiles:
                continue
            else:
                valid_input = True
        # remove from open_tiles
        open_tiles.remove(X)
        # update board state with player move
        board_state[X] = PLAYER

        # CHECK PLAYER WIN

        # punish MENACE for losing (remove beads from matchboxes)
        win = winner(board_state)
        if win == PLAYER:
            # show the board state
            clear()
            show_board(board_state)
            # remove PUNISH beads in the states that realized the loss
            for bead, state in actions:
                for _ in range(PUNISH):
                    matchboxes[state].remove(bead)
            # show player win
            print("===== YOU WIN =====")
            break

        # CHECK FOR A TIE

        # add a random bead for a tie
        if len(open_tiles) <= 0:
            # show the board state
            clear()
            show_board(board_state)
            # add TIE beads to everything anyways
            for bead, state in actions:
                for _ in range(TIE):
                    matchboxes[state].append(bead)
            # show tie
            print("===== TIE =====")
            break

    # store any learned memory
    save_memory(matchboxes)



if __name__ == '__main__':
    main()

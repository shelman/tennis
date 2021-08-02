PLAYERS = ['P1', 'P2', 'P3', 'P4', 'P5']
RACKETS = ['R1', 'R2', 'R3', 'R4']


def state_to_string(state):
    return f'({state["R1"]} and {state["R2"]}) vs. ({state["R3"]} and {state["R4"]})'


def state_equals(state_one, state_two):
    for racket in RACKETS:
        if state_one.get(racket, None) != state_two.get(racket, None):
            return False

    return True


def main():
    states_seen = set()
    current_state = {
        'R1': 'P1',
        'R2': 'P2',
        'R3': 'P3',
        'R4': 'P4',

        # flipped bookkeeping to make racket reassignment easier
        'P1': 'R1',
        'P2': 'R2',
        'P3': 'R3',
        'P4': 'R4',
    }

    next_player_out_index = 0
    next_player_in_index = 4
    while not state_to_string(current_state) in states_seen:
        print(state_to_string(current_state))

        states_seen.add(state_to_string(current_state))
        next_player_out = PLAYERS[next_player_out_index]
        next_player_in = PLAYERS[next_player_in_index]
        #print(f'{next_player_in} in, {next_player_out} out')

        # give the new player the old player's racket
        current_state[next_player_in] = current_state[next_player_out]
        current_state[current_state[next_player_in]] = next_player_in
        del current_state[next_player_out]

        next_player_in_index = (next_player_in_index + 1) % len(PLAYERS)
        next_player_out_index = (next_player_out_index + 1) % len(PLAYERS)





if __name__ == '__main__':
    main()
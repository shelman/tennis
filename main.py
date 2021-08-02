PLAYERS = ['P1', 'P2', 'P3', 'P4', 'P5']
RACKETS = ['R1', 'R2', 'R3', 'R4']
RACKET_SERVE_ORDER = ['R1', 'R3', 'R2', 'R4']


def get_teammate(current_state, player):
    if current_state[player] == 'R1':
        return current_state['R2']
    if current_state[player] == 'R2':
        return current_state['R1']
    if current_state[player] == 'R3':
        return current_state['R4']
    if current_state[player] == 'R4':
        return current_state['R3']


def print_game_record(game_record):
    for player in PLAYERS:
        print(f'Player {player} used rackets: {", ".join(list(game_record[player]["rackets_held"]))} and had '
              f'teammates {", ".join(list(game_record[player]["teammates_played_with"]))}')


def state_to_string(state):
    return f'({state["R1"]} and {state["R2"]}) vs. ({state["R3"]} and {state["R4"]})'


def update_game_record(current_state, game_record):
    for player in PLAYERS:
        if player in current_state:
            game_record[player]['rackets_held'].add(current_state[player])
            game_record[player]['teammates_played_with'].add(get_teammate(current_state, player))


def main():
    game_record = {
        player: { 'rackets_held': set(), 'teammates_played_with': set() }
        for player in PLAYERS
    }

    states_seen = set()
    current_state = {
        # racket -> player
        'R1': 'P1',
        'R2': 'P2',
        'R3': 'P3',
        'R4': 'P4',

        # player -> racket (flipped bookkeeping to make racket reassignment easier)
        'P1': 'R1',
        'P2': 'R2',
        'P3': 'R3',
        'P4': 'R4',
    }

    server = 'P1'
    referee = 'P5'
    serve_order_index = 0

    while not state_to_string(current_state) in states_seen:
        update_game_record(current_state, game_record)
        states_seen.add(state_to_string(current_state))

        # give the referee the server's racket
        current_state[referee] = current_state[server]
        current_state[current_state[referee]] = referee
        del current_state[server]

        # banish the server from the game
        referee = server

        # give the next server their turn
        serve_order_index = (serve_order_index + 1) % len(RACKET_SERVE_ORDER)
        server = current_state[RACKET_SERVE_ORDER[serve_order_index]]

    print_game_record(game_record)


if __name__ == '__main__':
    main()
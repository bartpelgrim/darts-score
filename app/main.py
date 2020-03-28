from match import Match
from player import Player


def run():
    match = Match()
    player_count = int(input('How many players? '))
    for i in range(player_count):
        player_name = input(f'Player {i+1} name: ')
        match.add_player(Player(player_name))
    match.start()
    while True:
        for player in match.players:
            print(f'Player {player.initial}: Games: {player.games_won} - Score: {player.score}')
        received_input = input(f'Player {match.game.active_player.initial} score: ')
        if received_input == 'exit':
            break
        try:
            match.enter_score(int(received_input))
        except ValueError:
            print('Please enter a number, or type "exit" to quit')


if __name__ == '__main__':
    run()

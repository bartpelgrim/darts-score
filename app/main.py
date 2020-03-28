from match import Match
from matrix import MatrixDriver
from player import Player


def run():
    match = Match()
    matrix_driver = MatrixDriver()
    player_count = int(input('How many players? '))
    for i in range(player_count):
        player_name = input(f'Player {i+1} name: ')
        match.add_player(Player(player_name))
    match.start()
    while True:
        matrix_driver.matrix.Clear()
        for i in range(len(match.players)):
            initial = match.players[i].initial
            score = match.players[i].score
            matrix_driver.draw_text(i, f'{initial}:{score}')
            if match.players[i] == match.game.active_player:
                matrix_driver.draw_active_player(i)
        if len(match.players) == 2:
            matrix_driver.draw_games_won(match.players[0].games_won, match.players[1].games_won)

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

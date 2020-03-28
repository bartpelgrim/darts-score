from typing import List

from game import Game
from matrix import MatrixDriver
from match import Match


class MatrixController:
    def __init__(self):
        self.matrix_driver = MatrixDriver()

    def draw_game_scores(self, game: Game):
        self.matrix_driver.matrix.Clear()
        for i in range(len(game.players)):
            initial = game.players[i].initial
            score = game.players[i].score
            self.matrix_driver.draw_text(i, f'{initial}:{score}')
            if game.players[i] == game.active_player:
                self.matrix_driver.draw_active_player(i)

    def draw_games_won(self, match: Match):
        if len(match.players) == 2:
            self.matrix_driver.draw_games_won(match.players[0].games_won, match.players[1].games_won)

from controller import MatrixController
from game import Game
from player import Player


class Match:
    def __init__(self):
        self.players = []
        self.iterator = None
        self.game = None
        self.matrix_controller = MatrixController()

    def add_player(self, player: Player):
        self.players.append(player)

    def start(self):
        self.iterator = iter(self.players)
        self.start_new_game()

    def next_starting_player(self) -> Player:
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.players)
            return next(self.iterator)

    def enter_score(self, amount: int) -> bool:
        valid_score = self.game.record_player_score(amount)
        if valid_score:
            self.display_scores()
            if self.game.ended:
                self.start_new_game()
            return True
        return False

    def start_new_game(self):
        self.game = Game(self.players, 501, self.next_starting_player())
        self.display_scores()

    def restart(self):
        for player in self.players:
            player.games_won = 0
        self.start_new_game()

    def display_scores(self):
        pass
        self.matrix_controller.draw_game_scores(self.game)
        self.matrix_controller.draw_games_won(self)

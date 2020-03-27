from app.game import Game
from app.player import Player


class Match:
    def __init__(self):
        self.players = []
        self.iterator = None
        self.game = None

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

    def enter_score(self, amount: int):
        self.game.record_player_score(amount)
        if self.game.ended:
            self.start_new_game()

    def start_new_game(self):
        self.game = Game(self.players, 501, self.next_starting_player())

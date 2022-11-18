from exception import InvalidScoreException
from player import Player

GAME_STARTING_SCORE = 501


class Game:
    def __init__(self, players: list, starting_score: int, starting_player: Player):
        self.players = players
        self.player_queue = iter(self.players)
        self.starting_score = starting_score
        self.reset_score()
        self.active_player = None
        self.ended = False
        self.set_turn_to_starting_player(starting_player)

    def reset_score(self):
        for player in self.players:
            player.score = self.starting_score

    def set_turn_to_starting_player(self, starting_player):
        while self.active_player != starting_player:
            self.next_player()

    def next_player(self):
        try:
            self.active_player = next(self.player_queue)
        except StopIteration:
            self.player_queue = iter(self.players)
            self.active_player = next(self.player_queue)

    def record_player_score(self, amount: int) -> bool:
        try:
            self.active_player.record_score(amount)
            if self.active_player.wins():
                self.active_player.games_won += 1
                self.ended = True
            self.next_player()
            return True
        except InvalidScoreException:
            return False



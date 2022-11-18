from exception import InvalidScoreException


class Player:
    def __init__(self, name: str):
        self.name = name
        self.initial = self.name[0].upper()
        self.score = 0
        self.games_won = 0

    def record_score(self, amount: int):
        if amount < 0 or amount > 180:
            raise InvalidScoreException
        new_score = self.score - amount
        if new_score < 0 or new_score == 1:
            raise InvalidScoreException
        self.score = new_score

    def wins(self) -> bool:
        if self.score == 0:
            return True
        else:
            return False

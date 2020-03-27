from dataclasses import dataclass

from app.exception import InvalidScoreException


@dataclass
class Player:
    initial: str
    score: int = 0
    games_won: int = 0

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

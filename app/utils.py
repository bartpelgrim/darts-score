def is_finish_score(score: int) -> bool:
    return score in list(range(1, 158)) + [160, 161, 164, 167, 170]

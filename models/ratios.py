from typing import Callable

from models.challenge import Challenge
from models.feature import Feature
from utils import FeatureRatio

RatioLambda = Callable[[Feature, Challenge], FeatureRatio]

sorting_ratios: list[tuple[RatioLambda, str]] = [
    (lambda f, c: [(f, f.daily_users / f.difficulty) for f in f], "Users/Diff"),
    (lambda f, c: [(f, f.daily_users) for f in f], "Users"),
    (lambda f, c: [(f, f.difficulty) for f in f], "Difficulty"),
    (lambda f, c: [(f, f.daily_users / len(f.get_binaries())) for f in f], "Users/Bin"),
    (lambda f, c: [(f, f.daily_users / len(f.services)) for f in f], "Users/Services"),
    (lambda f, c: [(f, f.daily_users / f.difficulty / len(f.services)) for f in f], "Users/Diff/Services"),
]

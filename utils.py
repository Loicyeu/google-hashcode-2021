from models.challenge import Challenge
from models.feature import Feature

# from models.ratios import RatioLambda
from models.features import Features

FeatureRatio = list[tuple[Feature, float]]


def sort_features(func, features: list[Feature], challenge: Challenge, reverse: bool = False) -> Features:
    """
    Return a list of features sorted by a ratio created by a given function
    The first one will be fascinating to implement, the last one will be meh

    :param func: The function to create ratios for sorting
    :param features: The list of features to sort
    :param challenge: The challenge
    :param reverse: If the sort must be reversed
    :return: A list of the features sorted
    """
    ratio = sorted(
        func(features, challenge),
        key=lambda feat: feat[1],
        reverse=not reverse)
    return Features([r[0] for r in ratio])


def get_ratios(func, features: list[Feature], challenge: Challenge, reverse: bool = False) -> FeatureRatio:
    return sorted(
        func(features, challenge),
        key=lambda feat: feat[1],
        reverse=not reverse)


def remove_duplicates(l: list) -> list:
    return list(dict.fromkeys(l))

from models.challenge import Challenge
from models.feature import Feature

# from models.ratios import RatioLambda

FeatureRatio = list[tuple[Feature, float]]


def get_ratios(func, features: list[Feature], challenge: Challenge, reverse: bool = False) -> FeatureRatio:
    """
    Return a list of features sorted by a ratio created by a given function
    The first one will be fascinating to implement, the last one will be meh

    :param func: The function to create ratios for sorting
    :param features: The list of features to sort
    :param challenge: The challenge
    :param reverse: If the sort must be reversed
    :return: A list of the features sorted
    """
    # For every feature in l, order it by the ratio, the bigger being the first one
    return sorted(
        func(features, challenge),
        key=lambda feat: feat[1],
        reverse=not reverse)


def remove_duplicates(l: list) -> list:
    return list(dict.fromkeys(l))

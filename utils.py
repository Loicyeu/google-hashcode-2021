from models.feature import Feature

FeatureRatio = list[tuple[Feature, float]]


def get_ratios(f: list[Feature]) -> FeatureRatio:
    """
    Return a list of features sorted by the ratio of daily users by difficulty.
    The first one will be fascinating to implement, the last one will be meh
    :param f: the list of features to implement
    :return: a list of the features sorted
    """
    # For every feature in l, order it by the ratio, the bigger being the first one
    return sorted([(f, f.daily_users / f.difficulty) for f in f], key=lambda feat: feat[1], reverse=True)


def remove_duplicates(l: list) -> list:
    return list(dict.fromkeys(l))

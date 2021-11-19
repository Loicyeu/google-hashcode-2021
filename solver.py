#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module de résolution du projet Poly#.
"""

from models.feature import Feature


def solve(challenge):
    """Résout un challenge donné.
    """
    return a_solution


def get_ratios(l: list[Feature]):
    """
    Return a list of features sorted by the ratio of daily users by difficulty.
    The first one will be super interesting to implement, the last one will be meh
    :param l: the list of features to implement
    :return: a list of the features sorted
    """
    # For every feature in l, order it by the ratio, the bigger being the first one
    return sorted([(f, f.daily_users / f.difficulty) for f in l], key=lambda feat: feat[1], reverse=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module de résolution du projet Poly#.
"""
from models.challenge import Challenge
from models.engineer import Engineer
from models.feature import Feature
from utils import FeatureRatio


def solve(challenge: Challenge, features: FeatureRatio):
    """
    Solve a given challenge.

    :param challenge: The given challenge
    :param features: a sorted list of features
    """

    engineers = {}
    for engineer in range(challenge.engineers):
        engineers[engineer] = Engineer(engineer, challenge.days_for_binary)

    feature: Feature = features[0][0]
    for bin in feature.get_binaries():
        engineers[1].implement(feature, bin)

    return None


if __name__ == '__main__':
    solve(Challenge(100, 2, 1, 1, 1), [])

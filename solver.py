#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module de résolution du projet Poly#.
"""
from models.challenge import Challenge
from models.engineer import Engineer
from models.engineers import Engineers
from models.feature import Feature
from utils import FeatureRatio


def solve(challenge: Challenge, features: FeatureRatio):
    """
    Solve a given challenge.

    :param challenge: The given challenge
    :param features: a sorted list of features
    """

    # engineers = [Engineer(e, challenge.days_for_binary) for e in range(challenge.engineers)]
    engineers = Engineers(challenge.engineers, challenge.days_for_binary)

    for i in range(len(features)):
        feature: Feature = features[i][0]
        for j in range(len(feature.get_binaries())):
            bin = feature.get_binaries()[j]
            engineers.get_engineer().implement(feature, bin)

    # for t in features:
    #     feature: Feature = t[0]
    #     for bin in feature.get_binaries():
    #         for engineer in engineers:
    #             engineer.implement(feature, bin)

    print(challenge.get_score([f[0] for f in features], engineers.get_all()))

# if __name__ == '__main__':
#     solve(Challenge(100, 2, 1, 1, 1), [])

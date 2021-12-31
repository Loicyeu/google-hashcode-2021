#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module de résolution du projet Poly#.
"""
from models.challenge import Challenge
from models.engineers import Engineers
from models.feature import Feature
from utils import FeatureRatio


def solve(challenge: Challenge, features: FeatureRatio) -> Engineers:
    """
    Solve a given challenge.

    :param challenge: The given challenge
    :param features: a sorted list of features
    """

    engineers = Engineers(challenge.engineers, challenge.days_for_binary, challenge.days)

    for i in range(len(features)):
        feature: Feature = features[i][0]
        for j in range(len(feature.get_binaries())):
            if engineers.finished():
                return engineers
            bin = feature.get_binaries()[j]
            engineers.get_engineer().implement(feature, bin)
    return engineers

    # Challenge.print_trace([f[0] for f in features], engineers.get_all())
    # print(challenge.get_score([f[0] for f in features]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module de résolution du projet Poly#.
"""
from models.challenge import Challenge
from models.engineers import Engineers
from models.feature import Feature
from models.features import Features
from utils import FeatureRatio


def solve(challenge: Challenge, features: FeatureRatio) -> Engineers:
    """
    Solve a given challenge.
    The strategy used is to sort the feature in a certain order. Then we take the first feature and we split the
    differents binaries to implement with the engineers that worked the least. If a feature cannot be implemented during
    the challenge days, we skip it.

    :param challenge: The given challenge
    :param features: A sorted list of features
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


def solve2(challenge: Challenge, features: Features) -> Engineers:
    """
    Solve a given challenge.
    The strategy used is to sort the feature in a certain order. Then we take the first feature and we split the
    differents binaries to implement with the engineers that worked the least. If a feature cannot be implemented during
    the challenge days, we skip it.

    :param challenge: The given challenge
    :param features: A sorted list of features
    """

    engineers = Engineers(challenge.engineers, challenge.days_for_binary, challenge.days)

    while True:
        next_features = features.next(5)
        if len(next_features) == 0:
            break
        feat_score = []
        for f in next_features:
            is_implentable, score = challenge.is_implentable(f, engineers)
            if not is_implentable:
                features.set_done(f)
            else:
                feat_score.append((f, score))
        if len(feat_score) == 0:
            continue
        feature = max(feat_score, key=lambda fc: fc[1])[0]
        features.set_done(feature)
        for j in range(len(feature.get_binaries())):
            if engineers.finished():
                return engineers
            bin = feature.get_binaries()[j]
            engineers.get_engineer().implement(feature, bin)
    return engineers

    # Challenge.print_trace([features[0] for features in features], engineers.get_all())
    # print(challenge.get_score([features[0] for features in features]))

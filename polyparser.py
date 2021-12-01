#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module de parsing des fichiers d'entrée pour la mise en oeuvre du projet Poly#.
"""
from pprint import pprint

from models.binary import Binary
from models.challenge import Challenge
from models.feature import Feature
from models.service import Service


def parse_challenge(filename: str) -> object:
    """Lit un fichier de challenge et extrait les informations nécessaires.
    """
    with open(filename, 'r') as outfile:
        content = outfile.read()

    line_list = [line.split(" ") for line in content.split('\n')]
    # pprint(line_list)

    first_line = line_list[0]

    challenge: Challenge = Challenge(int(first_line[0]), int(first_line[1]), int(first_line[4]), int(first_line[2]),
                                     int(first_line[5]))
    services: list[Service] = []

    for binary in range(int(first_line[3])):
        challenge.binaries.append(Binary(binary))

    i = 1
    for i in range(1, len(line_list)):
        line = line_list[i]
        if len(line) != 2:
            break
        else:
            service = Service(line[0], challenge.binaries[int(line[1])])
            services.append(service)
            challenge.binaries[int(line[1])].services.append(service)

    for j in range(i, len(line_list), 2):  # pas de 2
        line1 = line_list[j]
        line2 = line_list[j + 1]
        feature: Feature = Feature(line1[0], int(line1[2]), int(line1[3]))
        for k in line2:
            service = (list(filter(lambda s: s.name == k, services)))[0]  # s est le nom d'un service
            service.features.append(feature)
    print(challenge)
    return challenge


if __name__ == '__main__':
    parse_challenge("challenge.txt")

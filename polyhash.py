#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module principal pour la mise en oeuvre du projet Poly#.
"""
from models.challenge import Challenge
from models.engineers import Engineers
from models.writer import Writer
from polyparser import parse_challenge
from solver import solve
from utils import get_ratios

if __name__ == "__main__":
    # On fournit ici un exemple permettant de passer un simple
    # argument (le fichier du challenge) en paramètre. N'hésitez pas à
    # compléter avec d'autres paramètres.
    import argparse

    parser = argparse.ArgumentParser(description='Solve Poly# challenge.')
    parser.add_argument('challenge', type=str,
                        help='challenge definition filename',
                        metavar="challenge.txt")
    args = parser.parse_args()

    challenge, features = parse_challenge(args.challenge)
    engineers: Engineers = solve(challenge, get_ratios(features))

    Challenge.print_trace([f for f in features], engineers.get_all())
    print(challenge.get_score([f for f in features]))
    Writer().writeToFile()

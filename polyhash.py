from core.polyparser import parse_challenge
from core.polysolver import solve2
from models.engineers import Engineers
from utils.ratios import sorting_ratios
from utils.utils import sort_features
from utils.writer import Writer

if __name__ == "__main__":
    # On fournit ici un exemple permettant de passer un simple
    # argument (le fichier du challenge) en paramètre. N'hésitez pas à
    # compléter avec d'autres paramètres.
    import argparse

    parser = argparse.ArgumentParser(description='Solve Poly# challenge.')
    parser.add_argument('challenge', type=str,
                        help='challenge definition filename',
                        metavar="challenges/an_example.txt")
    args = parser.parse_args()

    results = []
    for ratio in sorting_ratios:
        for reverse in [False, True]:
            challenge, features = parse_challenge(args.challenge)
            engineers: Engineers = solve2(challenge, sort_features(ratio[0], features, challenge, reverse))

            results.append((challenge.get_score([f for f in features]), f"{ratio[1]} {'reverse' if reverse else ''}"))
            Writer().writeToFile(f"solutions/{ratio[1].replace('/', '-')}{' reverse' if reverse else ''}.txt")
    results.sort(key=lambda res: res[0], reverse=True)
    for r in results:
        print(f"{r[0]:,} --> {r[1]}")

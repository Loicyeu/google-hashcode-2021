# Projet Poly# - [N]apoléon

## I - L'équipe (N)

- **Blain Killian** *<killian.blain@etu.univ-nantes.fr>*
- **Charpentier Nathan** *<nathan.charpentier@etu.univ-nantes.fr>*
- **Henry Loïc** *<loic.henry@etu.univ-nantes.fr>*
- **Lajnef Yousri** *<yousri.lajnef@etu.univ-nantes.fr>*

---

## II - Descriptif général du projet

L'objectif de ce projet est d'organiser le travail d'ingénieurs qui doivent livrer des fonctionnalités qui raviront les
utilisateurs autant que possible. Pour cela, les ingénieurs doivent travailler de manière individuelle sur des
services (rangés dans des binaires) qui composent les dites fonctionnalités. Pour résoudre ce problème, on pose :

### Les fonctionnalités.

Par exemple : les listes de lecture vidéo dans YouTube.

### Les services.

Par exemple : YouTube peut disposer d'un service chargé de télécharger et stocker les collections de vidéos des
utilisateurs.

### Les binaires sont des groupes de services qui sont combinés pour s'exécuter ensemble dans un souci d’efficacité.

Par exemple : les services exécutés dans le même binaire peuvent partager des ressources telles qu'une connexion à une
base de données.

Les ingénieurs exécutent donc les tâches programmées dans un ordre bien défini (en fonction du nombre de point qu'une
fonctionnalité peut rapporter) afin de satisfaire les utilisateurs. Plus une fonctionnalité peut rapporter de points,
plus elle touche un nombre important d'utilisateur. Il est donc important de planifier les tâches dans la limite de
temps imparti afin que les utilisateurs puissent bénéficier de ces nouvelles fonctionnalités. En prenant compte ces
paramètres, on obtient un score mit à jour à chaque fin de travail d'un ingénieur (qui si le temps le permet, continuera
de travailler avant la fin). À savoir, les fonctionnalités qui sont entièrement implémentées hors temps imparti sont
autorisées mais ne rapportent aucun point.

Pour arriver à ce résultat, les ingénieurs ont plusieurs possibilités :

- Implémenter un service.
- Déplacer un service.
- Crée un binaire.
- Attendre pendant un certain temps avant de reprendre le travail.

Afin de calculer le score, on utilise la formule suivante: `Ui ✕ max(0, L - Ii)`

où:

- Ui - Est le nombre d'utilisateurs qui bénéficient de la i-ème fonctionnalité.
- L - La limite de temps en jours
- Ii - Est le jour où la i-ème fonctionnalité a été lancée (nombre de jours nécessaires à la mettre pleinement en œuvre
  la i-ème fonctionnalité).

Le score total est une somme des scores obtenus par chaque fonctionnalité lancée.

---

## III - Lancement du projet

Au lancement du projet, nous avons commencé par prendre du recul sur le projet. Nous avons donc chacun de notre côté,
analyser et pris des notes sur le sujet en vu d'une mise en commun des informations et des premières idées. Le premier
brainstorming nous a permis de mettre au clair plusieurs points du sujet comme les différentes contraintes que doivent
respecter les ingénieurs (au niveau du temps et de la répartition des tâches pour éviter qu'ils ne travaillent tous sur
le même binaire). Compte tenu du savoir faire de chacun, nous avons décidé de répartir les tâches (voir ci-dessous) et
de travailler avec l'outil 'Code With Me' de Pycharm.

---

## IV - Répartition des tâches/fonctions du projet au sein de l'équipe

### Partie conception

- Lancement du projet : Équipe complète
- Imagination solutions possibles : Équipe complète

### Partie réalisation / implémentation

- Parser : Nathan, Loïc
- Solver : Loïc
- Writer : Killian
- Modèles : Loïc, Nathan
- Gestion du score : Loïc
- Optimisation du code : Loïc, Killian

### Partie finalisation

- Compte Rendu : Nathan
- Vidéo : Killian, Yousri
- Documentation du code : Loïc

---

## V - Procédure d'installation

Se rendre sur le [dépôt GitLab du projet](https://gitlab.univ-nantes.fr/polyhash-n/polyhash) et télécharger ou cloner le
git.

```shell
$ git clone git@gitlab.univ-nantes.fr:polyhash-n/polyhash.git
```

---

## VI - Procédure d'exécution

Une fois l'installation effectuée, l'application est prête à être lancée. Pour se faire lancer, la commande suivante dans
le dossier racine :

```shell
$ python3 polyhash.py -c challenges/an_example.txt
$ python3 polyhash.py --challenge challenges/an_example.txt
```

Le challenge peut être changé et est obligatoire. Copie de la page d'aide :

```
usage: polyhash.py [-h] -c challenges/an_example.txt

[N]apoléon Solver Poly# challenge.

optional arguments:
  -h, --help            show this help message and exit
  -c challenges/an_example.txt, --challenge challenges/an_example.txt
                        challenge definition filename
```

---

## VII - Détail des stratégies mises en œuvre et commentaire à propos des performances (temps d'exécution et place mémoire)

Nous avons fait le choix dans nos stratégies de ne pas utiliser les possibilités de créer de nouveaux binaires ou de
déplacer des services entre deux binaires. Nous nous sommes aperçus que le coût en temps d'un déplacement de service
était bien top important au vu du gain qu'il peut apporter. En effet, en plus d'être coûteux en temps, il nécessite
qu'aucun ingénieur ne travaille sur les deux binaires concernés durant tout le temps du déplacement.

Nous nous sommes dirigés vers une solution basée sur une implémentation de features triées dans un certain ordre a l'aide de
ratios calculés.

**Scores réalisés par les deux stratégies :**

|                 | An example | Breath of choice | Const opti | Distinction | Expect max | Five thousand |
|-----------------|:----------:|:----------------:|:----------:|:-----------:|:----------:|:-------------:|
| **Stratégie 1** |    540     |    11 552 060    | 24 778 969 | 73 299 742  | 35 821 807 |  111 547 554  |
| **Stratégie 2** |    540     |    5 543 662     | 24 881 270 | 73 185 071  | 35 821 807 |  111 280 279  |

**Temps d'exécutions (pour un ratio) :**

|              | An example | Breath of choice | Const opti | Distinction | Expect max | Five thousand |
|--------------|:----------:|:----------------:|:----------:|:-----------:|:----------:|:-------------:|
| **Parser**   |  0.193 ms  |     2 886 ms     |   473 ms   |   292 ms    |    6 ms    |    131 ms     |
| **Solver 1** |  0.153 ms  |       7 ms       |   204 ms   |    15 ms    |   17 ms    |     7 ms      |
| **Solver 2** |  0.152 ms  |      31 ms       |   493 ms   |    72 ms    |   102 ms   |     32 ms     |

### Stratégie n°1

La première stratégie est simple, elle consiste simplement à trier les features dans un ordre précis (utilisation des
ratios). Une fois les features triées, elles sont données dans l'ordre à chaque ingénieur. L'ingénieur choisi est celui
qui a passé le moins de temps à travailler (chaque ingénieur ayant sa propre "temporalité"). L'algorithme s'arrête de
lui-même lorsqu'il n'y a plus de features à implémenter ou lorsque tous les ingénieurs ont dépassé la limite de temps du
challenge.

### Stratégie n°2

La deuxième stratégie est une version améliorée de la première. Celle-ci, en plus de vérifier que la prochaine feature est
bien implémentable dans les délais, regarde les x prochaines features. Elle les compare par rapport au score que
celles-ci produiront. Le solveur fera alors implémenter la feature a l'ingénieur ayant travaillé le moins. L'algorithme
s'arrête de lui-même lorsqu'il n'y a plus de feature à implémenter dans les délais ou que tous les ingénieurs ont
dépassé la limite de temps du challenge.

### Stratégie expérimentale

Imaginée et conceptualisé par Killian et Nathan, cette stratégie a pour but de faire prendre à l'application tous les
chemins possible. C'est-à-dire qu'elle teste toutes les possibilités et donc toutes les solutions. Cette stratégie n'est
restée qu'a l'étape de prototype.

### Stratégie 3

La troisième stratégie est l'application de la stratégie expérimentale avec des threads python. Celui-ci n'est pas
fonctionnel en l'état du au test de toutes les solutions possible (sans prendre en compte les déplacement de service et
créations de binaire). Ce solveur a part est disponible sur la branche `solver-v2`. Il n'a volontairement pas été
intégré dans la répartition du travail de l'équipe. Il n'est pas documenté et il n'y a aucune garanti qu'il fonctionne
correctement.

---

## VIII - Description de l'organisation du code (en packages, modules, classes, fonctions)

Le code est organisé en packages pour le rendre le plus compréhensible possible. Dans l'arborescence suivante, les
dossiers et fichiers ne contenant pas de code à proprement parlé ne seront pas représentés.

```
polyhash/
├── core/
│   ├── polyparser.py
│   └── polysolver.py
├── models/
│   ├── binary.py
│   ├── challenge.py
│   ├── engineer.py
│   ├── engineers.py
│   ├── feature.py
│   ├── features.py
│   └── service.py
├── utils/
│   ├── ratios.py
│   ├── singleton.py
│   ├── utils.py
│   └── writer.py
└── polyhash.py
```

Les classes représentant les principaux objets manipulés sont situés dans le dossier `models/`, les fonctions
principales de l'application sont quant à elles placés dans `core/`. Et le dossier `utils/` contient des classes,
fonction et données utiles pour l'application mais qui ne rentrait pas dans les deux autres dossiers.

---

## IX - Bugs et limitations connues

La principle limitation connue est que le solver n'utilise pas la création de binaire et le déplacement de service. \
Le parser est également peu optimisé et donc assez lent.

Le solver 2, censé normalement augmenter les points ou tout au moins les maintenir possède un bug quand on utilise le
fichier `breath of choice` car les points obtenus sont divisés par deux. \
Le scorer ne tient pas compte du bon ordre pour le travail des ingénieurs lorsqu'ils sont plusieurs à commencer à
travailler en même temps sur le même binaire. Normalement l'ingénieur ayant le numéro le plus faible (le plus haut dans
le fichier) ne doit pas se prendre de pénalité, notre scorer distribue des pénalités mais pas sur les bons ingénieurs.

Le solver 3, ne peut pas produire de solution pour les challenges autre que `An example` du fait qu'il tente toute les
combinaisons de solutions.

---

## X - Toute autre information que vous jugerez utile de nous communiquer
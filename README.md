Projet Poly#
============

Napoléon
============

### L'équipe (N)


- Henry Loïc,  				loic.henry@etu.univ-nantes.fr
- Blain Killian, 			killian.blain@etu.univ-nantes.fr
- Charpentier Nathan, 		nathan.charpentier@etu.univ-nantes.fr
- Lajnef Yousri, 			Yousri.lajnef@etu.univ-nantes.fr


---

**Descriptif général du projet :**

L'objectif de ce projet est d'organiser le travail d'ingénieurs qui doivent livrer des fonctionnalités qui raviront les utilisateurs autant que possible. 
Pour cela, les ingénieurs doivent travailler de manière individuelle sur des services (ranger dans des binaires) qui composent les dites fonctionnalités.
Pour résoudre ce problème, on pose:

● Les fonctionnalités. 

Par exemple : les listes de lecture vidéo dans YouTube.

● Les services. 

Par exemple : YouTube peut disposer d'un service chargé de télécharger et stocker les collections de vidéos des utilisateurs.

● Les binaires sont des groupes de services qui sont combinés pour s'exécuter ensemble dans un souci d’efficacité. 

Par exemple : les services exécutés dans le même binaire peuvent partager des ressources telles qu'une connexion à une base de données.

Les ingénieurs exécutent donc les tâches programmées dans un ordre bien défini (en fonction du nombre de point qu'une fonctionnalité peut rapporter) afin de satisfaire les utilisateurs. Plus une fonctionnalité peut rapporter de points, plus elle touche un nombre important d'utilisateur. Il est donc important de planifier les tâches dans la limite de temps imparti afin que les utilisateurs puissent bénéficier de ces nouvelles fonctionnalités.
En prenant compte ces paramètres, on obtient un score mit à jour à chaque fin de travail d'un ingénieur (qui si le temps le permet, continuera de travailler avant la fin). 
A savoir, les fonctionnalités qui sont entièrement implémentées hors temps imparti sont autorisées mais ne rapportent aucun point.

Pour arriver à ce résultat, les ingénieurs ont plusieurs possibilités:

- Implémenter un service.
- Déplacer un service.
- Crée un binaire.
- Attendre pendant un certain temps avant de reprendre le travail.

Afin de calculer le score, on utilise la formule suivante:

Ui ✕ max(0, L - Ii)

où:

● Ui - Est le nombre d'utilisateurs qui bénéficient de la i-ème fonctionnalité.

● L - La limite de temps en jours

● Ii - Est le jour où la i-ème fonctionnalité a été lancée (nombre de jours nécessaires à la
mettre pleinement en œuvre la i-ème fonctionnalité).

Le score total est une somme des scores obtenus par chaque fonctionnalité lancée.

---

**Lancement du projet:**

Au lancement du projet, nous avons commencé par prendre du recul sur le projet. Nous avons donc chacun de notre 
coté, analyser et pris des notes sur le sujet en vu d'une mise en commun des informations et des premières idées.
Le premier Brainstorming nous a permis de mettre au clair plusieurs points du sujet comme les différentes contraintes
que doivent respecter les ingénieurs (au niveau du temps et de la répartition des tâches pour éviter qu'ils ne travaillent tous sur le même binaire).
Compte tenu du savoir faire de chacun, nous avons décider de répartir les tâches (voir ci-dessous) et de travailler avec l'outil 'Code With Me' de Pycharm.
---

**Répartition des tâches/fonctions du projet au sein de l'équipe:**

- Lancement du projet : Equipe complète.
- Gestion du temps et des taches : Loic, Nathan.
- Mise en place des solutions : Yousri, Nathan.
- Parser : Loic, Nathan.
- Solver : Killian, Yousri.
- Implémentation : Loic, Killian.
- Gestion du score : Loic.
- Optimisation du code : Loic.
- Compte Rendu : Nathan.
- Vidéo : Killian, Yousri.

---


**Procédure d'installation:**

---
**Procédure d'exécution:**

---

**Détail de la/des stratégie.s mise.s en oeuvre et commentaire à propos des performances (temps 
d'exécution et place mémoire):**

---
**Description de l'organisation du code (en packages, modules, classes, fonctions):**

---
**Bugs et limitations connu.e.s:**

---
**Toute autre information que vous jugerez utile de nous communiquer.**
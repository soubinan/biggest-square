# Test du grand carré

## Recommandations

1. Ecrire la fonctionnalité demandée
2. Ecrire des tests unitaire
3. Ecrire des tests fonctionnels (appel du Web Service, vérification de la réponse)
4. Ecrire un Dockerfile qui lance le serveur Python
5. Lancer les tests en automatiques avec github action :  

## Le plus grand carré

* Il s’agit de trouver le plus grand carré possible sur un plateau en évitant des obstacles
* Un plateau vous est transmis dans un fichier passé en argument du programme.
* La première ligne du plateau contient les informations pour lire la carte
  * Le nombre de lignes du plateau ;
  * Le caractère "vide" ;
  * Le caractère "obstacle" ;
  * Le caractère "plein"
* Le plateau est composé de lignes de ’caractère "vide"’ et de ’caractère "obstacle"’
* Le but du programme est de remplacer les ’caractère "vide"’ par des ’caractère "plein"’ pour représenter le plus grand carré possible
* Dans le cas où il y en a plusieurs solutions, on choisira de représenter le carré le plus en haut à gauche

## Carte valide

* Toutes les lignes doivent avoir la même longueur
* Il y a au moins une ligne d’au moins une case
* À la fin de chaque ligne il y a un retour à la ligne
* Les caractères présent dans la carte doivent être uniquement ceux présenté à la première ligne
* En cas de carte invalide vous afficherez sur la sortie d’erreur : map error suivi d’un retour à la ligne puis il passera au traitement du plateau suivant

## Exemple de fonctionnement

%>cat example_file
9.ox
```
...........................
....o......................
............o..............
...........................
....o......................
...............o...........
...........................
......o..............o.....
..o.......o................
```

%>./find_square example_file
```
.....xxxxxxx...............
....oxxxxxxx...............
.....xxxxxxxo..............
.....xxxxxxx...............
....oxxxxxxx...............
.....xxxxxxx...o...........
.....xxxxxxx...............
......o..............o.....
..o.......o................
```

%>/!\ C’est bien un carré. Même si cela n’y ressemble pas visuellement• 

## Générateur de plateaux

* Tu trouveras ci-joint un générateur de plateaux (map_gen.py) en python3 prenant trois paramètres
  * nombres de colonnes ;
  * nombres de lignes ;
  * densité des obstacles.• Consignes :

**Exercice à réaliser en python 3**

* Uniquement la librairie standard python est autorisé.
* Le programme peut prendre de 1 à N fichiers en paramètre.
* A rendre sur github.
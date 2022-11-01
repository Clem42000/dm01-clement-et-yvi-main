# Junia Devoir maison : Magic Number
## Echéance : 14/11/2022

## Fonctionnalités :
- le programme choisit un nombre aléatoire entre 1 et 100
- le programme demande à l'utilisateur de saisir un nombre entre 1 et 100
- le programme répond :
 - "Trop grand", si le nombre proposé est plus grand que le nombre magique
 - "Trop petit", si le nombre proposé est plus petit que le nombre magique
 - "Bravo, vous avez trouvé", si le nombre proposé est égale au nombre magique
- au bout de 10 essais, si l'utilisateur n'a pas trouvé le nombre magique, le programme affiche "Perdu" et s'arrête.

 ## Contraintes :
- travail à réaliser en binôme
- programme en Python
- architecture MVC avec interface et 4 packages (model, view, controller, contract)
- l'ensemble des données (texte affiché, nombre magique, valeur min et max de tirage, nombre d'essais max, ...) doit être stocké dans le modèle
- l'ensemble des affichages (print()) et des saisies (input()) doit être réalisé par la vue
- l'ensemble de la mécanique du programme (comparaison entre nombre proposé et nombre magique, ...) doit être réalisé par le controller.

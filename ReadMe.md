# ReadMe : Test technique Oryx 
## Clustering with KMeans

#### 1. Lecture de Data :

En utilisant le DataFrame Pandas, et avec la fonction read_json, j'ai pu récupérer les données et les stocker dans le un DataFrame qui me permet de manipuler tout cette data.

#### 2. Exploiter les données :

En utilisant les fonctions info(), describe() et head(), j'ai pu exploiter ces données la, j'ai pu extraire plusieurs informations tel que : 

- Le champ name est une combinaison des champs address et number.
- Les noms des rues qu'ont sont presque unique. ( une seule adresse qui est redondante)
- Aucune valeur n'est NULL, pas de valeur manquante également. 
- Avec cette volume de donnée, les variables les plus importants sont Longitude et Latitude, mais avec plus des données, les adresses et le nombre de rues peuvent devenir utile.

#### 3.  Gategorical variable : 

Pour le cas de notre DataSet, il n'est pas vraiment utile de le faire, mais dans le cas d'une DataSet plus riche avec des informations, on aura pu utiliser la variable Address. Pour cela, je l'ai appliqué en utilisant la fonction Transfert de Preprocessing SickitLearn.

Le principe est de remplacer la valeur String par des valeurs numérique, afin de faciliter l'utilisation de la variable par l'algorithme de clustering.

####4. Visualisation des informations : 

Dans notre cas, la meilleure façon de connaître les possibilités de clusters est de faire un pairplot de SeaBorn. Ceci nous aide a détecter les relations entre les différentes variables.

####5.  Choix de K pour l'algorithme KMeans : 

En effet, et dans notre exemple, ce n'était pas évident de choisir un K. Mon choix est basé sur le problématique, et la raison de clustering. J'ai pensé au performance des stations, et pour cela, j'ai pensé a K=3 avec un cluster mauvais, un cluster moyen, et un cluster bien. 

####6. Entrainer le modèle : 

Une fois le K est choisi, ça sera simple en utilisant la fonction fit afin d'entraîner l'algorithme et donner des résultats. Pour avoir les résultats, c'est bien la fonctions labels_ sur le modèle entraîné qui retourne un tableau avec les clusters pour chaque donnée.







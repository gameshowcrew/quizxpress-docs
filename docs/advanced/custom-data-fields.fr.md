# Champs de données personnalisés

Vous pouvez désormais définir votre propre dictionnaire de données dans un quiz et stocker des données arbitraires avec les diapositives du quiz. Lors de l'interfaçage avec QuizXpress, les données peuvent être récupérées via le canal TCP (commandes getslide ou getquiz) et utilisées pour piloter une logique externe, comme des effets lumineux, des effets sonores, du matériel personnalisé ou d'autres fonctionnalités. Cette logique résiderait dans une couche d'intégration autour de QuizXpress qui communique avec QX via le canal TCP entrant de MessageBroker.

Vous définissez les champs personnalisés dans votre quiz dans la boîte de dialogue File->Options, onglet Metadata :

![](../assets/images/image478.webp){ width="271" loading=lazy }

Vous pouvez ici ajouter des champs de type : string, int ou float

![](../assets/images/image479.webp){ width="462" loading=lazy }

Une fois les champs définis, ils apparaissent dans la grille de propriétés de chaque diapositive :

![](../assets/images/image480.webp){ width="235" loading=lazy }

La couche d'intégration peut récupérer les données de la diapositive en cours pour obtenir les champs personnalisés :

![](../assets/images/image481.webp){ width="485" loading=lazy }

La commande getslide renvoie les données d'une seule diapositive au format XML lisible par l'humain. Vous pouvez aussi utiliser getquiz pour obtenir les données de toutes les diapositives en un seul appel.

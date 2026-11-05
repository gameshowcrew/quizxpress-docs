# Animations d'entrée

Depuis la version 8.6, la question et les réponses peuvent faire leur entrée dans Quiz Show : au lieu d'apparaître simplement, elles apparaissent en fondu, glissent depuis le bord, surgissent, tombent en rebondissant, etc. Vous choisissez un effet pour la question et un autre pour les réponses, et vous décidez si les réponses entrent l'une après l'autre ou toutes ensemble.

## Configurer une entrée

Sélectionnez la diapositive dans Quiz Studio et ouvrez la section « Animation » des propriétés de la diapositive (dans la [grille des propriétés avancées](../user-interface-overview/advanced-properties-grid.md), vous trouvez les mêmes réglages sous « Apparence ») :

| Réglage | Effet |
|---|---|
| « Entrée de la question » | Comment la question entre. Les images qui ne sont pas des réponses entrent en même temps que la question. |
| « Entrée des réponses » | Comment les réponses entrent. Sur une question image avec plusieurs images, les images de réponse entrent comme des réponses. |
| « Ordre des réponses » | « Une par une » : les réponses entrent l'une après l'autre. « Toutes ensemble » : elles entrent en même temps. Affiché lorsqu'une entrée des réponses est choisie. |
| « Vitesse d'animation » | « Normale », « Lente » ou « Rapide ». S'applique à la question et aux réponses. |
| « Compte à rebours pendant l'animation » | Activé, le compte à rebours démarre pendant que la question et les réponses entrent encore. Désactivé (par défaut), le compte à rebours démarre dès que tout est à l'écran. |

« Ordre des réponses », « Vitesse d'animation » et « Compte à rebours pendant l'animation » n'apparaissent qu'une fois qu'une entrée est choisie pour la question ou les réponses.

Lorsque la question et les réponses ont toutes deux une entrée, les réponses commencent quand la question est à mi-chemin, pour un enchaînement fluide.

## Effets

| Effet | Ce que vous voyez |
|---|---|
| « Aucune » | Pas d'animation : l'élément apparaît simplement (par défaut). |
| « Fondu » | L'élément apparaît en fondu. |
| « Glisser depuis la gauche » / « la droite » / « le haut » / « le bas » | L'élément glisse depuis l'extérieur de l'écran. |
| « Alterner gauche et droite » | Les réponses arrivent tour à tour de la gauche et de la droite, en commençant par la gauche. Pour la question, elle glisse depuis la gauche. |
| « Zoom avant » | L'élément grandit à partir de la moitié de sa taille tout en apparaissant en fondu. |
| « Surgir » | L'élément surgit, dépasse légèrement sa taille puis se stabilise. |
| « Retourner » | L'élément se retourne comme une carte. |
| « Tourner » | L'élément tourne sur lui-même jusqu'à sa place tout en grandissant. |
| « Tomber et rebondir » | L'élément tombe du haut et rebondit avant de se stabiliser. |

Avec la vitesse « Normale », un élément met environ 0,6 seconde à entrer, avec « Lente » environ 0,9 seconde et avec « Rapide » environ 0,35 seconde. « Tourner » et « Tomber et rebondir » prennent un peu plus de temps pour rester lisibles.

## Réponses affichées plus tard

Si les réponses ne sont pas affichées tout de suite, parce que « Montrer les réponses » est réglé sur « Cacher et montrer les réponses une par une » ou « Cacher et montrer en une fois », l'« Entrée des réponses » est utilisée chaque fois que des réponses apparaissent.

## Diapositives prises en charge

Les animations d'entrée fonctionnent sur les diapositives de question et sur les autres types de diapositives qui affichent une question et des réponses. Elles ne sont pas disponibles pour Trivia Feud, les manches de Bingo, les mini-jeux, les manches Trivia Board et Trivia Ladder ; pour ces diapositives, les réglages « Animation » ne sont pas affichés.

!!! tip
    Les animations d'entrée se combinent bien avec les [animations d'apparition du texte](text-reveal-animations.md) : faites glisser la question puis révélez son texte mot par mot, ou faites tomber les réponses une par une après la lecture de la question.

# L'écran d'enregistrement des keypads et buzzers

Le but de l'écran d'enregistrement est de déterminer quels buzzers/keypads participent au quiz. En demandant aux participants de s'enregistrer explicitement, le logiciel sait combien d'appareils sont présents. Il existe trois « variantes » d'écrans d'attribution des buzzers :

- Écran Sony Buzzer Assignment

- Écran Buzzer Assignment pour moins de 100 participants

- Écran Buzzer Assignment pour plus de 100 équipes

## Écran Sony Buzzer Assignment

Avec des buzzers Sony, les noms peuvent être saisis dans le programme Quiz Setup pour chaque participant/équipe. Comme un buzzer Sony ne possède pas d'identifiant explicite, il n'est pas possible d'associer un nom d'équipe à un buzzer précis lors de la définition des noms d'équipes dans Quiz Setup. L'écran Buzzer Assignment résout ce problème : il affiche les noms des équipes un par un, et lorsqu'une équipe voit son nom apparaître à l'avant du « Buzzer Assignment Carousel », elle doit appuyer sur le buzzer pour s'enregistrer et participer au quiz. Vous trouverez ci-dessous une capture d'écran de l'écran Sony Buzzer Assignment.

![](../../assets/images/image403.webp){ width="605" loading=lazy }

En bas, vous voyez deux boutons : celui de gauche (la flèche circulaire) réinitialise les données afin que l'attribution des buzzers recommence ; le bouton le plus à droite est le bouton « start », qui démarre le quiz.

## Écran Buzzer Assignment, moins de 100 participants

Chaque keypad Reply/QuizXpress possède un identifiant unique, également utilisé dans le logiciel QuizXpress Live pour identifier un participant (par exemple, buzzer avec l'ID 1 : Équipe 1). Lorsque moins de 100 buzzers participent au quiz (selon le paramètre « Keypads » saisi dans Quiz Setup), une grille avec tous les identifiants de buzzers est affichée.

Lorsqu'une touche d'un keypad est pressée, il est enregistré comme actif dans le système QuizXpress Live. Une coche apparaît dans la grille au numéro correspondant à l'ID du buzzer utilisé.

À strictement parler, il n'est pas nécessaire que les buzzers se connectent explicitement. Cependant, le logiciel QuizXpress Live doit savoir exactement combien d'équipes participent, afin de déterminer quand toutes les équipes ont répondu à une question et d'arrêter le compte à rebours.

Le bouton affiché en bas de l'écran est le bouton « start », qui démarre le quiz. Vous trouverez ci-dessous deux captures d'écran, l'une montrant l'écran avant que quiconque se soit connecté, l'autre montrant l'état de l'écran une fois que tout le monde s'est connecté.

| ![](../../assets/images/image404.webp){ loading=lazy } | ![](../../assets/images/image405.webp){ loading=lazy } |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------|

!!! note

    à des fins de test, vous pouvez attribuer les 100 buzzers en une seule fois en appuyant sur F1, ou tous les buzzers configurés dans Quiz Setup en appuyant sur F2.*

## Écran Buzzer Assignment, plus de 100 participants

Lorsque plus de 100 buzzers sont utilisés, une grille devient de plus en plus difficile à lire. C'est pourquoi QuizXpress Live utilise dans ce cas un écran Buzzer Assignment différent. Voir ci-dessous pour une capture d'écran.

Le bouton affiché en bas de l'écran est le bouton « start », qui démarre le quiz.

!!! note

    aucun écran d'attribution des buzzers n'est affiché lors de l'utilisation de buzzers de type Keyboard ou Game port, car ces systèmes ont une attribution fixe.*
